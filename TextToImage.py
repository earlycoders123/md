import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# Set your OpenAI API key
# It's recommended to store your API key securely, e.g., using environment variables or Streamlit secrets, rather than hardcoding it.
# For example, using Streamlit secrets: st.secrets["openai_api_key"]
# For this example, we'll keep it for direct functionality.
# openai.api_key = "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"

# Initialize the OpenAI client with the API key
client = openai.OpenAI(api_key="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") 

# Streamlit App
st.set_page_config(page_title="Text to Image Generator", page_icon="🖼️")
st.title("🎨 AI Image Generator for Kids")
st.write("Describe your image and get AI-generated artwork!")

# Input Box
prompt = st.text_input("📝 Describe your image:")

# Generate Button
if st.button("🎨 Generate Image"):
    if prompt.strip() != "":
        with st.spinner("Creating your image..."):
            # DALL-E 3 supports specific sizes: "1024x1024", "1024x1792", or "1792x1024".
            # Using 1024x1024 for a square image.
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,  # n=1 is the only supported value for DALL-E 3.
                size="1024x1024"  
            )
            image_url = response.data[0].url  # Access URL via response.data[0].url

            # Fetch and Display Image
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption="Here’s your AI-generated image!")

            # Download Button
            st.download_button("Download Image", image_response.content, "ai_image.png", "image/png")
    else:
        st.warning("Please describe your image!")

# Footer
st.caption("Made with ❤️ using Streamlit & DALL·E")
