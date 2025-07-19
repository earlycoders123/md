# text_to_image_app.py

import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# 🎯 Set your OpenAI API key here (for Colab or local)
# Use st.secrets["openai_api_key"] in production on Streamlit Cloud
openai.api_key = "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"

# Streamlit App
st.set_page_config(page_title="AI Picture Maker", page_icon="🎨")
st.title("🎨 AI Picture Maker for Kids")
st.write("Type anything and let AI draw your idea!")

# Get user input
prompt = st.text_input("📝 What should AI draw for you?")

# Generate Image Button
if st.button("✨ Draw Picture"):
    if prompt.strip():
        with st.spinner("Drawing your picture..."):
            # Use DALL·E 3 model
            response = openai.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024"   # High-quality square image
            )
            image_url = response.data[0].url

            # Fetch and show image
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))

            st.image(image, caption="🎉 Here's your AI picture!")

            # Download button
            st.download_button(
                label="📥 Download Image",
                data=image_response.content,
                file_name="ai_picture.png",
                mime="image/png"
            )
    else:
        st.warning("Please describe something!")

st.caption("Made with ❤️ using OpenAI DALL·E and Streamlit")
