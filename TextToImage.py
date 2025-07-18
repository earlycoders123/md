# text_to_image_generator.py

import google.generativeai as genai
import streamlit as st
from PIL import Image
import io
import base64

# Set Gemini API Key
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")  # Secure via secrets in production

# Load Gemini Model (Multimodal)
model = genai.GenerativeModel('models/gemini-2.5-pro')  # Correct multimodal model

# Streamlit App
st.set_page_config(page_title="Text to Image Generator", page_icon="🖼️")

st.title("🎨 AI Image Generator for Kids")
st.write("Describe your image and get AI-generated artwork!")

# Input Box
prompt = st.text_input("📝 Describe your image:")

# Button to Generate Image
if st.button("🎨 Generate Image"):
    if prompt.strip() != "":
        with st.spinner("Creating your image..."):
            response = model.generate_content(prompt + ". Generate a simple cartoon-like image.")

            # Extract image bytes from response
            image_data = None
            for part in response.parts:
                if part.mime_type.startswith("image/"):
                    image_data = part.data

            if image_data:
                image = Image.open(io.BytesIO(image_data))
                st.image(image, caption="Here’s your AI-generated image!")

                # Optional: Download button
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                st.download_button(
                    label="Download Image",
                    data=buffered.getvalue(),
                    file_name="ai_image.png",
                    mime="image/png"
                )
            else:
                st.error("No image was generated. Try a simpler prompt.")
    else:
        st.warning("Please describe your image!")

# Footer
st.caption("Made with ❤️ using Streamlit & Gemini AI")
