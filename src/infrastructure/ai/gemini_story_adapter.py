import mimetypes
import tempfile
from pathlib import Path

from google import genai
from google.genai import types

from src.application.dto.chapter_response import ChapterResponse
from src.application.dto.image_analysis_response import ImageAnalysisResponse
from src.application.dto.story_finalization_response import (
    StoryFinalizationResponse,
)
from src.application.mappers.chapter_mapper import ChapterMapper
from src.application.mappers.image_analysis_mapper import ImageAnalysisMapper
from src.application.mappers.story_finalization_mapper import (
    StoryFinalizationMapper,
)
from src.application.ports.ai_story_port import AIStoryPort
from src.domain.entities.chapter import Chapter
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story
from src.infrastructure.ai.json_parser import parse_ai_json
from src.infrastructure.ai.prompts import (
    FINALIZATION_PROMPT,
    FIRST_CHAPTER_PROMPT,
    IMAGE_ANALYSIS_PROMPT,
    NEXT_CHAPTER_PROMPT,
)


class GeminiStoryAdapter(AIStoryPort):
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash") -> None:
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def analyze_image(self, image_bytes: bytes) -> ImageAnalysis:
        response_text = self._generate_with_image(
            prompt=IMAGE_ANALYSIS_PROMPT,
            image_bytes=image_bytes,
        )

        dto = parse_ai_json(response_text, ImageAnalysisResponse)
        return ImageAnalysisMapper.to_domain(dto)

    def generate_first_chapter(self, story: Story) -> Chapter:
        prompt = f"""
{FIRST_CHAPTER_PROMPT}

Story settings:
- Genre: {story.genre}
- Tone: {story.tone}
- Protagonist role: {story.protagonist_role}

Image analysis:
- Setting: {story.image_analysis.setting}
- Mood: {story.image_analysis.mood}
- Main objects: {story.image_analysis.main_objects}
- Story seed: {story.image_analysis.story_seed}
- Magical elements: {story.image_analysis.magical_elements}
- Possible conflict: {story.image_analysis.possible_conflict}
"""

        response_text = self._generate_text(prompt)
        dto = parse_ai_json(response_text, ChapterResponse)

        return ChapterMapper.to_domain(
            chapter_number=1,
            dto=dto,
        )

    def generate_next_chapter(
        self,
        story: Story,
        selected_choice_id: str,
    ) -> Chapter:
        chapter_number = len(story.chapters) + 1

        prompt = f"""
{NEXT_CHAPTER_PROMPT}

You are writing Chapter {chapter_number}.

Story settings:
- Genre: {story.genre}
- Tone: {story.tone}
- Protagonist role: {story.protagonist_role}

Previous chapters:
{self._format_chapters(story)}

Selected choice id:
{selected_choice_id}
"""

        response_text = self._generate_text(prompt)
        dto = parse_ai_json(response_text, ChapterResponse)

        return ChapterMapper.to_domain(
            chapter_number=chapter_number,
            dto=dto,
        )

    def finalize_story(self, story: Story) -> Story:
        prompt = f"""
{FINALIZATION_PROMPT}

Completed story:
{self._format_chapters(story)}
"""

        response_text = self._generate_text(prompt)
        dto = parse_ai_json(response_text, StoryFinalizationResponse)

        return StoryFinalizationMapper.apply(
            story=story,
            dto=dto,
        )

    def _generate_text(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )

        return response.text or ""

    def _generate_with_image(
        self,
        prompt: str,
        image_bytes: bytes,
    ) -> str:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_file.write(image_bytes)
            temp_image_path = Path(temp_file.name)

        try:
            mime_type = mimetypes.guess_type(temp_image_path)[0] or "image/png"

            uploaded_file = self.client.files.upload(
                file=str(temp_image_path),
                config=types.UploadFileConfig(
                    mime_type=mime_type,
                ),
            )

            response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    prompt,
                    uploaded_file,
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                ),
            )

            return response.text or ""

        finally:
            temp_image_path.unlink(missing_ok=True)

    def _format_chapters(self, story: Story) -> str:
        formatted_chapters = []

        for chapter in story.chapters:
            formatted_chapters.append(
                f"""
Chapter {chapter.number}: {chapter.title}
Summary: {chapter.summary}
Selected choice: {chapter.selected_choice_id}
Content:
{chapter.content}
"""
            )

        return "\n".join(formatted_chapters)
