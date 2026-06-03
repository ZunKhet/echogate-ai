from src.application.use_cases.export_story import ExportStoryUseCase
from src.domain.entities.chapter import Chapter
from src.domain.entities.choice import Choice
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story
from src.infrastructure.document.pdf_export_adapter import PDFExportAdapter
from src.infrastructure.persistence.in_memory_story_repository import (
    InMemoryStoryRepository,
)


def create_completed_story() -> Story:
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
            suggested_title="The Whispering Gate",
        ),
        character_profile="A curious explorer.",
        world_description="A hidden realm of gates and echoes.",
        final_ending="The gate closed softly.",
        is_complete=True,
    )

    story.add_chapter(
        Chapter(
            number=1,
            title="The First Echo",
            summary="A gate awakens.",
            content="Chapter content.",
            choices=[
                Choice(id="1", text="Enter the gate"),
                Choice(id="2", text="Follow the path"),
                Choice(id="3", text="Touch the rune"),
            ],
        )
    )

    return story


def test_export_completed_story_as_pdf() -> None:
    repository = InMemoryStoryRepository()
    story = create_completed_story()
    repository.save(story)

    use_case = ExportStoryUseCase(
        story_repository=repository,
        document_exporter=PDFExportAdapter(),
    )

    result = use_case.execute(
        story_id=story.id,
        cover_image_bytes=None,
        include_cover_image=False,
    )

    assert isinstance(result, bytes)
    assert result.startswith(b"%PDF")
