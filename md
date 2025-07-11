# File: mood_agent.py
import streamlit as st

st.title("🧘 Mood Agent")
st.subheader("Tell me how you're feeling, and I'll guide you.")

mood = st.selectbox(
    "How are you feeling right now?",
    ["😊 Happy", "😔 Sad", "😡 Angry", "😴 Tired", "😕 Confused"]
)

if mood == "😊 Happy":
    st.success("That’s awesome! Keep spreading positivity 🌈")
elif mood == "😔 Sad":
    st.warning("It’s okay to feel sad. Try listening to your favorite song 🎵")
elif mood == "😡 Angry":
    st.warning("Take a deep breath. Let’s take a short break 🧘‍♂️")
elif mood == "😴 Tired":
    st.info("Maybe a short nap or a walk can refresh your mind 😴")
elif mood == "😕 Confused":
    st.info("Try writing down your thoughts to bring clarity 📝")
