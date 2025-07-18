import streamlit as st
import requests

st.title("📚 AI Storybook Creator")

title = st.text_input("Story Title")
mood = st.selectbox("Pick Story Mood:", ["Adventure", "Funny", "Scary", "Magical"])

if st.button("Generate My Story!"):
    # Step 1: AI Story (GPT2 via Hugging Face)
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_TOKEN"}
    prompt = f"Write a {mood.lower()} story titled '{title}' for kids."

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    story = response.json()[0]['generated_text']
    st.success("Here is your AI Story:")
    st.write(story)

    # Step 2: AI Image (Bing Image Creator)
    image_prompt = f"storybook cover for {title} in {mood.lower()} style"
    st.write("Click below to generate cover image:")
    st.link_button("Generate Cover Image", f"https://www.bing.com/images/create?q={image_prompt.replace(' ','+')}")

