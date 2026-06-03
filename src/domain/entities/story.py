from dataclasses import dataclass, field

from src.domain.entities.chapter import Chapter
from src.domain.entities.image_analysis import ImageAnalysis


@dataclass
class Story:
    id: str
    title: str
    genre: str
    tone: str
    protagonist_role: str
    image_analysis: ImageAnalysis
    chapters: list[Chapter] = field(default_factory=list)
    character_profile: str | None = None
    world_description: str | None = None
    final_ending: str | None = None
    is_complete: bool = False
