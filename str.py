import cv2
import streamlit as st
from PIL import Image
import numpy as np

# Initialize tool data
tools = [
    {"name": "Tool1", "measurement": "10 cm"},
    {"name": "Tool2", "measurement": "12 cm"},
    {"name": "Tool3", "measurement": "14 cm"},
    {"name": "Tool4", "measurement": "16 cm"},
    {"name": "Tool5", "measurement": "18 cm"},
    {"name": "Tool6", "measurement": "20 cm"},
]

# Function to overlay tool information on video frame
def overlay_tool_info(frame, tools):
    height, width, _ = frame.shape
    for i, tool in enumerate(tools):
        y_offset = 50 + i * 30  # Vertical spacing between tool info
        cv2.putText(
            frame,
            f"{tool['name']} - {tool['measurement']}",
            (10, y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
    return frame


# Streamlit app
def main():
    st.title("Surgical Tool Measurements Viewer")
    st.text("This application displays tool names and measurements in real time with live video.")

    # Access webcam feed
    run_video = st.checkbox("Start Video")
    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)

    while run_video:
        ret, frame = cap.read()
        if not ret:
            st.warning("Unable to access the webcam.")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = overlay_tool_info(frame, tools)
        FRAME_WINDOW.image(frame)

    cap.release()


if __name__ == "__main__":
    main()