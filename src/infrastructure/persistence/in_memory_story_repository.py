from src.application.ports.story_repository_port import StoryRepositoryPort
from src.domain.entities.story import Story


class InMemoryStoryRepository(StoryRepositoryPort):
    def __init__(self) -> None:
        self._stories: dict[str, Story] = {}

    def save(self, story: Story) -> None:
        self._stories[story.id] = story

    def get_by_id(self, story_id: str) -> Story | None:
        return self._stories.get(story_id)
