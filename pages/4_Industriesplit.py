import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
set_bg_color("#A7C7E7")



st.title("Industriesplit: Welche Branche trifft es wie stark?")

@st.cache_data
def load_data():
    file_path = 'industriesplit_input.xlsx'
    data = pd.read_excel(file_path, sheet_name='Daten_Industrie')
    return data

data = load_data()

# Streamlit Anwendung
st.title('Datenvisualisierung nach Industrie und Jahr')

# ------------------ Teil 1: Pie Chart  ------------------
st.subheader('Anteil der Industrien am Schaden GDP')

# Auswahl des Jahres für das Pie Chart
year_for_pie = st.selectbox('Jahr für Pie Chart auswählen', data['Year'].unique(), key='year_for_pie')

# Daten für das ausgewählte Jahr filtern
data_for_pie = data[data['Year'] == year_for_pie]

# Pie Chart erstellen
fig1, ax1 = plt.subplots()
ax1.pie(data_for_pie['Schaden GDP in Mio.'], labels=data_for_pie['Industry'], autopct='%1.1f%%')
ax1.set_facecolor('azure')  # Setzt den Hintergrund der Achsen auf hellblau
fig1.patch.set_facecolor('#A7C7E7')  # Setzt den Hintergrund des gesamten Plots
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Pie Chart anzeigen
st.pyplot(fig1)

# Tabelle mit allen Zahlen für das ausgewählte Jahr anzeigen
st.subheader(f'Daten für das Jahr {year_for_pie}')
# 'Year' als Index 
data_for_pie.set_index('Year', inplace=True)
st.table(data_for_pie)


# ------------------ Teil 2: Auswahl und Barchart  ------------------
st.subheader('Vergleich von Schaden GDP für ein Jahr und Industrien')

# Auswahl eines Jahres, standardmäßig 2023
selected_year = st.selectbox('Jahr für Vergleich auswählen', data['Year'].unique(), index=list(data['Year'].unique()).index(2023))

# Auswahl aller Industrien, standardmäßig alle ausgewählt
all_industries = data['Industry'].unique()
selected_industries = st.multiselect('Industrien für Vergleich auswählen', all_industries, default=all_industries)

# Daten für das ausgewählte Jahr und die ausgewählten Industrien filtern
comparison_data = data[(data['Year'] == selected_year) & (data['Industry'].isin(selected_industries))]

# Matplotlib Diagramm erstellen
if not comparison_data.empty:
    fig, ax = plt.subplots()
    
    # Erstellen einer Palette von Pastellblautönen
    pastel_blue_colors = plt.cm.Pastel1(np.linspace(0, 1, len(comparison_data)))
    
    ax.bar(comparison_data['Industry'], comparison_data['Schaden GDP in Mio.'], color=pastel_blue_colors)
    ax.set_ylabel('Ermittelte Schadenshöhe (in Millionen €)', fontsize=12)
    #ax.set_facecolor('azure')  # Setzt den Hintergrund der Achsen auf hellblau
    fig.patch.set_facecolor('#A7C7E7')  # Setzt den Hintergrund des gesamten Plots

    ax.set_xticks(comparison_data['Industry'])
    ax.set_xticklabels(comparison_data['Industry'], rotation=90)  # Alle Industrien anzeigen und drehen
    ax.tick_params(axis='y', labelsize=10)

    # Barchart anzeigen
    st.pyplot(fig)

else:
    st.error('Keine Daten für das ausgewählte Jahr und die ausgewählten Industrien gefunden.')
    
    
with st.expander("Weitere Informationen"):
    st.write("Universität St. Gallen mit dem Industriepartner Strategy& durchgeführt. Für die Richtigkeit der Daten leisten wir keine Gewähr. Weiterverwendung der Inhalte mit korrekter Zitation gestatt.")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

#st.markdown(hide_st_style, unsafe_allow_html=True)
