from dataclasses import dataclass


@dataclass
class ImageAnalysis:
    setting: str
    mood: str
    main_objects: list[str]
    story_seed: str
    magical_elements: list[str]
    possible_conflict: str
    suggested_title: str
