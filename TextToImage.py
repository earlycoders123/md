import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# Create OpenAI client
client = openai.OpenAI(api_key=st.secrets["openai_api_key"])  # Secure key from Streamlit secrets

# Streamlit App
st.title("🎨 AI Picture Generator")

prompt = st.text_input("What should AI draw?")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("AI is drawing..."):
            response = client.images.generate(
            model="dall-e-2",   # Use dall-e-2 instead of dall-e-3
            prompt=prompt,
            size="512x512",     # Smaller size reduces cost
            n=1
)
            image_url = response.data[0].url

            # Fetch and Display Image
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption="🎉 Your AI-generated image!")

            st.download_button("Download Image", image_response.content, "AI_Image.png", "image/png")
