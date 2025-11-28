import streamlit as st
from streamlit_lottie import st_lottie
import json

# Basic page settings
st.set_page_config(
    page_title="DetectoAI – Deepfake Detection",
    page_icon="🕵🏻‍♂️",
    layout="wide"
)

# Styling
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: 800;
        background: -webkit-linear-gradient(#7f00ff, #e100ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        font-weight: 500;
        color: #6c6c6c;
        text-align: center;
        margin-top: -10px;
    }
    .upload-box {
        padding: 25px;
        border-radius: 18px;
        border: 2px dashed #b266ff;
        background-color: #faf7ff;
        text-align: center;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🎭 DetectoAI — Deepfake Detection Web App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze video using Audio–Gesture Synchronization and Agentic Reasoning</p>',
            unsafe_allow_html=True)

# Lottie animation
# lottie_file = open("app/assets/ai.json")
# lottie_json = json.load(lottie_file)
# st_lottie(lottie_json, height=220)

# Upload section
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_video = st.file_uploader("📤 Upload your MP4 video file", type=["mp4"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_video is not None:
    st.video(uploaded_video)
    st.success("Video Uploaded Successfully! 🎉")

    if st.button("🔍 Start Deepfake Analysis", use_container_width=True):
        with st.spinner("Agentic AI is analyzing the video... 🧠✨"):
            # Temporary placeholder values
            result = "Fake"
            confidence = "78%"
            reason = "Detected mismatch between audio energy peaks and lip motion intensity from timestamps 04s – 11s."

        st.header("📌 Detection Result")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Prediction", value=result)
        with col2:
            st.metric(label="Confidence", value=confidence)

        st.subheader("🧠 Agentic Explanation")
        st.info(reason)

        st.subheader("📊 Synchronization Graph")
        st.line_chart([1, 3, 5, 2, 8, 3, 1])  # placeholder chart

        st.success("Analysis Complete ✨ Feel free to upload another video!")
