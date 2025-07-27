# pencil_sketch_app.py

import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit UI
st.set_page_config(page_title="🖤 Pencil Sketch Maker", layout="centered")
st.title("✏️ Black & White Pencil Sketch Generator")

uploaded_file = st.file_uploader("📸 Upload a photo", type=["jpg", "jpeg", "png"])

# Pencil Sketch Function
def pencil_sketch(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_img = 255 - gray_img
    blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)
    return sketch

# If image uploaded
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_np = np.array(img)
    img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Generate Sketch
    sketch = pencil_sketch(img_cv2)

    # Show Original and Sketch
    st.subheader("🎨 Original vs Sketch")
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, caption="Original", use_column_width=True)
    with col2:
        st.image(sketch, caption="Pencil Sketch", use_column_width=True, channels="GRAY")
