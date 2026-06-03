from abc import ABC, abstractmethod

from src.domain.entities.chapter import Chapter
from src.domain.entities.image_analysis import ImageAnalysis
from src.domain.entities.story import Story


class AIStoryPort(ABC):
    @abstractmethod
    def analyze_image(self, image_bytes: bytes) -> ImageAnalysis:
        pass

    @abstractmethod
    def generate_first_chapter(self, story: Story) -> Chapter:
        pass

    @abstractmethod
    def generate_next_chapter(self, story: Story, selected_choice_id: str) -> Chapter:
        pass

    @abstractmethod
    def finalize_story(self, story: Story) -> Story:
        pass
