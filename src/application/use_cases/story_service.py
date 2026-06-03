from uuid import uuid4

from src.application.ports.ai_story_port import AIStoryPort
from src.domain.entities.story import Story


class StoryService:
    def __init__(self, ai_story_port: AIStoryPort) -> None:
        self.ai_story_port = ai_story_port

    def start_story(
        self,
        image_bytes: bytes,
        genre: str,
        tone: str,
        protagonist_role: str,
    ) -> Story:
        image_analysis = self.ai_story_port.analyze_image(image_bytes)

        story = Story(
            id=str(uuid4()),
            title="Untitled Echo",
            genre=genre,
            tone=tone,
            protagonist_role=protagonist_role,
            image_analysis=image_analysis,
        )

        first_chapter = self.ai_story_port.generate_first_chapter(story)
        story.chapters.append(first_chapter)

        return story

    def continue_story(
        self,
        story: Story,
        selected_choice_id: str,
    ) -> Story:
        if story.is_complete:
            return story

        current_chapter = story.chapters[-1]
        current_chapter.selected_choice_id = selected_choice_id

        if len(story.chapters) < 5:
            next_chapter = self.ai_story_port.generate_next_chapter(
                story=story,
                selected_choice_id=selected_choice_id,
            )
            story.chapters.append(next_chapter)

        if len(story.chapters) == 5:
            story = self.ai_story_port.finalize_story(story)

        return story
