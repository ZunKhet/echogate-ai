from src.application.dto.chapter_response import (
    ChapterResponse,
    ChoiceResponse,
)
from src.application.dto.image_analysis_response import (
    ImageAnalysisResponse,
)
from src.application.mappers.chapter_mapper import ChapterMapper
from src.application.mappers.image_analysis_mapper import (
    ImageAnalysisMapper,
)
from src.application.dto.story_finalization_response import (
    StoryFinalizationResponse,
)
from src.application.mappers.story_finalization_mapper import (
    StoryFinalizationMapper,
)
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story


def test_image_analysis_mapper() -> None:
    dto = ImageAnalysisResponse(
        setting="Ancient Forest",
        mood="Mysterious",
        main_objects=["gate"],
        story_seed="A forgotten gate awakens.",
        magical_elements=["portal"],
        possible_conflict="Lose a memory.",
    )

    result = ImageAnalysisMapper.to_domain(dto)

    assert result.setting == "Ancient Forest"
    assert result.mood == "Mysterious"


def test_chapter_mapper() -> None:
    dto = ChapterResponse(
        title="The First Echo",
        summary="A mysterious gate appears.",
        content="Story content.",
        choices=[
            ChoiceResponse(
                id="1",
                text="Enter the gate",
            )
        ],
    )

    chapter = ChapterMapper.to_domain(
        chapter_number=1,
        dto=dto,
    )

    assert chapter.number == 1
    assert chapter.title == "The First Echo"
    assert chapter.summary == "A mysterious gate appears."


def test_story_finalization_mapper() -> None:
    story = Story(
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
        ),
    )

    dto = StoryFinalizationResponse(
        character_profile="A curious explorer who follows forgotten echoes.",
        world_description="A hidden realm of gates, memories, and moonlit paths.",
        final_ending="The gate closed, but the final echo remained.",
    )

    result = StoryFinalizationMapper.apply(
        story=story,
        dto=dto,
    )

    assert result.character_profile == (
        "A curious explorer who follows forgotten echoes."
    )
    assert result.world_description == (
        "A hidden realm of gates, memories, and moonlit paths."
    )
    assert result.final_ending == (
        "The gate closed, but the final echo remained."
    )
    assert result.is_complete is True
