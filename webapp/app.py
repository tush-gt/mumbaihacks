import streamlit as st
from streamlit_lottie import st_lottie
import json
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

# =========== Cloudinary Setup ===========
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("CLOUD_API_KEY"),
    api_secret=os.getenv("CLOUD_API_SECRET"),
    secure=True
)

# =========== Streamlit UI Config ===========
st.set_page_config(
    page_title="DetectoAI – Deepfake Detection",
    page_icon="🕵🏻‍♂️",
    layout="wide"
)

# Page Styling
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

# Title Text
st.markdown('<p class="title"> DetectoAI — Deepfake Detection Web App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Analyze video using Audio–Gesture Synchronization and Agentic Reasoning</p>',
            unsafe_allow_html=True)

# ================== Video Upload Section ==================
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_video = st.file_uploader("📤 Upload your MP4 video file", type=["mp4"])
st.markdown('</div>', unsafe_allow_html=True)


if uploaded_video is not None:
    st.video(uploaded_video)
    st.success("🎉 Video Uploaded Successfully!")

    # Save uploaded file temporarily
    temp_video_path = "temp_uploaded_video.mp4"
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())

    # Upload to Cloudinary
    with st.spinner("⏳ Uploading to cloud storage..."):
        upload_result = cloudinary.uploader.upload(
            temp_video_path,
            resource_type="video",
            folder="deepfake_uploads"
        )

    video_url = upload_result.get("secure_url")
    st.success("☁ Uploaded to Cloudinary Successfully!")
    st.write("🔗 **Cloud Video URL:**")
    st.code(video_url)

    # ============ ANALYSIS BUTTON ============
    if st.button("🔍 Start Deepfake Analysis", use_container_width=True):
        with st.spinner("🤖 Agentic AI is analyzing the video..."):

            # ---------------------
            # Backend logic placeholder
            # (Will be replaced once backend is ready)
            # ---------------------
            result = "Fake"
            confidence = "78%"
            reason = "Detected mismatch between audio energy peaks and lip motion intensity from timestamps 04s – 11s."
            chart_data = [1, 4, 2, 7, 3, 6, 1]

        st.header("📌 Detection Result")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Prediction", value=result)
        with col2:
            st.metric(label="Confidence", value=confidence)

        st.subheader("🧠 Agentic Explanation")
        st.info(reason)

        st.subheader("📊 Synchronization Graph")
        st.line_chart(chart_data)

        st.success("✨ Analysis Complete! Upload another video anytime.")
