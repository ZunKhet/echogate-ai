from pydantic import BaseModel


class StoryFinalizationResponse(BaseModel):
    character_profile: str
    world_description: str
    final_ending: str
