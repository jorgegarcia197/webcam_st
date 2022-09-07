from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import av
import cv2
import streamlit as st


class VideoProcessor:
    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")

        return av.VideoFrame.from_ndarray(frm, format="bgr24")


st.title("My first Streamlit app")
st.mardown("# HSV Calibration")


class VideoProcessor:
    def __init__(self) -> None:
        self.uh = 255
        self.us = 255
        self.uv = 255
        self.lh = 0
        self.ls = 0
        self.lv = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.cvtColor(
            cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_BGR2HSV
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


ctx = webrtc_streamer(
    key="key",
    video_processor_factory=VideoProcessor,
    rtc_configuration=RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
    ),
)
if ctx.video_processor:
    ctx.video_processor.uh = st.slider(
        "Upper Hue", min_value=0, max_value=255, step=1, value=100
    )
    ctx.video_processor.lh = st.slider(
        "Lower Hue", min_value=0, max_value=255, step=1, value=100
    )
    ctx.video_processor.us = st.slider(
        "Upper Saturation", min_value=0, max_value=255, step=1, value=200
    )
    ctx.video_processor.ls = st.slider(
        "Lower Saturation", min_value=0, max_value=255, step=1, value=200
    )
    ctx.video_processor.uv = st.slider(
        "Upper Value", min_value=0, max_value=255, step=1, value=200
    )
    ctx.video_processor.lv = st.slider(
        "Lower Value", min_value=0, max_value=255, step=1, value=200
    )
