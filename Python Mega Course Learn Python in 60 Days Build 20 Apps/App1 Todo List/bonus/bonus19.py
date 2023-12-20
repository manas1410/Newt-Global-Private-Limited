import streamlit as st
from PIL import Image


with st.expander("Start Camera"):
    # Start the Camera
    camera_image = st.camera_input("Camera")

# Create a pillow image instance
if camera_image:
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)