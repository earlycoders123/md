
# Import
import google.generativeai as genai
import streamlit as st

# Set your Gemini API Key
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")  # Paste actual key

# Use Gemini Pro Model
model = genai.GenerativeModel('gemini-pro')

# Generate Story
user_prompt = st.text_input("Enter your story prompt:")

# When button is clicked
if st.button("Generate Story") and user_prompt:
    # Generate content from Gemini
    response = model.generate_content(user_prompt)

    # Check if response is valid
    if response and hasattr(response, 'text'):
        st.subheader("🎉 AI-Generated Story:")
        st.write(response.text)
    else:
        st.error("❌ AI did not return a story. Please try again.")




