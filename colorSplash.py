import streamlit as st
import requests

st.title("📚 AI Storybook Creator")

# Load Hugging Face API token securely from secrets
HF_TOKEN = st.secrets["api"]["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"]

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

title = st.text_input("Story Title")
mood = st.selectbox("Pick Story Mood:", ["Adventure", "Funny", "Scary", "Magical"])

if st.button("Generate My Story!"):
    with st.spinner("⏳ Generating your story..."):
        prompt = f"Write a {mood.lower()} story titled '{title}' for kids."
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        result = response.json()

        # Handle errors or incomplete API responses
        if isinstance(result, list) and 'generated_text' in result[0]:
            story = result[0]['generated_text']
            st.success("Here is your AI Story:")
            st.write(story)
        else:
            st.error("⚠️ Error: AI did not return a story. Please try again or check your API token.")
            st.write(result)  # Display API response for debugging

    # Step 2: Generate Cover Image via Bing (manual step)
    image_prompt = f"storybook cover for {title} in {mood.lower()} style"
    st.write("Click below to generate your cover image:")
    st.link_button("Generate Cover Image", f"https://www.bing.com/images/create?q={image_prompt.replace(' ','+')}")

