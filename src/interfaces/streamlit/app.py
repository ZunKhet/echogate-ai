import streamlit as st

from src.interfaces.streamlit.factories import (
    get_export_story_use_case,
    get_story_service,
    initialize_session_state,
)

from src.config.settings import settings


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

    story = st.session_state.story
    story_title = ""

    if story is None:
        story_title = st.text_input(
            "Story Title (Optional)",
            placeholder="Leave empty to let AI decide later",
        )
    else:
        edited_title = st.text_input(
            "Story Title",
            value=story.title,
            key="editable_story_title",
        )

        if edited_title != story.title:
            if st.button("Update Title", use_container_width=True):
                try:
                    story.rename(edited_title)
                    st.session_state.story_repository.save(story)
                    st.session_state.story = story
                    st.session_state.story_file = None
                    st.success("Title updated.")
                    st.rerun()
                except ValueError as error:
                    st.error(str(error))

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
    st.header("Story Status")

    story = st.session_state.story

    if story is None:
        st.caption("No story started yet.")
    else:
        st.caption(f"Title: {story.title}")
        st.caption(f"Progress: {len(story.chapters)} / 5 chapters")

        if story.is_complete:
            st.success("Story complete")
        else:
            st.info("Story in progress")

        if st.button("🆕 Start New Story", use_container_width=True):
            st.session_state.story = None
            st.session_state.story_started = False
            st.session_state.story_file = None
            st.session_state.uploaded_image_bytes = None
            st.rerun()

    st.divider()
    st.header("PDF Settings")

    include_cover_image = st.checkbox(
        "Include uploaded image on cover page",
        value=st.session_state.include_cover_image,
    )
    st.session_state.include_cover_image = include_cover_image

    st.divider()
    st.markdown("**Story Format**")
    st.caption("Interactive 5-chapter adventure")


story_service = get_story_service()

story = st.session_state.story


if story is None:
    st.subheader("Open the Gate")

    uploaded_image = st.file_uploader(
        "Upload an image to begin your story",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_image:
        st.session_state.uploaded_image_bytes = uploaded_image.getvalue()

    if st.session_state.uploaded_image_bytes:
        st.image(
            st.session_state.uploaded_image_bytes,
            caption="Your Story Gate",
            use_container_width=True,
        )

    start_button = st.button(
        "✨ Open the Gate",
        type="primary",
        use_container_width=True,
        disabled=st.session_state.uploaded_image_bytes is None,
    )

    if start_button and st.session_state.uploaded_image_bytes:
        try:
            with st.spinner("Listening to the echo..."):
                st.session_state.story = story_service.start_story(
                    image_bytes=st.session_state.uploaded_image_bytes,
                    genre=genre,
                    tone=tone,
                    protagonist_role=protagonist_role,
                    story_title=story_title,
                )
                st.session_state.story_started = True

            st.rerun()

        except Exception as error:
            st.error(f"Failed to open the gate: {error}")

else:
    image_col, vision_col = st.columns([1, 1.2])

    with image_col:
        st.subheader("Your Story Gate")

        if st.session_state.uploaded_image_bytes:
            st.image(
                st.session_state.uploaded_image_bytes,
                caption="Uploaded image",
                use_container_width=True,
            )

    with vision_col:
        with st.container(border=True):
            st.markdown("### ✨ The Gate's Vision")

            st.markdown(f"**Setting:** {story.image_analysis.setting}")
            st.markdown(f"**Mood:** {story.image_analysis.mood}")

            if story.image_analysis.main_objects:
                st.markdown(
                    "**Key Elements:** "
                    + ", ".join(story.image_analysis.main_objects)
                )

            st.markdown("**First Echo:**")
            st.write(story.image_analysis.story_seed)

            if story.image_analysis.possible_conflict:
                st.markdown("**Hidden Tension:**")
                st.write(story.image_analysis.possible_conflict)

        with st.container(border=True):
            st.markdown("### 📖 Story Details")
            st.markdown(f"**Genre:** {story.genre}")
            st.markdown(f"**Tone:** {story.tone}")
            st.markdown(f"**Protagonist Role:** {story.protagonist_role}")

    st.divider()

    st.markdown(f"# {story.title}")

    progress = len(story.chapters) / 5
    st.progress(progress)
    st.caption(f"Chapter {len(story.chapters)} of 5")

    st.markdown("## 📚 Story So Far")

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
            choice.text: choice.id for choice in latest_chapter.choices}

        selected_choice_text = st.radio(
            "Choose your next action",
            options=list(choice_options.keys()),
            label_visibility="collapsed",
        )

        if st.button("Continue the Story", use_container_width=True):
            selected_choice_id = choice_options[selected_choice_text]
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

if settings.DEBUG_MODE:
    st.divider()

    with st.expander("Developer Debug"):
        st.json(
            {
                "story_id": story.id,
                "title": story.title,
                "genre": story.genre,
                "tone": story.tone,
                "protagonist_role": story.protagonist_role,
                "chapter_count": len(story.chapters),
                "is_complete": story.is_complete,
                "image_analysis": {
                    "setting": story.image_analysis.setting,
                    "mood": story.image_analysis.mood,
                    "main_objects": story.image_analysis.main_objects,
                    "story_seed": story.image_analysis.story_seed,
                    "magical_elements": story.image_analysis.magical_elements,
                    "possible_conflict": story.image_analysis.possible_conflict,
                    "suggested_title": story.image_analysis.suggested_title,
                },
                "chapters": [
                    {
                        "number": chapter.number,
                        "title": chapter.title,
                        "summary": chapter.summary,
                        "selected_choice_id": chapter.selected_choice_id,
                        "choices": [
                            {"id": choice.id, "text": choice.text}
                            for choice in chapter.choices
                        ],
                    }
                    for chapter in story.chapters
                ],
            }
        )
