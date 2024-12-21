import torch
from PIL import Image
import cv2
import time
import numpy as np
import tempfile
import streamlit as st
import base64

# Set page config for the futuristic theme
st.set_page_config(
    page_title="Object Detection System",
    page_icon="🤖",
    layout="wide"
)
# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set background image
def set_background_image(image_path):
    img_base64 = image_to_base64(image_path)
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url('data:image/jpg;base64,{img_base64}');
                background-size: cover;
                background-position: center;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the path to your background image
background_image_path = "./bg3.jpg"

# Apply the background image
set_background_image(background_image_path)

# Custom CSS for futuristic theme and to control video size
st.markdown(
    """
    <style>
        body {
            margin: 0px;
            padding: 0px;
            background-color: #121212;  
            color: white;
            font-family: 'Roboto', sans-serif;
        }
        .main-title {
            font-size: 3rem;  
            text-align: center;
            color: #00f5d4;
            font-weight: bold;
        }
        .st-emotion-cache-1mw54nq h1{
            color: #00f5d4;
            text-align: center;
            font-size: 28px;
            margin-bottom: 15px
        }
        h1#object-detection-system.main-title{
            color: #00f5d4;
        }
        .stApp p{
            text-align: center;
            color: white;
        }
        .custom-text {
            font-size: 20px;
            text-align: center;
            color: white;
        }
        .stButton > button {
            background-color: #00f5d4;
            color: black;
            font-size: 18px;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #00b8a9;
        }
        .stImage, .stVideo, .stWebcam {
            width: 80%;  /* Set the width */
            height: 80%;  /* Maintain aspect ratio */
        }
        .st-emotion-cache-1ibsh2c{
            padding: 30px
        }
        .st-emotion-cache-12fmjuu {
            display: none;
        }
        [data-testid="stSidebar"] {
            background-color: #000046;  
        }
        .stFileUploader {
            background-color: #000056;  /* Replace with your desired color */
            padding: 10px;
            border-radius: 5px;
            border: 1px dashed #00f5d4;
        }
        .st-emotion-cache-taue2i {
            background-color: #000069;
            color: #e6e6e6;
            font-size: 15px;
        }
        .st-emotion-cache-1aehpvj {
            color: rgba(204, 204, 204, 0.7);
            font-size: 14px;
        }
        .st-emotion-cache-zaw6nw {
            color: #00004d;
            background-color: #00f5d4;
            border: 1px solid rgba(49, 51, 63, 0.2);
        }
        .center-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
         .center-button button {
            color:  #00004d;
        }
        .st-emotion-cache-1v45yng .es2srfl9 {
            width: 100%;
            color: #e6e6e6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the pretrained YOLOv5 model
@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5m')

model = load_model()

# Function to process frames
def process_frame(frame):
    # Convert frame (numpy array) to PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Perform YOLOv5 inference
    results = model(image)

    # Render the results on the frame
    results.render()
    processed_frame = results.ims[0]  # Annotated frame
    processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR)  # Convert back to BGR

    return processed_frame