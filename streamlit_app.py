import streamlit as st
import pandas as pd

# Load CSV data
@st.cache
def load_data():
    data = pd.read_csv("test_data.csv")
    return data

# Search by name
def search_by_name(data, name):
    result = data[(data['First Name'] == name) | (data['Last Name'] == name)]
    return result

# Search by city
def search_by_city(data, city):
    result = data[data['City'] == city]
    return result

# Search by supervisor
def search_by_supervisor(data, supervisor):
    # Assuming supervisor information is not included in the CSV file
    st.write("Supervisor information is not available in the dataset.")

# Search by education year
def search_by_education_year(data, year):
    result = data[data['Current Ed Year'] == year]
    return result

# Display profile in bullet points
def display_profile(profile):
    st.write("Profile:")
    for key, value in profile.items():
        st.write(f"- {key}: {value}")

def main():
    st.title("TA Center Student Database")

    # Load data
    data_load_state = st.text("Loading data...")
    data = load_data()
    data_load_state.text("Data loaded successfully!")

    # Sidebar options
    st.sidebar.subheader("Search Options")
    search_option = st.sidebar.selectbox("Choose search option:", ("Search by Name", "Search by City", "Search by Supervisor", "Search by Education Year"))
    if search_option == "Search by Name":
        name = st.sidebar.text_input("Enter name:")
        if st.sidebar.button("Search"):
            result = search_by_name(data, name)
            if not result.empty:
                profile = result.iloc[0].to_dict()
                display_profile(profile)
            else:
                st.write("No results found.")
    elif search_option == "Search by City":
        city = st.sidebar.text_input("Enter city:")
        if st.sidebar.button("Search"):
            result = search_by_city(data, city)
            st.write(result)
    elif search_option == "Search by Supervisor":
        supervisor = st.sidebar.text_input("Enter supervisor:")
        if st.sidebar.button("Search"):
            search_by_supervisor(data, supervisor)
    elif search_option == "Search by Education Year":
        year = st.sidebar.selectbox("Choose education year:", sorted(data['Current Ed Year'].unique()))
        if st.sidebar.button("Search"):
            result = search_by_education_year(data, year)
            st.write(result)

    # Visualization options
    st.sidebar.subheader("Visualization Options")
    visualization = st.sidebar.selectbox("Choose visualization:", ("Gender Balance", "Number of People in Each Year of Study"))
    if st.sidebar.button("Show Visualization"):
        if visualization == "Gender Balance":
            gender_counts = data['Sex'].value_counts()
            st.bar_chart(gender_counts)
        elif visualization == "Number of People in Each Year of Study":
            year_counts = data['Current Ed Year'].value_counts().sort_index()
            st.bar_chart(year_counts)

if __name__ == "__main__":
    main()
