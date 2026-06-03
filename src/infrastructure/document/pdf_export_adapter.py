from fpdf import FPDF

from src.application.ports.document_export_port import DocumentExportPort
from src.domain.entities.story import Story


class PDFExportAdapter(DocumentExportPort):
    def export_story(self, story: Story) -> bytes:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.add_page()
        pdf.set_font("Helvetica", "B", 24)
        pdf.cell(0, 15, story.title, ln=True, align="C")

        pdf.set_font("Helvetica", "", 12)
        pdf.cell(0, 10, f"{story.tone} {story.genre}", ln=True, align="C")
        pdf.cell(
            0, 10, f"Protagonist: {story.protagonist_role}", ln=True, align="C")

        pdf.ln(10)

        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "Character Profile", ln=True)
        pdf.set_font("Helvetica", "", 12)
        pdf.multi_cell(0, 8, story.character_profile or "")

        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "World Description", ln=True)
        pdf.set_font("Helvetica", "", 12)
        pdf.multi_cell(0, 8, story.world_description or "")

        for chapter in story.chapters:
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 18)
            pdf.cell(
                0, 10, f"Chapter {chapter.number}: {chapter.title}", ln=True)

            pdf.ln(5)
            pdf.set_font("Helvetica", "", 12)
            pdf.multi_cell(0, 8, chapter.content)

        pdf.add_page()
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 10, "Final Ending", ln=True)

        pdf.ln(5)
        pdf.set_font("Helvetica", "", 12)
        pdf.multi_cell(0, 8, story.final_ending or "")

        pdf_bytes = pdf.output(dest="S")

        if isinstance(pdf_bytes, str):
            return pdf_bytes.encode("latin-1")

        return bytes(pdf_bytes)
