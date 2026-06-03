from uuid import uuid4

from src.application.ports.ai_story_port import AIStoryPort
from src.application.ports.story_repository_port import StoryRepositoryPort
from src.domain.constants import MAX_CHAPTERS
from src.domain.entities.story import Story


class StoryService:
    def __init__(
        self,
        ai_story_port: AIStoryPort,
        story_repository: StoryRepositoryPort,
    ) -> None:
        self.ai_story_port = ai_story_port
        self.story_repository = story_repository

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
        story.add_chapter(first_chapter)

        self.story_repository.save(story)
        return story

    def continue_story(
        self,
        story_id: str,
        selected_choice_id: str,
    ) -> Story:
        story = self.story_repository.get_by_id(story_id)

        if story is None:
            raise ValueError(f"Story with id {story_id} was not found.")

        if story.is_complete:
            return story

        story.select_choice_for_latest_chapter(selected_choice_id)

        if story.can_continue():
            next_chapter = self.ai_story_port.generate_next_chapter(
                story=story,
                selected_choice_id=selected_choice_id,
            )
            story.add_chapter(next_chapter)

        if story.should_finalize():
            story = self.ai_story_port.finalize_story(story)

        self.story_repository.save(story)
        return story
