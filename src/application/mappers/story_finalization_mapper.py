from src.application.dto.story_finalization_response import (
    StoryFinalizationResponse,
)
from src.domain.entities.story import Story


class StoryFinalizationMapper:
    @staticmethod
    def apply(
        story: Story,
        dto: StoryFinalizationResponse,
    ) -> Story:
        story.character_profile = dto.character_profile
        story.world_description = dto.world_description
        story.final_ending = dto.final_ending
        story.is_complete = True

        return story
