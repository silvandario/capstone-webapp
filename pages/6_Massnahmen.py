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

st.title("Welche Massnahmen bieten sich für Deutschland an?")

st.markdown('Kurzübersicht')

image_file_path1 = 'overview1.png'
image_file_path2 = 'overview2.png'
st.image(image_file_path1)
st.image(image_file_path2)

st.markdown('Neugierig? Die einzelnen Massnahmen im Detail')
st.markdown('Folgende Massnahmen sollte Deutschland umsetzen:')

# Renteneintrittsalter
with st.container():
    st.write('**Renteneintrittsalter**')
    st.write('Anhebung des tatsächlichen Renteneintrittsalters durch flexible Arbeitsmöglichkeiten, finanzielle Anreize und die Förderung des lebenslangen Lernens')
    if st.checkbox('Mehr Infos zum Renteneintrittsalter'):
        pdf_file_path = 'retirement_age.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Renteneintrittsalter", data=PDFbyte, file_name="retirement_age.pdf", mime='application/octet-stream')

# Arbeitslosigkeit
with st.container():
    st.write('**Stärkung der Langzeitarbeitslosen**')
    st.write('Überbrückung der Arbeitskräftelücke durch finanzielle Unterstützung für Unternehmen')
    if st.checkbox('Mehr Infos zu Langzeitarbeitslosen'):
        pdf_file_path = 'longterm_unemployment.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Langzeitarbeitslosigkeit", data=PDFbyte, file_name="longterm_unemployment.pdf", mime='application/octet-stream')

# sick_days
with st.container():
    st.write('**Krankheitstage**')
    st.write('Eindämmung der steigenden Zahl von Krankheitstagen durch präventive Maßnahmen, um deren Auswirkungen auf das Arbeitsvolumen zu minimieren')
    if st.checkbox('Mehr Infos zu Krankheitstagen'):
        pdf_file_path = 'sick_days.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Krankheitstage", data=PDFbyte, file_name="sick_days.pdf", mime='application/octet-stream')

# Bindung
with st.container():
    st.write('**Bindung**')
    st.write('Bindung von Fachkräften an das Land durch steuerliche Anreize in Form von Ermäßigungen bei den Ausbildungskosten')
    if st.checkbox('Mehr Infos zur Bindung'):
        pdf_file_path = 'training_costs.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Bindung", data=PDFbyte, file_name="training_costs.pdf", mime='application/octet-stream')

# asylsuchende
with st.container():
    st.write('**Asylsuchende**')
    st.write('Verbesserung der Integration von asylsuchenden Arbeitnehmern durch Vereinfachung der Asylverfahren, Vereinheitlichung der Arbeitserlaubnis und proaktive Berufsausbildung')
    if st.checkbox('Mehr Infos zu Asylsuchenden'):
        pdf_file_path = 'asylum_seekers.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Asylsuchende", data=PDFbyte, file_name="asylum_seekers.pdf", mime='application/octet-stream')

# digital
with st.container():
    st.write('**Digitalisierung**')
    st.write('Digitalisierung durch steuerliche Anreize für Unternehmen, die in innovative Technologien und die digitale Ausbildung ihrer Mitarbeiter investieren')
    if st.checkbox('Mehr Infos zu Digitalisierung'):
        pdf_file_path = 'digitalization.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Digitalisierung", data=PDFbyte, file_name="digitalization.pdf", mime='application/octet-stream')

# Flüchtende 
with st.container():
    st.write('**Flüchtende**')
    st.write('Erleichterung des Zugangs zu Arbeit für ukrainische Flüchtlinge durch die Anerkennung von Qualifikationen, Kinderbetreuung, Sprachkurse und eine Verringerung des bürokratischen Aufwands')
    if st.checkbox('Mehr Infos zu Flüchtenden'):
        pdf_file_path = 'ukrainian_refugees.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Flüchtende", data=PDFbyte, file_name="ukrainian_refugees.pdf", mime='application/octet-stream')

# Mütter
with st.container():
    st.write('**Mütter fördern**')
    st.write('Förderung der Rückkehr von Müttern in den Beruf durch flexiblere Arbeitszeiten, veränderte soziale Erwartungen und bessere Kinderbetreuung')
    if st.checkbox('Mehr Infos zu Mütter'):
        pdf_file_path = 'mothers.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Mütter", data=PDFbyte, file_name="mothers.pdf", mime='application/octet-stream')

# apprenticeships.pdf
with st.container():
    st.write('**Lehrlingsausbildung**')
    st.write('Stärkung der Lehrlingsausbildung durch Förderung der Gleichstellung von Männern und Frauen, unternehmerisches Engagement, soziale Anerkennung, Anreize und verbesserte Qualität')
    if st.checkbox('Mehr Infos zur Lehrlingsausbildung'):
        pdf_file_path = 'apprenticeships.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Lehrlingsausbildung", data=PDFbyte, file_name="apprenticeships.pdf", mime='application/octet-stream')

# unattraktiv 
with st.container():
    st.write('**Arbeitslosigkeit unattraktiv machen**')
    st.write('Verschärfung der Sanktionen: Erhöhung des Arbeitsvolumens durch Verschärfung der Bedingungen für den Bezug von Arbeitslosengeld')
    if st.checkbox('Mehr Infos zur unattraktiven Arbeitslosigkeit'):
        pdf_file_path = 'unemployment.pdf'
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Arbeitslosigkeit", data=PDFbyte, file_name="unemployment.pdf", mime='application/octet-stream')


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
