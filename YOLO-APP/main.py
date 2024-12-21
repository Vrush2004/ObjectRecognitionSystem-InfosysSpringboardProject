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