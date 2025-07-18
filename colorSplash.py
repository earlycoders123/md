import streamlit as st
import google.generativeai as genai

# Load API key securely from Streamlit Secrets
genai.configure(api_key=st.secrets["api"]["gemini_key"])

st.title("📖 AI Storybook Creator (Powered by Gemini)")

title = st.text_input("Enter Story Title:")
mood = st.selectbox("Choose Story Mood:", ["Adventure", "Funny", "Scary", "Magical"])

if st.button("✨ Generate Story"):
    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt = f"Write a short {mood.lower()} story for kids titled '{title}'. Make it fun and creative."

    response = model.generate_content(prompt)

    st.subheader("Here is your AI Story:")
    st.write(response.text)
