import pytest

from src.domain.entities.chapter import Chapter
from src.domain.entities.choice import Choice
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story


def create_story() -> Story:
    return Story(
        id="story-1",
        title="The First Echo",
        genre="Fantasy",
        tone="Mysterious",
        protagonist_role="Explorer",
        image_analysis=ImageAnalysis(
            setting="Ancient forest",
            mood="Mysterious",
            main_objects=["gate", "mist"],
            story_seed="A forgotten gate awakens.",
            magical_elements=["portal"],
            possible_conflict="A memory must be sacrificed.",
            suggested_title="The Whispering Gate",
        ),
    )


def create_chapter(number: int) -> Chapter:
    return Chapter(
        number=number,
        title=f"Chapter {number}",
        summary=f"Summary {number}",
        content=f"Content {number}",
        choices=[
            Choice(id="1", text="Enter the gate"),
            Choice(id="2", text="Follow the path"),
            Choice(id="3", text="Touch the rune"),
        ],
    )


def test_add_chapter() -> None:
    story = create_story()
    chapter = create_chapter(1)

    story.add_chapter(chapter)

    assert len(story.chapters) == 1
    assert story.chapters[0].number == 1


def test_get_latest_chapter() -> None:
    story = create_story()
    story.add_chapter(create_chapter(1))
    story.add_chapter(create_chapter(2))

    latest_chapter = story.get_latest_chapter()

    assert latest_chapter.number == 2


def test_get_latest_chapter_raises_error_when_empty() -> None:
    story = create_story()

    with pytest.raises(ValueError, match="Story has no chapters."):
        story.get_latest_chapter()


def test_select_choice_for_latest_chapter() -> None:
    story = create_story()
    story.add_chapter(create_chapter(1))

    story.select_choice_for_latest_chapter("2")

    assert story.get_latest_chapter().selected_choice_id == "2"


def test_can_continue() -> None:
    story = create_story()
    story.add_chapter(create_chapter(1))

    assert story.can_continue() is True


def test_cannot_continue_when_complete() -> None:
    story = create_story()
    story.is_complete = True

    assert story.can_continue() is False


def test_should_finalize_when_story_has_five_chapters() -> None:
    story = create_story()

    for chapter_number in range(1, 6):
        story.add_chapter(create_chapter(chapter_number))

    assert story.should_finalize() is True


def test_add_chapter_raises_error_after_five_chapters() -> None:
    story = create_story()

    for chapter_number in range(1, 6):
        story.add_chapter(create_chapter(chapter_number))

    with pytest.raises(ValueError, match="Story cannot have more than 5 chapters."):
        story.add_chapter(create_chapter(6))
