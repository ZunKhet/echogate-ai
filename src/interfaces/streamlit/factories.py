import streamlit as st

from src.application.use_cases.export_story import ExportStoryUseCase
from src.application.use_cases.story_service import StoryService
from src.infrastructure.ai.fake_story_adapter import FakeStoryAdapter
from src.infrastructure.document.pdf_export_adapter import PDFExportAdapter
from src.infrastructure.persistence.in_memory_story_repository import (
    InMemoryStoryRepository,
)
from src.infrastructure.ai.gemini_story_adapter import GeminiStoryAdapter


def initialize_session_state() -> None:
    if "story_repository" not in st.session_state:
        st.session_state.story_repository = InMemoryStoryRepository()

    if "story" not in st.session_state:
        st.session_state.story = None

    if "story_started" not in st.session_state:
        st.session_state.story_started = False

    if "story_file" not in st.session_state:
        st.session_state.story_file = None

    if "uploaded_image_bytes" not in st.session_state:
        st.session_state.uploaded_image_bytes = None

    if "include_cover_image" not in st.session_state:
        st.session_state.include_cover_image = True

    if "story_mode" not in st.session_state:
        st.session_state.story_mode = "Demo Mode"

    if "gemini_api_key" not in st.session_state:
        st.session_state.gemini_api_key = ""

    if "active_story_mode" not in st.session_state:
        st.session_state.active_story_mode = None

    if "active_gemini_api_key" not in st.session_state:
        st.session_state.active_gemini_api_key = ""


def get_story_service(
    story_mode: str = "Demo Mode",
    gemini_api_key: str | None = None,
) -> StoryService:
    return StoryService(
        ai_story_port=get_ai_story_adapter(
            story_mode=story_mode,
            gemini_api_key=gemini_api_key,
        ),
        story_repository=st.session_state.story_repository,
    )


def get_export_story_use_case() -> ExportStoryUseCase:
    return ExportStoryUseCase(
        story_repository=st.session_state.story_repository,
        document_exporter=PDFExportAdapter(),
    )


def get_ai_story_adapter(
    story_mode: str = "Demo Mode",
    gemini_api_key: str | None = None,
):
    if story_mode == "Demo Mode":
        return FakeStoryAdapter()

    if story_mode == "Gemini AI Mode":
        if not gemini_api_key:
            raise ValueError("Gemini API key is missing.")

        return GeminiStoryAdapter(
            api_key=gemini_api_key,
        )

    raise ValueError(f"Unsupported story mode: {story_mode}")
