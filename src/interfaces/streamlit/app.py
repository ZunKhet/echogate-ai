import streamlit as st

st.set_page_config(
    page_title="EchoGate",
    page_icon="🌌",
    layout="centered",
)

st.title("EchoGate")
st.caption("Every image echoes a story.")

uploaded_image = st.file_uploader(
    "Open the Gate",
    type=["jpg", "jpeg", "png"],
)

if uploaded_image:
    st.image(uploaded_image, caption="Your Story Gate", use_container_width=True)