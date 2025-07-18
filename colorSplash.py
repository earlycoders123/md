
# Import
import google.generativeai as genai

# Set your Gemini API Key
genai.configure(api_key="AIzaSyDI5Hr2zxpxm3ZyfCGgO5iTWeAp_eprUaA")  # Paste actual key

# Use Gemini Pro Model
model = genai.GenerativeModel('gemini-2.5-pro')

# Generate Story
prompt = "Write a short, colorful story for kids about a magical cat."

response = model.generate_content(prompt)

# Show the story
print(response.text)
