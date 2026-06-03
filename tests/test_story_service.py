from src.application.use_cases.story_service import StoryService
from src.infrastructure.ai.fake_story_adapter import FakeStoryAdapter
from src.infrastructure.persistence.in_memory_story_repository import (
    InMemoryStoryRepository,
)


def test_start_story_creates_first_chapter() -> None:
    story_service = StoryService(
        ai_story_port=FakeStoryAdapter(),
        story_repository=InMemoryStoryRepository(),
    )

    story = story_service.start_story(
        image_bytes=b"fake-image",
        genre="Fantasy",
        tone="Mysterious",
        protagonist_role="Explorer",
        story_title="The Gate Beneath the Moon",
    )

    assert story.title == "The Gate Beneath the Moon"
    assert story.id
    assert story.genre == "Fantasy"
    assert story.tone == "Mysterious"
    assert story.protagonist_role == "Explorer"
    assert len(story.chapters) == 1
    assert story.chapters[0].number == 1
    assert len(story.chapters[0].choices) == 3


def test_continue_story_until_complete() -> None:
    repository = InMemoryStoryRepository()

    story_service = StoryService(
        ai_story_port=FakeStoryAdapter(),
        story_repository=repository,
    )

    story = story_service.start_story(
        image_bytes=b"fake-image",
        genre="Fantasy",
        tone="Mysterious",
        protagonist_role="Explorer",
    )

    for _ in range(2):
        story = story_service.continue_story(
            story_id=story.id,
            selected_choice_id="1",
        )

    assert len(story.chapters) == 3
    assert story.is_complete is True
    assert story.character_profile is not None
    assert story.world_description is not None
    assert story.final_ending is not None
