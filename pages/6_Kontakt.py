import streamlit as st

def set_bg_color(hex_color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {hex_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background color to light pink (#ffb6c1)
set_bg_color("white")

st.title("Kontakt")

st.markdown('Bei Anregungen oder Fragen: Schreibe uns gerne auf LinkedIn! Wir freuen uns auf spannende Gespräche.')

image_file_path = 'lucas.png'
st.image(image_file_path, caption='Schreibe Lucas auf LinkedIn')

image_file_path = 'yanis.png'
st.image(image_file_path, caption='Schreibe Yanis auf LinkedIn')

image_file_path = 'silvan.png'
st.image(image_file_path, caption='Schreibe Silvan auf LinkedIn')

with st.expander("Weitere Informationen"):
    st.write("Capstoneprojekt HSG - Siehe Excel für Berechnungen und Quellen")  

#hide style

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

#st.markdown(hide_st_style, unsafe_allow_html=True)
