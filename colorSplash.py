import streamlit as st
import requests

# Load your Gemini API key from Streamlit Secrets
API_KEY = st.secrets["api"]["gemini_key"]

st.title("📚 AI Storybook Creator (Powered by Gemini Pro)")

title = st.text_input("Enter Story Title:")
mood = st.selectbox("Choose Story Mood:", ["Adventure", "Funny", "Scary", "Magical"])

if st.button("✨ Generate My Story!"):
    with st.spinner("Generating your story using Gemini Pro..."):

        prompt = f"Write a {mood.lower()} story for kids with the title '{title}'. Keep it simple, short, and fun."

        # ✅ Correct Gemini Pro API Endpoint
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        # API Call
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()

        try:
            # ✅ Extract generated text properly
            story = result['candidates'][0]['content']['parts'][0]['text']
            st.success("🎉 Your AI Story is ready!")
            st.write(story)
        except Exception as e:
            st.error("❌ AI failed to generate a story. Check API key or quotas.")
            st.write(result)
