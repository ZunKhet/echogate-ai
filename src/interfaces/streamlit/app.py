from src.interfaces.streamlit.factories import (
    get_export_story_use_case,
    get_story_service,
    initialize_session_state,
)
import streamlit as st


st.set_page_config(
    page_title="EchoGate",
    page_icon="🌌",
    layout="wide",
)

initialize_session_state()

st.title("🌌 EchoGate")
st.caption("Every image echoes a story.")


with st.sidebar:
    st.header("Story Settings")

    story_title = st.text_input(
        "Story Title (Optional)",
        placeholder="Leave empty to let AI decide later",
    )

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
    st.header("PDF Settings")

    include_cover_image = st.checkbox(
        "Include uploaded image on cover page",
        value=st.session_state.include_cover_image,
    )

    st.session_state.include_cover_image = include_cover_image

    st.divider()

    if st.button("Start New Story", use_container_width=True):
        st.session_state.story = None
        st.session_state.story_started = False
        st.session_state.story_file = None
        st.session_state.uploaded_image_bytes = None
        st.rerun()

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
        st.session_state.uploaded_image_bytes = uploaded_image.getvalue()
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

    try:
        with st.spinner("Listening to the echo..."):
            st.session_state.story = story_service.start_story(
                image_bytes=image_bytes,
                genre=genre,
                tone=tone,
                protagonist_role=protagonist_role,
                story_title=story_title,
            )
            st.session_state.story_started = True

    except Exception as error:
        st.error(f"Failed to open the gate: {error}")


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
        st.markdown(f"# {story.title}")

        progress = len(story.chapters) / 5
        st.progress(progress)
        st.caption(f"Chapter {len(story.chapters)} of 5")

        st.markdown("## Story So Far")

        for chapter in story.chapters:
            with st.expander(
                f"Chapter {chapter.number}: {chapter.title}",
                expanded=chapter.number == len(story.chapters),
            ):
                st.caption(chapter.summary)
                st.write(chapter.content)

                if chapter.selected_choice_id:
                    selected_choice = next(
                        (
                            choice.text
                            for choice in chapter.choices
                            if choice.id == chapter.selected_choice_id
                        ),
                        None,
                    )

                    if selected_choice:
                        st.markdown(f"**Chosen path:** {selected_choice}")

        latest_chapter = story.get_latest_chapter()

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

                # Clear previously generated PDF
                st.session_state.story_file = None

                try:
                    with st.spinner("The story continues..."):
                        st.session_state.story = story_service.continue_story(
                            story_id=story.id,
                            selected_choice_id=selected_choice_id,
                        )

                    st.rerun()

                except Exception as error:
                    st.error(f"Failed to continue the story: {error}")

        if story.is_complete:
            st.divider()

            st.markdown("## The Echo Falls Silent")

            st.markdown("### Character Profile")
            st.write(story.character_profile)

            st.markdown("### World Description")
            st.write(story.world_description)

            st.markdown("### Final Ending")
            st.write(story.final_ending)

            export_use_case = get_export_story_use_case()

            if st.button("Prepare PDF", use_container_width=True):
                try:
                    with st.spinner("Preparing your storybook..."):
                        st.session_state.story_file = export_use_case.execute(
                            story_id=story.id,
                            cover_image_bytes=st.session_state.uploaded_image_bytes,
                            include_cover_image=st.session_state.include_cover_image,
                        )

                except Exception as error:
                    st.error(f"Failed to prepare PDF: {error}")

            if st.session_state.story_file:
                st.download_button(
                    label="Download Story PDF",
                    data=st.session_state.story_file,
                    file_name="echogate_story.pdf",
                    mime="application/octet-stream",
                    use_container_width=True,
                )


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
