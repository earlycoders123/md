import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# Set your OpenAI API key
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Image Generator for Kids", page_icon="🖼️")
st.title("🖼️ AI Image Generator for Kids")
st.write("✨ Describe anything you like, and watch AI draw it!")

prompt = st.text_input("📝 What should AI draw for you?")

if st.button("✨ Generate Picture"):
    if prompt.strip() != "":
        with st.spinner("Drawing your picture..."):
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url

            # Fetch and Display Image
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption="🎉 Here's your AI-generated image!")

            st.download_button(
                label="📥 Download Image",
                data=image_response.content,
                file_name="ai_image.png",
                mime="image/png"
            )
    else:
        st.warning("Please describe what you want to see!")

st.caption("Made with ❤️ using OpenAI DALL·E 3 and Streamlit")
