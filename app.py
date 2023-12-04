import streamlit as st
from pages.Fachkräftemangel import app as Fachkräftemangel_app
from pages.Schaden import app as Schaden_app
from pages.Stuerausfälle import app as Stuerausfälle_app
from pages.Industriesplit import app as Industriesplit_app
from pages.Massnahmen import app as Massnahmen_app



st.set_page_config(page_title="Your App Title",
                   page_icon=":bar_chart:",
                   layout="wide")

PAGES = {
    "Fachkräftemangel": Fachkräftemangel_app,
    "Schaden": Schaden_app,
    "Steuerausfälle": Stuerausfälle_app,
    "Industriesplit": Industriesplit_app,
    "Massnahmen": Massnahmen_app
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()