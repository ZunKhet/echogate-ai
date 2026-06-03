from src.application.dto.chapter_response import ChapterResponse
from src.domain.entities.chapter import Chapter
from src.domain.entities.choice import Choice


class ChapterMapper:
    @staticmethod
    def to_domain(
        chapter_number: int,
        dto: ChapterResponse,
    ) -> Chapter:
        return Chapter(
            number=chapter_number,
            title=dto.title,
            summary=dto.summary,
            content=dto.content,
            choices=[
                Choice(
                    id=choice.id,
                    text=choice.text,
                )
                for choice in dto.choices
            ],
        )
