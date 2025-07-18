
# Import
import google.generativeai as genai
import streamlit as st

# Set your Gemini API Key
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")  # Paste actual key

# Use Gemini Pro Model
model = genai.GenerativeModel('gemini-2.5-pro')

# Generate Story
user_prompt = st.text_input("Enter your story prompt:")

if st.button("Generate Story"):
    # Use the prompt to generate story
    st.write(response.text)
