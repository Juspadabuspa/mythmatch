import streamlit as st
import os
from utils.load_scrolls import load_scroll
from utils.ui_components import footer

# Page config
st.set_page_config(
    page_title="MythMatch | Scroll Viewer",
    page_icon="📜",
    layout="wide"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Imperial+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Oleo+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)



# Check for selected scroll
if "current_scroll" not in st.session_state:
    st.warning("No scroll selected. Return to the Vault to begin your legend.")
    if st.button("← Return to Vault"):
        st.switch_page("vault")
    st.stop()

# Load and display scroll
scroll_file = st.session_state["current_scroll"]
scroll_path = os.path.join("scrolls", scroll_file)
load_scroll(scroll_path)

# Optional footer
footer()


st.markdown('''
<style>
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }

    h1.title-scroll {
        font-family: 'Imperial Script', cursive;
        font-size: 3rem;
        color: gold;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    .mini-legend {
        font-family: 'Dancing Script', cursive;
        font-size: 1.2rem;
        color: #cccccc;
        font-style: italic;
        margin-bottom: 1.5rem;
    }

    .scroll-section-label {
        font-family: 'Oleo Script', cursive;
        font-size: 1rem;
        color: #66cc99;
        margin-top: 1rem;
    }

    .scroll-timestamp {
        font-family: 'Bungee Spice', cursive;
        font-size: 1.6rem;
        color: orangered;
        margin-bottom: 1rem;
    }

    .tags span {
        font-family: 'Oleo Script', cursive;
        font-size: 0.85rem;
        padding: 0.25rem 0.5rem;
        border-radius: 12px;
        background-color: rgba(0,62,31,0.6);
        margin-right: 0.4rem;
        display: inline-block;
    }
</style>

<link href="https://fonts.googleapis.com/css2?family=Imperial+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Oleo+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap" rel="stylesheet">
''', unsafe_allow_html=True)
