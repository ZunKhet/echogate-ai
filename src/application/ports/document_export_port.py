from abc import ABC, abstractmethod

from src.domain.entities.story import Story


class DocumentExportPort(ABC):
    @abstractmethod
    def export_story(
        self,
        story: Story,
        cover_image_bytes: bytes | None = None,
        include_cover_image: bool = True,
    ) -> bytes:
        pass
