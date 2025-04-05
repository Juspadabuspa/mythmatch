import streamlit as st

def hero_section():
    """Display the hero section (Cathedral Archway)"""
    st.markdown(
        """
        <div style="text-align: center; padding: 6rem 1rem; 
                    background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1577223625816-7546f13df25d'); 
                    background-size: cover; background-position: center; color: white;">
            <h1 style="font-size: 3.5rem; font-weight: bold; margin-bottom: 1.5rem; 
                       font-family: 'Cinzel', serif;">MythMatch</h1>
            <h2 style="font-size: 2rem; margin-bottom: 2rem; font-weight: normal; 
                      font-family: 'Cinzel', serif;">Not all matches end. Some echo forever.</h2>
            <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto 2rem auto; 
                      line-height: 1.7;">
                Football moments transformed into myth. Where legendary matches become poetic scrolls.
                Stories crafted for the lorekeepers and believers in beautiful memory.
            </p>
            <div>
                <button style="background-color: #003E1F; color: white; border: none; 
                               padding: 10px 24px; border-radius: 4px; font-size: 16px; 
                               margin-right: 12px; cursor: pointer;">
                    Enter the Vault
                </button>
                <button style="background-color: transparent; color: white; 
                               border: 1px solid white; padding: 10px 24px; 
                               border-radius: 4px; font-size: 16px; cursor: pointer;">
                    Latest Scroll
                </button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def footer():
    """Display the footer with branding and subtle CTAs"""
    st.markdown("---")
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("### MythMatch")
        st.markdown("Where football becomes legend")
        
    with cols[1]:
        st.markdown("### Join the Ritual")
        st.markdown("New scrolls every Sunday")
        st.button("Subscribe")
        
    with cols[2]:
        st.markdown("### Have a Story?")
        st.markdown("The Loreforge awaits your tales")
        st.button("Submit a Legend")
        
    st.markdown("<div style='text-align: center; margin-top: 3rem; opacity: 0.7;'>© 2025 MythMatch | For those who remember</div>", unsafe_allow_html=True)