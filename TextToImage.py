import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# Set your OpenAI API key (replace with Streamlit Secrets for safety in production)
openai.api_key = "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"

# Streamlit App
st.set_page_config(page_title="AI Image Generator for Kids", page_icon="🖼️")
st.title("🖼️ AI Image Generator for Kids")
st.write("✨ Describe anything you like, and watch AI turn it into a picture!")

# Input Box
prompt = st.text_input("📝 What should AI draw for you?")

# Generate Button
if st.button("✨ Generate Picture"):
    if prompt.strip() != "":
        with st.spinner("Creating your magical picture..."):
            response = openai.Image.create(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="512x512"
            )
            image_url = response["data"][0]["url"]

            # Fetch and Display Image
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption="🎉 Your AI-created picture!")

            # Download Button
            st.download_button(
                label="📥 Download Image",
                data=image_response.content,
                file_name="your_ai_image.png",
                mime="image/png"
            )
    else:
        st.warning("Please describe what you want to see!")

# Footer
st.caption("Made with ❤️ using OpenAI DALL·E and Streamlit")
