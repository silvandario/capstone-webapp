import streamlit as st

st.title("Kontakt")

st.markdown('Bei Anregungen oder Fragen: Schreibe uns gerne auf LinkedIn! Wir freuen uns auf spannende Gespräche.')

image_file_path = 'lucas.png'
st.image(image_file_path, caption='Schreibe Lucas auf LinkedIn')

image_file_path = 'yanis.png'
st.image(image_file_path, caption='Schreibe Yanis auf LinkedIn')

image_file_path = 'silvan.png'
st.image(image_file_path, caption='Schreibe Silvan auf LinkedIn')

with st.expander("Weitere Informationen"):
    st.write("Disclaimer: Diese Untersuchung wurde im Rahmen des Capstone-Projektes an der Universität St. Gallen mit dem Industriepartner Strategy& durchgeführt. Für die Richtigkeit der Daten leisten wir keine Gewähr. Weiterverwendung der Inhalte mit korrekter Zitation gestatt.")  

#hide style

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

#st.markdown(hide_st_style, unsafe_allow_html=True)
