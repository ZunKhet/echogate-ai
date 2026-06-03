from dataclasses import dataclass, field

from src.domain.constants import MAX_CHAPTERS
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

    def add_chapter(self, chapter: Chapter) -> None:
        if len(self.chapters) >= MAX_CHAPTERS:
            raise ValueError(
                f"Story cannot have more than {MAX_CHAPTERS} chapters.")

        self.chapters.append(chapter)

    def get_latest_chapter(self) -> Chapter:
        if not self.chapters:
            raise ValueError("Story has no chapters.")

        return self.chapters[-1]

    def select_choice_for_latest_chapter(self, selected_choice_id: str) -> None:
        latest_chapter = self.get_latest_chapter()
        latest_chapter.selected_choice_id = selected_choice_id

    def can_continue(self) -> bool:
        return not self.is_complete and len(self.chapters) < MAX_CHAPTERS

    def should_finalize(self) -> bool:
        return not self.is_complete and len(self.chapters) == MAX_CHAPTERS

    def rename(self, new_title: str) -> None:
        clean_title = new_title.strip()

        if not clean_title:
            raise ValueError("Story title cannot be empty.")

        self.title = clean_title
