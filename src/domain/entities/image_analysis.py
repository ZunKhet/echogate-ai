from dataclasses import dataclass, field


@dataclass
class ImageAnalysis:
    setting: str
    mood: str
    main_objects: list[str]
    story_seed: str
    magical_elements: list[str] = field(default_factory=list)
    possible_conflict: str | None = None
