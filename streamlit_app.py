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
    st.set_page_config(page_title="TA Center Demo", page_icon=":mortar_board:", layout="wide")

    st.title("TA Center Student Database Demo")
    st.subheader("Version 0.1")

    st.image("university_logo.png", use_column_width=True)
    
    st.write("---")

    # Load data
    data_load_state = st.text("Loading data...")
    data = load_data()
    data_load_state.text("Data loaded successfully!")

    st.write("---")

    st.markdown("""
                    ### How do I use this Demo?
                
                    NOTE: all data in this application is fake and serves only for demonstration purposes.

                    - You can search by a name, for example: John and click search. The entire profile will appear.
                    - You can search by the year of education, and the list of all students in that year will show.
                    - You can also check out interesting visualizations for demo purposes.
                """)
    
    st.write("---")
    st.subheader("SEARCH THE DATABASE")
    with st.expander("Search Options"):
        search_option = st.selectbox("Choose search option:", ("Search by Name", "Search by City", "Search by Education Year"))
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
    st.subheader("SHOW ME INTERESTING VISUALIZATIONS!")
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
