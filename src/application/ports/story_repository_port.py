from abc import ABC, abstractmethod

from src.domain.entities.story import Story


class StoryRepositoryPort(ABC):
    @abstractmethod
    def save(self, story: Story) -> None:
        pass

    @abstractmethod
    def get_by_id(self, story_id: str) -> Story | None:
        pass
