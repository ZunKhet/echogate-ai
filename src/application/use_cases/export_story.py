from src.application.ports.document_export_port import DocumentExportPort
from src.application.ports.story_repository_port import StoryRepositoryPort


class ExportStoryUseCase:
    def __init__(
        self,
        story_repository: StoryRepositoryPort,
        document_exporter: DocumentExportPort,
    ) -> None:
        self.story_repository = story_repository
        self.document_exporter = document_exporter

    def execute(self, story_id: str) -> bytes:
        story = self.story_repository.get_by_id(story_id)

        if story is None:
            raise ValueError(f"Story with id {story_id} was not found.")

        if not story.is_complete:
            raise ValueError("Story must be completed before export.")

        return self.document_exporter.export_story(story)
