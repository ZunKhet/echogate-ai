from dataclasses import dataclass

from src.domain.entities.choice import Choice


@dataclass
class Chapter:
    number: int
    title: str
    content: str
    choices: list[Choice]
    selected_choice_id: str | None = None
