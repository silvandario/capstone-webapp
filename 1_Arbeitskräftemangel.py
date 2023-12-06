import streamlit as st
import pandas as pd
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

@st.cache_data
def load_data():
    file_path = 'industriesplit_input.xlsx'
    data = pd.read_excel(file_path, sheet_name='Daten_FKM')
    return data

df = load_data()
filtered_df = pd.DataFrame()


st.title("Arbeitskräftemangel in Deutschland quantifiziert")

st.markdown("""Um der Berücksichtigung verschiedener Einflussfaktoren des Arbeitskräftemangel gerecht zu werden,
            wurden verschiedene Szenarien erstellt. 
            Diese sollen durch die verschiedenen Stufen der Komplexität eine bessere Annäherung an die Realität darstellen. 
            Beachte, dass die Szenarien aufeinander aufbauen. 
            Zur Validierung wird eine weitere Berechnung aufgesetzt, 
            die sich der Lücke zwischen Arbeitsnachfrage und Arbeitsangebot bedient. """)

# Status für das Anzeigen der Beschreibung (anfänglich auf False gesetzt)
if 'show_description' not in st.session_state:
    st.session_state.show_description = False

# Schaltfläche, um die Beschreibung anzuzeigen/zu verbergen
if st.button('Klicke hier, um mehr über die Berechnungen zu erfahren'):
    st.session_state.show_description = not st.session_state.show_description

# Wenn der Status True ist, wird das Dropdown-Menü mit den Beschreibungen gezeigt
if st.session_state.show_description:
    szenario_description = st.selectbox(
        'Wähle ein Methode aus, über die du mehr erfahren möchstest:',
        ['Forecast vs. Demand-Supply-Gap', 'Methode 1 - Szenario 1', 'Methode 1 - Szenario 2', 'Methode 1 - Szenario 3', 'Demand-Supply-Gap', 'Bedeutung von W1, W2 und W3']
    )
    
    descriptions = {
        'Forecast vs. Demand-Supply-Gap': "Zwei verschiedene Modelle wurden zur Berechnung des Arbeitskräftemangels eigens von uns erstellt. Einerseits eine Trendfortschreibung mit verschiedenen Szenarien und andererseits das Gegenüberstellen von Nachfrage und Angebot. Die Methoden können sich dementsprechend gegenseitig validieren und wir haben eine vorzuweisende Bandbreite und keinen Point-Estimate.",
        'Methode 1 - Szenario 1': "Trend-Forecast unter Berücksichtigung von Sesaonality und Trend als Basis.",
        'Methode 1 - Szenario 2': "Die Corona-Pandemie wird als ein einmaliges und sehr einschneidendes Ereignis klassifiziert, welches den Trend stark beeinflusst. Deshalb wird die Corona-Zeit (ab 2019) für die Trendanalyse ignoriert.",
        'Methode 1 - Szenario 3': "Der Trend kann während Zeiten von Corona vernachlässigt werden, jedoch soll das aktuelle Level berücksichtigt werden -wir rechnen also den ermittelten Trend auf die aktuellen Zahlen.",
        'Demand-Supply-Gap': "Die Arbeitsnachfrage wird dem Arbeitsangebot gegenübergestellt und die anfallende Lücke berechnet.",
        'Bedeutung von W1, W2 und W3': "Die zukünftige Bevölkerungszahl wird stark durch den Saldo der Wanderungen - der Differenz zwischen Zuzügen und Fortzügen - beeinflusst. Wir benutzen die drei Wanderungsszenarien W1 (relativ gering), W2 (moderat) und W3 (hoch) des statistischen Bundesamtes, um auch bei dieser Methode eine Range an zukünftigen Szenarien zu erhalten."
        }
    
    st.write(f"Beschreibung für {szenario_description}: {descriptions[szenario_description]}")

with st.container():
    col1, col2 = st.columns((3, 1))
    
    with col2:
        st.subheader("Einstellungen für den Chart der fehlenden Arbeitskräfte")
        st.markdown("Wie viele Arbeitskräfte fehlen?")
        szenario = st.selectbox('Wählen hier ein Szenario für die fehlenden Arbeitskräfte aus:', ['Methode 1 - Szenario 1',
                                                                                               'Methode 1 - Szenario 2', 
                                                                                               'Methode 1 - Szenario 3',
                                                                                               'Methode 2 (W1)',
                                                                                               'Methode 2 (W2)',
                                                                                               'Methode 2 (W3)',
                                                                                               'Methode 2 (ohne W)',
                                                                                               'Methode 2 (W1, konstante Nachfrage)',
                                                                                               'Methode 2 (W2, konstante Nachfrage)',
                                                                                               'Methode 2 (W3, konstante Nachfrage)'
                                                                                               ]
                                )
        # Zeitraum-Selektor
        years = st.slider('Wähle den Zeitraum aus:', 2023, 2040, (2023, 2040))
      
        # Daten basierend auf dem Zeitraum und Szenario filtern
        filtered_df = df[(df['Year'] >= years[0]) & (df['Year'] <= years[1])]
        
        if st.checkbox('Zeig mir die Differenz der fehlenden Arbeitskräfte'):
            # Berechnen der Differenz der fehlenden Arbeitskräfte zwischen Anfangs- und Endjahr
            start_year_gap = filtered_df[filtered_df['Year'] == years[0]][szenario].values[0]
            end_year_gap = filtered_df[filtered_df['Year'] == years[1]][szenario].values[0]
            total_gap_diff = (end_year_gap - start_year_gap)
            # Überprüfen, ob die Differenz positiv oder negativ ist, um eine angemessene Meldung anzuzeigen
            if total_gap_diff >= 0:
                st.write(f"Zwischen den Jahren {years[0]} und {years[1]} entsteht eine zusätzliche Arbeitskräftelücke von {total_gap_diff} Tausend Personen")
            else:
                st.write(f"Zwischen den Jahren {years[0]} und {years[1]} verringert sich die Arbeitskräftelücke um {-total_gap_diff} Tausend Personen")
        
    with col1:
        st.title('Arbeitskräftelücke Szenario-Analyse')
        if not filtered_df.empty:
            fig, ax = plt.subplots()
            ax.bar(filtered_df['Year'], filtered_df[szenario], color='#CCCCFF')
            ax.set_xticks(filtered_df['Year'])
            ax.set_xticklabels(filtered_df['Year'], rotation=45)
            ax.set_ylabel('Fehlende Facharbeitskräfte (in Tausend)')
            ax.set_facecolor('azure')
            fig.patch.set_facecolor('#A7C7E7')
            plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
            plt.tight_layout()
            st.pyplot(fig)

        if st.checkbox('Zeige mir die Daten für die ausgewählten Jahre'):
            st.write("Tabelle der fehlenden Arbeitskräfteß:")
            year_df = filtered_df
            year_df = year_df.set_index('Year')

            st.dataframe(year_df)


# Custom CSS 
st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: white;
        color: black; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: white;
        color: black; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
    )

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
