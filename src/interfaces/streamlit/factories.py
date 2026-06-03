import streamlit as st

from src.application.use_cases.export_story import ExportStoryUseCase
from src.application.use_cases.story_service import StoryService
from src.infrastructure.ai.fake_story_adapter import FakeStoryAdapter
from src.infrastructure.document.pdf_export_adapter import PDFExportAdapter
from src.infrastructure.persistence.in_memory_story_repository import (
    InMemoryStoryRepository,
)


def initialize_session_state() -> None:
    if "story_repository" not in st.session_state:
        st.session_state.story_repository = InMemoryStoryRepository()

    if "story" not in st.session_state:
        st.session_state.story = None

    if "story_started" not in st.session_state:
        st.session_state.story_started = False

    if "story_file" not in st.session_state:
        st.session_state.story_file = None


def get_story_service() -> StoryService:
    return StoryService(
        ai_story_port=FakeStoryAdapter(),
        story_repository=st.session_state.story_repository,
    )


def get_export_story_use_case() -> ExportStoryUseCase:
    return ExportStoryUseCase(
        story_repository=st.session_state.story_repository,
        document_exporter=PDFExportAdapter(),
    )
