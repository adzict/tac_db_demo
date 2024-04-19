import streamlit as st
import pandas as pd
import seaborn as sns

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

# Visualizations
def visualize(data, visualization):
    if visualization == "Gender Balance":
        gender_counts = data['Sex'].value_counts()
        st.bar_chart(gender_counts)
    elif visualization == "Number of People in Each Year of Study":
        year_counts = data['Current Ed Year'].value_counts().sort_index()
        st.bar_chart(year_counts)
    elif visualization == "Mean and Median Age":
        st.write("Mean age:", data['Date of Birth'].mean())
        st.write("Median age:", data['Date of Birth'].median())
    elif visualization == "Mean and Median Age per Education Year":
        age_per_year = data.groupby('Current Ed Year')['Date of Birth'].agg(['mean', 'median'])
        st.bar_chart(age_per_year)

def main():
    st.title("Explore Student Data")

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
            st.write(result)
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
    visualization = st.sidebar.selectbox("Choose visualization:", ("Gender Balance", "Number of People in Each Year of Study", "Mean and Median Age", "Mean and Median Age per Education Year"))
    visualize(data, visualization)

if __name__ == "__main__":
    main()
