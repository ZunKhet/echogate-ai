
from src.infrastructure.ai.fake_story_adapter import FakeStoryAdapter
from src.application.use_cases.story_service import StoryService
import streamlit as st


st.set_page_config(
    page_title="EchoGate",
    page_icon="🌌",
    layout="wide",
)


def initialize_session_state() -> None:
    if "story" not in st.session_state:
        st.session_state.story = None

    if "story_started" not in st.session_state:
        st.session_state.story_started = False


def get_story_service() -> StoryService:
    ai_adapter = FakeStoryAdapter()
    return StoryService(ai_story_port=ai_adapter)


initialize_session_state()

st.title("🌌 EchoGate")
st.caption("Every image echoes a story.")


with st.sidebar:
    st.header("Story Settings")

    genre = st.selectbox(
        "Genre",
        options=[
            "Fantasy",
            "Mystery",
            "Sci-fi",
            "Adventure",
            "Dark Fairytale",
            "Cozy Magical",
        ],
        index=0,
    )

    tone = st.selectbox(
        "Tone",
        options=[
            "Mysterious",
            "Epic",
            "Dreamy",
            "Dark",
            "Hopeful",
            "Emotional",
        ],
        index=0,
    )

    protagonist_role = st.selectbox(
        "Protagonist Role",
        options=[
            "Explorer",
            "Wanderer",
            "Mage",
            "Guardian",
            "Dreamer",
            "Lost Traveler",
        ],
        index=0,
    )

    st.divider()
    st.markdown("**Story Format**")
    st.caption("Interactive 5-chapter adventure")


left_col, right_col = st.columns([1, 1.2])


with left_col:
    st.subheader("Open the Gate")

    uploaded_image = st.file_uploader(
        "Upload an image to begin your story",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_image:
        st.image(
            uploaded_image,
            caption="Your Story Gate",
            use_container_width=True,
        )

    start_button = st.button(
        "✨ Open the Gate",
        type="primary",
        use_container_width=True,
        disabled=uploaded_image is None,
    )


story_service = get_story_service()

if start_button and uploaded_image:
    image_bytes = uploaded_image.getvalue()

    st.session_state.story = story_service.start_story(
        image_bytes=image_bytes,
        genre=genre,
        tone=tone,
        protagonist_role=protagonist_role,
    )
    st.session_state.story_started = True


with right_col:
    st.subheader("Story Preview")

    story = st.session_state.story

    if not st.session_state.story_started:
        st.info(
            "Upload an image, choose your story settings, "
            "and open the gate to begin."
        )

    if story:
        st.success("The gate has opened...")

        latest_chapter = story.chapters[-1]

        st.markdown(
            f"### Chapter {latest_chapter.number}: {latest_chapter.title}")
        st.write(latest_chapter.content)

        if latest_chapter.choices:
            st.markdown("### Which path will you follow?")

            choice_options = {
                choice.text: choice.id for choice in latest_chapter.choices
            }

            selected_choice_text = st.radio(
                "Choose your next action",
                options=list(choice_options.keys()),
                label_visibility="collapsed",
            )

            if st.button(
                "Continue the Story",
                use_container_width=True,
            ):
                selected_choice_id = choice_options[selected_choice_text]

                st.session_state.story = story_service.continue_story(
                    story=story,
                    selected_choice_id=selected_choice_id,
                )

                st.rerun()

        if story.is_complete:
            st.divider()
            st.markdown("## The Echo Falls Silent")

            st.markdown("### Character Profile")
            st.write(story.character_profile)

            st.markdown("### World Description")
            st.write(story.world_description)

            st.markdown("### Final Ending")
            st.write(story.final_ending)


st.divider()

if st.session_state.story:
    story = st.session_state.story
    st.caption(
        f"Selected style: {story.tone} {story.genre} • "
        f"Role: {story.protagonist_role} • "
        "Format: 5-chapter adventure"
    )
else:
    st.caption("Format: 5-chapter adventure")
