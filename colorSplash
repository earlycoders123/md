import streamlit as st
import random

st.title("🎨 AI Color Splash App")

colors = st.multiselect("Pick your favorite colors:", ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange'])

if st.button("Splash Colors!"):
    if colors:
        splash = random.choices(colors, k=10)
        st.subheader("💥 Color Splash:")
        st.write(splash)
    else:
        st.warning("Please pick at least one color!")
