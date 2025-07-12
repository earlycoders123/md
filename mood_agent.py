import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load Gemini API Key from .env
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyCtDlmvc6hqwVimM60IFMZxOXDMbzJo33Q"))

st.set_page_config(page_title="Kids AI Agent Builder", layout="centered")
st.title("🤖 Kids AI Agent Builder")

# Sidebar to select agent
agent = st.sidebar.selectbox("Choose an AI Agent", [
    "Hello Agent",
    "Mood Bot",
    "Pizza Order Bot",
    "Cab Booking Agent",
    "Homework Helper",
    "Smart Chat Agent (Gemini-Pro)"
])

if agent == "Hello Agent":
    st.header("👋 Hello Agent")
    name = st.text_input("What's your name?")
    if st.button("Say Hello"):
        if name:
            st.success(f"Hello, {name}! 🎉")
        else:
            st.warning("Please enter your name to say hello.")

elif agent == "Mood Bot":
    st.header("😊 Mood Bot")
    mood = st.selectbox("How do you feel?", ["Happy", "Sad", "Angry", "Tired", "Excited"])
    if st.button("How to cheer up"):
        replies = {
            "Happy": "That's great! Keep smiling 😊",
            "Sad": "Here's a hug 🤗 and a favorite song could help.",
            "Angry": "Take a deep breath... in, out... 🧘",
            "Tired": "Maybe a quick walk or a nap would help 😴",
            "Excited": "Woohoo! Let's celebrate your energy! 🎉"
        }
        st.info(replies.get(mood))

elif agent == "Pizza Order Bot":
    st.header("🍕 Pizza Order Bot")
    pizza = st.selectbox("Choose pizza:", ["Cheese", "Pepperoni", "Veggie", "BBQ Chicken"])
    size = st.radio("Size:", ["Small", "Medium", "Large"])
    toppings = st.multiselect("Extra toppings:", ["Extra cheese", "Olives", "Mushrooms", "Peppers"])
    if st.button("Place Order"):
        extras = ", ".join(toppings) if toppings else "no extra toppings"
        st.success(f"Order: {size} {pizza} pizza with {extras}. Enjoy! 😋")

elif agent == "Cab Booking Agent":
    st.header("🚗 Cab Booking Agent")
    pickup = st.text_input("Pickup location:")
    dropoff = st.text_input("Destination:")
    time = st.time_input("Pickup time:")
    if st.button("Book Cab"):
        if pickup and dropoff:
            st.success(f"Cab booked from **{pickup}** to **{dropoff}** at **{time}**!")
        else:
            st.error("Please fill in both pickup and destination.")

elif agent == "Homework Helper":
    st.header("📚 Homework Helper")
    subject = st.selectbox("Subject:", ["Math", "Science", "History", "English"])
    question = st.text_area("Type your question here:")
    if st.button("Get Help"):
        if question:
            st.info(f"Here's a hint for your **{subject}** question:\n\n> Think about what you already know about this topic!")
        else:
            st.warning("Please type your question so I can help.")

elif agent == "Smart Chat Agent (Gemini-Pro)":
    st.header("🧠 Smart Chat Agent powered by Gemini-Pro")
    user_input = st.text_input("Ask me anything:")

    if user_input:
        with st.spinner("Thinking..."):
            try:
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content(
                    f"You are a friendly assistant for kids. Answer this: {user_input}"
                )
                st.success(response.text)
            except Exception as e:
                st.error(f"Error from Gemini API: {e}")
