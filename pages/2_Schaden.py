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
    data = pd.read_excel(file_path, sheet_name='Daten_BIP')
    return data
df = load_data()
filtered_df = pd.DataFrame()

st.title("BIP-Ausfall in Deutschland quantifiziert")

st.markdown("""Durch das Quantifizieren der fehlenden Arbeitskräfte können wir nun auch abschätzen, wie viel weniger Bruttoinlandprodukt Deutschland durch den Mangel verbuchen kann.""")
if 'show_description' not in st.session_state:
    st.session_state.show_description = False
# Schaltfläche, um die Beschreibung anzuzeigen/zu verbergen
if st.button('Gewusst, es gibt noch andere Schäden, die sich kaum quantifizieren lassen?'):
    st.session_state.show_description = not st.session_state.show_description


# Wenn der Status True ist, wird das Dropdown-Menü mit den Beschreibungen gezeigt
if st.session_state.show_description:
    szenario_description = st.selectbox(
        'Wähle eine Schadensart aus, über die du mehr erfahren möchstest:',
        ['Verzögerung von Bauprojekten', 'Verringerung der Fähigkeit zur Innovation', 'Druck auf die Altersvorsorge', 'Überlastung der vorhandenen Arbeitskräfte', 'Kürzung der Staatsausgaben in anderen Bereichen']
    )
    
    descriptions = {
        'Verzögerung von Bauprojekten': "Deutschland ist bekannt für seine nicht enden wollenden Baustellen auf den Autobahnen. Wenn es vermehrt an Arbeitskräften mangelt, können sich staatliche und private Bau- und Infrastrukturprojekte enorm verzögern. Sei es auf Autobahnen oder in Städten. Auch neue, möglicherweise sehr wichtige Projekte müssen unter Umständen bis auf Weiteres verschoben werden.  Das kann die Lebensqualität der Deutschen mindern und zu mehr Unzufriedenheit im Lande führen.",
        'Verringerung der Fähigkeit zur Innovation': "Die Fähigkeit zur Innovation ist entscheidend für den langfristigen Erfolg eines Unternehmens. Makroökonomisch gesehen sind erfolgreiche und innovative Unternehmen der Motor der Wirtschaft einer Region oder eines Landes. Es ist daher von größter Bedeutung, dass Länder wie Deutschland, die bereits von innovativen Industrien leben, in diesem Bereich weiterhin starke Leistungen erbringen. Neben dem wirtschaftlichen Wachstum kann die Gesellschaft eines Landes auch weiterhin von den neuen Verfahren, Produkten, Modellen und Methoden profitieren, die zur Lösung von Problemen und zur Verbesserung des Lebens geschaffen werden.Wenn es weniger Arbeitskräfte gibt als benötigt werden, verringert sich das Potenzial, neue Innovationen hervorzubringen. Außerdem werden die verbleibenden Arbeitnehmer stark unter Druck gesetzt, da sie ihre Arbeit in Unterbesetzung verrichten müssen, was ihnen die Zeit für kreatives und innovatives Denken nimmt. Alles in allem erhöht dies das Risiko, dass deutsche Unternehmen international nicht wettbewerbsfähig sind.",
        'Druck auf die Altersvorsorge': "",
        'Überlastung der vorhandenen Arbeitskräfte': "Aufgrund des allgemeinen Personalmangels in verschiedenen deutschen Sektoren kann es zu einem enormen Druck auf die verbleibenden Arbeitskräfte kommen. Sie müssen den Mangel an Arbeitskräften kompensieren. Dies kann zu einem starken Anstieg des Stresses führen, der sich letztlich in Burnouts und anderen psychischen Erkrankungen äußert. Dies wiederum führt zu einer Belastung des deutschen Gesundheitssystems und der sozialen Sicherungssysteme. Langfristig kann dies auch Auswirkungen auf die Qualität der Arbeit und die Bindung von Talenten in Deutschland haben.",
        'Kürzung der Staatsausgaben in anderen Bereichen': "Insgesamt muss der deutsche Staat sehr viele finanzielle Mittel in die Behebung des Arbeitskräftemangels investieren. Seine Verringerung hat hohe Priorität, da ein positives Ergebnis die Staatseinnahmen erheblich verbessern kann (wie in den obigen Berechnungen gezeigt). Im Umkehrschluss bedeutet dies aber auch, dass weniger staatliche Ausgaben für andere soziale Belange zur Verfügung stehen. Es ist jedoch auch zu beachten, dass fast alle anderen Ausgaben negativ mit dem Arbeitskräftemangel korrelieren (Migration, Bildung usw.).",
    }
    
    st.write(f"Beschreibung für {szenario_description}: {descriptions[szenario_description]}")

numbers = range(2023,2041)
with st.container():
    col1, col2 = st.columns((3, 1))
    
    with col2:
        st.subheader("Einstellungen für den Schadens-Chart")
        st.markdown("Wie viel wirtschaftlicher Schaden entsteht für Deutschland?")
       
        selected_datengrundlage = st.selectbox(
            'Wähle hier die Datengrundlage aus:',
            options=['BIP-Schaden Methode 1', 'BIP-Schaden Methode 2']
        )

        start_year, end_year = st.select_slider(
            'Wähle einen Zeitraum aus:',
            options = numbers,
            value=(2023, 2040)
        )

        filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

        if st.checkbox('Zeige den wirtschaftlichen Schaden für den ausgewählten Zeitraum'):
            if selected_datengrundlage in filtered_df.columns:
                total_damage = int(round((filtered_df[selected_datengrundlage].sum()),-4)/1000)
                st.write(f"Im Zeitraum von {start_year} bis {end_year} entsteht ein wirtschaftlicher Schaden in der Höhe von {total_damage} Milliarden Euro.")

    with col1:
        if not filtered_df.empty and selected_datengrundlage in filtered_df.columns:
        # Teilen Werte durch 1000, um sie in Milliarden umzurechnen
            filtered_df['Milliarden'] = filtered_df[selected_datengrundlage] / 1000
    
            fig, ax = plt.subplots()
            ax.bar(filtered_df['Year'], filtered_df['Milliarden'], color='#CCCCFF')
            
            # Aktualisiere die Y-Achsen-Beschriftung
            ax.set_ylabel('Ermittelte Schadenshöhe (in Milliarden €)', fontsize=12)
            ax.set_facecolor('azure')
            fig.patch.set_facecolor('#A7C7E7')
    
            ax.set_xticks(filtered_df['Year'])
            ax.set_xticklabels(filtered_df['Year'].astype(int), rotation=45)
            ax.tick_params(axis='y', labelsize=10)
    
            ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
            plt.tight_layout()
            st.pyplot(fig)

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