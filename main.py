import streamlit as st
import json
from datetime import datetime
import os
from utils.load_scrolls import get_all_scrolls, load_scroll
from utils.ui_components import hero_section, footer

# Page configuration
st.set_page_config(
    page_title="MythMatch | Football's Eternal Stories",
    page_icon="⚽",
    layout="wide"
)


st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Imperial+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Oleo+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)



st.markdown("""
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
""", unsafe_allow_html=True)



# Hero Section - Cathedral Archway
hero_section()

# Sunday Ritual Section
st.markdown("---")
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("🔮 Sunday Ritual")
    st.markdown("Every Sunday, a new sacred chapter unfolds. Return to witness the next legendary moment transformed into myth.")
    
    # Next ritual countdown
    today = datetime.now()
    next_sunday = today + datetime.timedelta(days=(6-today.weekday()) % 7)
    days_until = (next_sunday - today).days
    
    st.markdown(f"**Next Ritual:** {next_sunday.strftime('%B %d')} • {days_until} days from now")

with col2:
    st.button("Subscribe to Rituals", type="primary")

# Featured Scrolls
st.markdown("---")
st.header("📜 Featured Scrolls")

# Load scrolls from metadata
all_scrolls = get_all_scrolls()
featured_scrolls = [s for s in all_scrolls if s.get("featured", False)]

# Display scrolls in a 2-column grid
col1, col2 = st.columns(2)
columns = [col1, col2]

for i, scroll in enumerate(featured_scrolls):
    with columns[i % 2]:
        with st.container():
            st.markdown(f"""
            <div class="scroll-card">
                <h3>{scroll['title']}</h3>
                <p>{scroll['blurb']}</p>
                <div class="tags">
                    {' '.join([f'<span>{tag}</span>' for tag in scroll['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Unroll Scroll", key=f"scroll_{i}"):
                st.session_state['current_scroll'] = scroll['filename']
                st.experimental_rerun()

# Vault Preview
st.markdown("---")
st.header("🏛️ Vault of Legends")
st.markdown("Explore the complete collection of mythic moments, sorted by emotion, team, or era.")

# Preview of emotion filters
emotions = ["Glory", "Heartbreak", "Redemption", "Miracle", "Legacy"]
cols = st.columns(len(emotions))
for i, emotion in enumerate(emotions):
    with cols[i]:
        st.button(emotion)

st.button("Enter the Full Vault", type="secondary")

# Footer with subtle CTA for Loreforge (Phase 2)
footer()

# Logic to open a scroll when selected
if 'current_scroll' in st.session_state:
    scroll_path = f"scrolls/{st.session_state['current_scroll']}"
    load_scroll(scroll_path)
    # Clear the selection after loading
    st.session_state.pop('current_scroll')

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
