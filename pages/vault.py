import streamlit as st
import pandas as pd
from utils.load_scrolls import get_all_scrolls
from utils.ui_components import footer

st.set_page_config(
    page_title="MythMatch | Vault of Legends",
    page_icon="⚽",
    layout="wide"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Imperial+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Oleo+Script&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Bungee+Spice&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


# Custom CSS
st.markdown("""
<style>
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    h1, h2, h3 {font-family: 'Cinzel', serif;}
    .scroll-card {
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 8px;
        padding: 1rem;
        background: rgba(28, 29, 33, 0.8);
        margin-bottom: 1rem;
    }
    .scroll-card:hover {
        background: rgba(28, 29, 33, 0.95);
    }
    .tag {
        display: inline-block;
        padding: 0.2rem 0.5rem;
        margin-right: 0.3rem;
        border-radius: 20px;
        font-size: 0.7rem;
        background: rgba(0, 62, 31, 0.7);
    }
</style>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Page Header
st.title("🏛️ Vault of Legends")
st.markdown("Explore the complete collection of football's mythic moments")

# Filters
st.markdown("### Find Your Legend")
col1, col2, col3 = st.columns(3)

with col1:
    emotion_filter = st.multiselect(
        "By Emotion",
        ["Glory", "Heartbreak", "Redemption", "Miracle", "Legacy"]
    )
    
with col2:
    # Get unique teams from all scrolls
    all_scrolls = get_all_scrolls()
    all_teams = set()
    for scroll in all_scrolls:
        if "teams" in scroll:
            for team in scroll["teams"]:
                all_teams.add(team)
    
    team_filter = st.multiselect(
        "By Team",
        sorted(list(all_teams))
    )
    
with col3:
    year_filter = st.slider(
        "By Year",
        1950, 2025, (1990, 2025)
    )

# Search
search = st.text_input("Search Scrolls", "")

# Convert scrolls to DataFrame for easier filtering
scrolls_df = pd.DataFrame(all_scrolls)

# Apply filters (this would be expanded with actual filtering logic)
# For now, just show all scrolls
filtered_scrolls = all_scrolls

# Sorting options
sort_options = st.radio(
    "Sort by:",
    ["Newest First", "Oldest First", "Most Epic"],
    horizontal=True
)

# Display scrolls in a grid
st.markdown("### The Archives")

# Create rows of 3 scrolls each
for i in range(0, len(filtered_scrolls), 3):
    row_scrolls = filtered_scrolls[i:i+3]
    cols = st.columns(3)
    
    for j, scroll in enumerate(row_scrolls):
        with cols[j]:
            st.markdown(f"""
            <div class="scroll-card">
                <h3>{scroll['title']}</h3>
                <p><small>{scroll['match']}</small></p>
                <p>{scroll['blurb']}</p>
                <div>
                    {' '.join([f'<span class="tag">{tag}</span>' for tag in scroll['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Unroll", key=f"vault_scroll_{i+j}"):
                st.session_state['current_scroll'] = scroll['filename']
                st.experimental_rerun()

# Pagination
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 8px;">
        <button disabled style="background: transparent; border: 1px solid #666; color: #666; 
                                width: 36px; height: 36px; border-radius: 18px;">1</button>
        <button style="background: transparent; border: 1px solid white; color: white; 
                       width: 36px; height: 36px; border-radius: 18px;">2</button>
        <button style="background: transparent; border: 1px solid white; color: white; 
                       width: 36px; height: 36px; border-radius: 18px;">3</button>
    </div>
    """, unsafe_allow_html=True)

# Footer
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
