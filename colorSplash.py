# story_generator.py

import google.generativeai as genai
import streamlit as st

# Set Gemini API Key (Replace with your real key)
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")

# Load Gemini Model
model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')

# Streamlit App
st.set_page_config(page_title="Text to Story Generator", page_icon="📖")

st.title("📖 AI Story Generator for Kids")
st.write("Enter your idea and get a magical story!")

# Input Box
prompt = st.text_input("📝 Enter your story idea:")

# Button to Generate Story
if st.button("✨ Generate Story"):
    if prompt.strip() != "":
        with st.spinner("Writing your magical story..."):
            response = model.generate_content(prompt + " Create a fun and simple children's story.")
            story = response.text
            st.success("Here's your story!")
            st.write(story)
    else:
        st.warning("Please enter something to get a story!")

# Footer
st.caption("Made with ❤️ using Streamlit & Gemini AI")
