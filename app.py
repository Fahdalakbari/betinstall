from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent

st.set_page_config(
    page_title="BET Surface Area Prediction",
    page_icon=str(HERE / "icon.png"),
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header, menu and footer, and remove page padding,
# so the page looks like a normal website.
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"] {display: none !important;}
      .stApp {background: #0B2A2F;}
      .block-container {padding: 0 !important; max-width: 520px !important;}
      iframe {display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (HERE / "bet_site.html").read_text(encoding="utf-8")
# The page resizes its own frame to fit its content, so the whole site scrolls as one page.
components.html(html, height=1400, scrolling=False)
