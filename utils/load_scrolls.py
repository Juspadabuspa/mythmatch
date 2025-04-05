import streamlit as st
import json
import os
import markdown

def get_all_scrolls():
    """Load all scroll metadata from JSON file"""
    try:
        with open("scrolls/metadata.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Sample metadata for initial setup
        return [
            {
                "filename": "drogba_2012.md",
                "title": "The Lion, The Rain, The Redemption",
                "match": "UEFA Champions League Final, 2012",
                "teams": ["Chelsea", "Bayern Munich"],
                "blurb": "In one night, past sins forgiven. In one header, destiny rewritten. In one kick, history made eternal.",
                "tags": ["Chelsea", "2012", "Redemption", "UCL"],
                "featured": True,
                "publish_date": "2025-04-07"
            },
            {
                "filename": "aguero_9320.md",
                "title": "93:20 - The Moment That Bent Time",
                "match": "Premier League Final Day, 2012",
                "teams": ["Manchester City", "QPR"],
                "blurb": "When seconds became eternity, and a single swing of a foot changed the course of a club forever.",
                "tags": ["Man City", "2012", "Glory", "Premier League"],
                "featured": True,
                "publish_date": "2025-04-14"
            }
        ]

def load_scroll(path):
    """Load and display a scroll with enhanced styling"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            
        # Extract filename without path and extension
        filename = os.path.basename(path)
        scroll_data = None
        
        # Find metadata for this scroll
        all_scrolls = get_all_scrolls()
        for scroll in all_scrolls:
            if scroll["filename"] == filename:
                scroll_data = scroll
                break
                
        # Back button and scroll header
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("← Return"):
                st.session_state.pop('current_scroll', None)
                st.experimental_rerun()
        
        # Display the scroll with styling
        st.markdown("""
        <style>
            .scroll-container {
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
                background-image: url('https://img.freepik.com/free-photo/old-paper-texture_1194-5416.jpg');
                background-size: cover;
                background-color: rgba(245, 242, 235, 0.95);
                border-radius: 8px;
                color: #1C1D21;
                font-family: 'Cormorant Garamond', serif;
            }
            .scroll-container h1 {
                font-family: 'Cinzel', serif;
                font-size: 2.5rem;
                color: #111;
                margin-bottom: 1rem;
            }
            .scroll-container blockquote {
                border-left: 3px solid #003E1F;
                padding-left: 1rem;
                font-style: italic;
                margin: 1.5rem 0;
            }
            .mini-legend {
                font-style: italic;
                margin: 2rem 0 1rem 0;
                font-weight: bold;
                border-top: 1px solid rgba(0,0,0,0.2);
                padding-top: 1rem;
            }
            .tags-section {
                margin-top: 1rem;
            }
            .tag {
                display: inline-block;
                padding: 0.2rem 0.6rem;
                margin-right: 0.5rem;
                border-radius: 20px;
                font-size: 0.7rem;
                background: #003E1F;
                color: white;
            }
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Cormorant+Garamond:wght@400;500;700&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="scroll-container">
            {markdown.markdown(content)}
        </div>
        """, unsafe_allow_html=True)
        
        # Add reactions
        st.markdown("---")
        reaction_cols = st.columns(5)
        reactions = ["🔥 Epic", "💔 Heartbreaking", "✨ Magical", "🦁 Heroic", "🏆 Legendary"]
        for i, reaction in enumerate(reactions):
            with reaction_cols[i]:
                st.button(reaction)
                
        # Related scrolls
        if scroll_data and 'tags' in scroll_data:
            st.markdown("### Related Mythic Moments")
            related = [s for s in all_scrolls if s["filename"] != filename and 
                      any(tag in scroll_data["tags"] for tag in s["tags"])][:2]
            
            if related:
                rel_cols = st.columns(len(related))
                for i, rel in enumerate(related):
                    with rel_cols[i]:
                        st.markdown(f"**{rel['title']}**")
                        st.markdown(f"{rel['blurb']}")
                        if st.button("Read This Scroll", key=f"related_{i}"):
                            st.session_state['current_scroll'] = rel['filename']
                            st.experimental_rerun()
        
    except Exception as e:
        st.error(f"Error loading scroll: {e}")
        return None