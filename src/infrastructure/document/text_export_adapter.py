from src.application.ports.document_export_port import DocumentExportPort
from src.domain.entities.story import Story


class TextExportAdapter(DocumentExportPort):
    def export_story(self, story: Story) -> bytes:
        lines = [
            story.title,
            "",
            f"Genre: {story.genre}",
            f"Tone: {story.tone}",
            f"Protagonist Role: {story.protagonist_role}",
            "",
            "Character Profile:",
            story.character_profile or "",
            "",
            "World Description:",
            story.world_description or "",
            "",
        ]

        for chapter in story.chapters:
            lines.extend(
                [
                    f"Chapter {chapter.number}: {chapter.title}",
                    chapter.content,
                    "",
                ]
            )

        lines.extend(
            [
                "Final Ending:",
                story.final_ending or "",
            ]
        )

        return "\n".join(lines).encode("utf-8")
