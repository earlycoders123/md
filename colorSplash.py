import streamlit as st
import os
import google.generativeai as genai

# Set environment variable manually
os.environ["GEMINI_API_KEY"] = "AIzaSyCtDlmvc6hqwVimM60IFMZxOXDMbzJo33Q"

# Load in code
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Streamlit UI
st.title("📖 AI Storybook Creator (Powered by Gemini)")

title = st.text_input("Enter Story Title:")
mood = st.selectbox("Choose Story Mood:", ["Adventure", "Magical", "Funny", "Scary"])

if st.button("✨ Generate Story"):

    # Initialize Gemini Pro model (Official name)
    model = genai.GenerativeModel('gemini-pro')

    # Create prompt
    prompt = f"Write a short {mood.lower()} story for kids titled '{title}'. Make it colorful, simple, and fun."

    # Generate Story
    try:
        response = model.generate_content(prompt)
        story = response.text
        st.subheader("📚 Here is your AI Story:")
        st.write(story)
    except Exception as e:
        st.error("⚠️ AI failed to generate content. Check your API key or quota.")
        st.write(e)
