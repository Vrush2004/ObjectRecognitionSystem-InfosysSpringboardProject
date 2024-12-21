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