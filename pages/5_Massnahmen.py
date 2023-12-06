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
set_bg_color("#ffb6c1")

st.title("Effektive Massnahmen zur Bekämpfung")

st.markdown('In Deutschland sieht es besonders brenzlig aus!')

image_file_path = 'heatmap.png'
st.image(image_file_path, caption='Heatmap')

st.title("Welche Massnahmen bieten sich für Deutschland an?")



st.markdown('Mit dem Blick auf andere Länder gerichtet untersuchen wir Massnahmen und Best-Practices, die sich Deutschland zu Herzen nehmen könnte.')

st.markdown('Folgende Best-Practices sind besonders interessant:')


# Schweden
with st.container():
    st.write('**Best Practice Schweden**')
    st.write('Förderung der Vollzeitbeschäftigung von Frauen durch verbesserte Kinderbetreuungseinrichtungen.')
    if st.checkbox('Mehr Infos 🇸🇪'):
        pdf_file_path = 'sweden.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Schweden", data=PDFbyte, file_name="sweden.pdf", mime='application/octet-stream')


# Schweiz
with st.container():
    st.write('**Best Practice Schweiz**')
    st.write('Behebung des Fachkräftemangels durch verstärkte Erwachsenenbildung. Außerdem soll eine integrativere Arbeitskultur durch bessere Bildung für Menschen mit Behinderungen und eine gezieltere Ausgleichsabgabe erreicht werden.')
    if st.checkbox('Mehr Infos 🇨🇭'):
        pdf_file_path = 'switzerland.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Schweiz", data=PDFbyte, file_name="switzerland.pdf", mime='application/octet-stream')

# USA
with st.container():
    st.write('**Best Practice USA**')
    st.write('Erleichterung der Integration ehemaliger Straftäter in den Arbeitsmarkt durch steuerliche Anreize.')
    if st.checkbox('Mehr Infos 🇺🇸'):
        pdf_file_path = 'usa.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="USA", data=PDFbyte, file_name="usa.pdf", mime='application/octet-stream')

# Kanada
with st.container():
    st.write('**Best Practice Kanada**')
    st.write('Steigerung der Attraktivität Deutschlands durch Förderung einer Willkommenskultur und Vereinfachung bürokratischer Verfahren. Erleichterung der Zuwanderung durch eine verbesserte Chancenkarte, um qualifizierte Fachkräfte effektiv anzuziehen.')
    if st.checkbox('Mehr Infos 🇨🇦'):
        pdf_file_path = 'canada.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Kanada", data=PDFbyte, file_name="canada.pdf", mime='application/octet-stream')

# China
with st.container():
    st.write('**Best Practice China**')
    st.write('Mit finanziellen Anreizen deutsche Arbeitnehmer und Studenten aus dem Ausland zurückholen.')
    if st.checkbox('Mehr Infos 🇨🇳'):
        pdf_file_path = 'china.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="China", data=PDFbyte, file_name="china.pdf", mime='application/octet-stream')

# Japan
with st.container():
    st.write('**Best Practice Japan**')
    st.write('Durchführung von Weiterbildungsinitiativen, um den durch die Automatisierung verursachten Wandel in der Belegschaft wirksam zu bewältigen.')
    if st.checkbox('Mehr Infos 🇯🇵'):
        pdf_file_path = 'japan.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Japan", data=PDFbyte, file_name="japan.pdf", mime='application/octet-stream')

with st.expander("Weitere Informationen"):
    st.write("Disclaimer: Diese Untersuchung wurde im Rahmen des Capstone-Projektes an der Universität St. Gallen mit dem Industriepartner Strategy& durchgeführt. Für die Richtigkeit der Daten leisten wir keine Gewähr. Weiterverwendung der Inhalte mit korrekter Zitation gestattet.")  

#hide style

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

#st.markdown(hide_st_style, unsafe_allow_html=True)
