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
def load_tax_data():
    file_path = 'industriesplit_input.xlsx'
    data = pd.read_excel(file_path, sheet_name='Daten_Tax')
    return data
df = load_tax_data()
filtered_df = pd.DataFrame()
st.title("Steuerausfälle in Deutschland quantifiziert")

with st.container():
    col1, col2 = st.columns((3, 1))
    
    with col2:
        st.subheader("Einstellungen für die Steuerdiagramme")
       
        selected_tax = st.selectbox(
            'Wähle hier die Steuerkategorie aus:',
            options=df.columns[1:]  # Ignoriere die erste Spalte (Jahr)
        )

        start_year, end_year = st.select_slider(
            'Wähle einen Zeitraum aus:',
            options=df['Year'].unique(),
            value=(2023, 2040)
        )

        filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

        if st.checkbox('Zeige die Gesamtsumme für die ausgewählte Steuerkategorie'):
            if selected_tax in filtered_df.columns:
                total_tax = round((filtered_df[selected_tax].sum() / 1000), 1)
                st.write(f"Im Zeitraum von {start_year} bis {end_year} entgehen Deutschland Steuern in der Höhe von {total_tax} Milliarden Euro in dieser Kategorie.")

    with col1:
        if not filtered_df.empty and selected_tax in filtered_df.columns:
            # Teile die Werte durch 1000, um sie in Milliarden umzurechnen
            filtered_df['Milliarden'] = filtered_df[selected_tax] / 1000
    
            fig, ax = plt.subplots()
            ax.bar(filtered_df['Year'], filtered_df['Milliarden'], color='#CCCCFF')
            
            ax.set_ylabel(f'Ermittelte {selected_tax} (in Milliarden €)', fontsize=12)
            ax.set_facecolor('azure')
            fig.patch.set_facecolor('#A7C7E7')
    
            ax.set_xticks(filtered_df['Year'])
            ax.set_xticklabels(filtered_df['Year'].astype(int), rotation=45)
            ax.tick_params(axis='y', labelsize=10)
    
            ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
            plt.tight_layout()
            
            st.title('Dem deutschen Fiskus bleiben Milliarden an Steuern verwehrt')
            
            st.pyplot(fig)
            
            
            # Berechnung der Gesamtsummen für jede Methode
            total_methode_1 = filtered_df.filter(like='Methode 1').sum().sum() / 1000  # In Milliarden
            total_methode_2 = filtered_df.filter(like='Methode 2').sum().sum() / 1000  # In Milliarden


            # Gesamtsumme anzeigen
            st.write(f"Gesamtsumme der fehlenden Steuern nach Methode 1: {total_methode_1} Milliarden Euro.")
            st.write(f"Gesamtsumme der fehlenden Steuern nach Methode 2: {total_methode_2} Milliarden Euro.")
            
            
            
            
            
            
            
            
            st.title('BIP-Lücke nähert sich bis 2040 einer Billion')
            # Anpassung für die Berechnung des Durchschnitts
            def calculate_average(df, year, category):
                methode_1 = df.loc[df['Year'] == year, f'{category} (Methode 1)'].values[0]
                methode_2 = df.loc[df['Year'] == year, f'{category} (Methode 2)'].values[0]
                return (methode_1 + methode_2) / 2 / 1000  # Durchschnitt in Milliarden

            # Erstellung des gestapelten Balkendiagramms mit Durchschnittswerten
            fig, ax = plt.subplots()
            categories = ['Lohnsteuer', 'Gewinnsteuer', 'Umsatzsteuer']  # Kategorien anpassen

            # Jahre von 2023 bis 2040
            years = range(2023, 2041)

            for year in years:
                bottom = 0  # Startwert für das Stapeln der Balken
                if year in filtered_df['Year'].unique():
                    for category in categories:
                        average = calculate_average(filtered_df, year, category)
                        ax.bar(year, average, bottom=bottom, label=category if year == 2023 else "", color=['#CCCCFF','#ffcccc','#ccffcc'])
                        bottom += average

            # Setzen der X-Achsen-Ticks und Beschriftungen
            ax.set_xticks(years)
            ax.set_xticklabels(years, rotation=45)

            # Anpassen des Diagrammhintergrunds
            ax.set_facecolor('azure')
            fig.patch.set_facecolor('#A7C7E7')


            # Beschriftungen und Titel
            ax.set_ylabel('Gesamtsteuern (in Milliarden €)')
            ax.set_xlabel('Jahr')
            ax.set_title('Durchschnittliche Gesamtsteuern pro Jahr nach Kategorie')

            plt.tight_layout()
            st.pyplot(fig)





with st.expander("Weitere Informationen"):
    st.write("Universität St. Gallen mit dem Industriepartner Strategy& durchgeführt. Für die Richtigkeit der Daten leisten wir keine Gewähr. Weiterverwendung der Inhalte mit korrekter Zitation gestatt.")

#hide style

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
