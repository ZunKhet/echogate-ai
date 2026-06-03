from pydantic import BaseModel


class ImageAnalysisResponse(BaseModel):
    setting: str
    mood: str
    main_objects: list[str]
    story_seed: str
    magical_elements: list[str]
    possible_conflict: str
