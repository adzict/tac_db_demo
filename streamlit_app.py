import streamlit as st
import pandas as pd

# Load CSV data
@st.cache
def load_data():
    data = pd.read_csv("test_data.csv")
    return data

# Search by name
def search_by_name(data, name):
    # Convert input name to title case
    name = name.title()
    result = data[(data['First Name'] == name) | (data['Last Name'] == name)]
    return result

# Search by city
def search_by_city(data, city):
    result = data[data['City'] == city]
    return result

# Display profile in bullet points
def display_profile(profile):
    st.write("Profile:")
    for key, value in profile.items():
        st.write(f"- {key}: {value}")

def main():
    st.set_page_config(page_title="TA Centar Demo", page_icon=":mortar_board:", layout="wide")

    st.title("TA Centar Baza Podataka Studenata Demo")
    st.subheader("Verzija 0.1")

    st.write("---")

    # Load data
    data_load_state = st.text("Loading data...")
    data = load_data()
    data_load_state.text("Uspešno očitani podaci!")

    st.write("---")

    st.markdown("""
                    ### Šta je ovaj Demo?
                
                    Ovaj Demo je namenjen za TA Centar kao pokazna aplikacija o mogućnostima manipulisanja podacima na optimalniji način.
                    Ovo je prva pokazna verzija aplikacije, koja za cilj ima demonstraciju dostupnih opcija. Lista opcija je u ovom momentu neograničena i zavisi od iskustva korisnika.

                    ### Odakle podaci?
                
                    Podaci koje ovaj Demo koristi nisu stvarni, i svako podudaranje sa stvarnošću je slučajno. Modul korišćen za kreiranje dummy podataka je Faker, i s obzirom na njegove limite u pogledu zemalja koje obuhvata, ova aplikacija sadrži podatke koji su medijalno karaktera Sjedinjenih Američkih Država. Većina podataka je stvorena koristeći sintagme i veštačku inteligenciju.

                    ### Kako se koristi ovaj Demo?
                
                    Demo trenutno raspolaže sa dve opcije: Pretraga baze i Prikaz zanimljivih grafikona.

                    #### Pretraga baze
                    - omogućena je pretraga po imenu, odnosno prezimenu (ne i zajedno). Zbog prirode podataka preporučujem da koristite neka česta američka imena, kao što su: John, Jennifer, Spears, William, David, Kim, Brenda...
                    - nije neophodno koristiti velika slova, program je podešen da očita šta god upišete dok god se poklapa sa podatkom iz baze.
                    - moguća je pretraga po godini edukacije, gde je dovoljno samo da izaberete godinu i prikazaće vam se kompletan spisak studenata.
                    - možete da uvećate spisak sa ikonicom kvadrata u gornje desnom uglu.
                    - nakon što ukucate ime ili izaberete godinu, kliknite Search.
                    - napomena: neka polja su još uvek na engleskom.
                    
                    #### Prikaz zanimljivih vizualizacija
                    - za sada postoje dve opcije: pol i broj studenata po godinama. Grafički prikazi su mogući u svim oblicima, ovo su prikazi radi demonstracije.
                """)
    
    st.write("---")
    st.subheader("Pretraži bazu:")

    with st.expander("Opcije pretrage:"):
        search_option = st.selectbox("Izaberite opciju:", ("Search by Name", "Search by City", "Search by Education Year"))
        if search_option == "Search by Name":
            name = st.text_input("Enter name:")
            if st.button("Search"):
                result = search_by_name(data, name)
                if not result.empty:
                    profile = result.iloc[0].to_dict()
                    display_profile(profile)
                else:
                    st.write("No results found.")
        elif search_option == "Search by City":
            st.write("This option is currently not available due to the application being a demo version. Thank you for your understanding.")
        elif search_option == "Search by Education Year":
            year = st.selectbox("Choose education year:", sorted(data['Current Ed Year'].unique()))
            if st.button("Search"):
                result = data[data['Current Ed Year'] == year]
                st.write(result)

    st.write("---")
    st.subheader("Pokaži mi neke zanimljive grafikone!")

    with st.expander("Visualization Options"):
        visualization = st.selectbox("Choose visualization:", ("Gender Balance", "Number of People in Each Year of Study"))
        if st.button("Show Visualization"):
            if visualization == "Gender Balance":
                gender_counts = data['Sex'].value_counts()
                st.bar_chart(gender_counts)
        elif visualization == "Number of People in Each Year of Study":
            year_counts = data['Current Ed Year'].value_counts().sort_index()
            st.bar_chart(year_counts)

if __name__ == "__main__":
    main()
