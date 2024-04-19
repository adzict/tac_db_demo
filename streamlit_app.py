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

# Display profile in bullet points
def display_profile(profile):
    st.write("Profile:")
    for key, value in profile.items():
        st.write(f"- {key}: {value}")

def main():
    st.title("Explore Student Data")

    # Load data
    data_load_state = st.text("Loading data...")
    data = load_data()
    data_load_state.text("Data loaded successfully!")

    # Sidebar options
    st.sidebar.subheader("SEARCH")
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
        st.write("This option is currently not available due to the application being a demo version. Thank you for your understanding.")
    elif search_option == "Search by Supervisor":
        st.write("This option is currently not available due to the application being a demo version. Thank you for your understanding.")
    elif search_option == "Search by Education Year":
        year = st.sidebar.selectbox("Choose education year:", sorted(data['Current Ed Year'].unique()))
        if st.sidebar.button("Search"):
            result = data[data['Current Ed Year'] == year]
            st.write(result)

    # Visualization options
    st.sidebar.subheader("Show me interesting visualizations!")
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
