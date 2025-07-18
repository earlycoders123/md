import streamlit as st
import requests

# Load your Gemini API Key from Streamlit Secrets
API_KEY = st.secrets["api"]["gemini_key"]

st.title("📚 AI Storybook Creator (Powered by Gemini)")

title = st.text_input("Enter Story Title:")
mood = st.selectbox("Choose Story Mood:", ["Adventure", "Funny", "Scary", "Magical"])

if st.button("✨ Generate My Story!"):
    with st.spinner("Generating your story using Gemini..."):

        prompt = f"Write a {mood.lower()} story for kids with the title '{title}'. Keep it fun and creative."

        # Gemini API Endpoint
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

        payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }

        headers = {"Content-Type": "application/json"}

        # API Call
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()

        # Extract and display story
        try:
            story = result['candidates'][0]['content']['parts'][0]['text']
            st.success("Here is your AI Story!")
            st.write(story)
        except Exception as e:
            st.error("❌ Failed to generate story. Check API key or request limits.")
            st.write(result)  # Show full API response for debugging

