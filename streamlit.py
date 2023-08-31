import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import builtins
import os

def load_data():
    pickle_path = "temp_data.pkl"
    if os.path.exists(pickle_path):
        return pd.read_pickle(pickle_path)
    else:
        data = pd.read_csv('HRDataset_v14.csv')
        data.to_pickle(pickle_path)
        return data

data = load_data()

# Function for Data Exploration
def data_exploration():
    st.title("Data Exploration")
    st.write(data.describe())
    st.write(data.isnull().sum())

# Function for In-depth Analysis & Visualization
def in_depth_analysis():
    st.title("In-depth Analysis & Visualization")

    fig, ax = plt.subplots()
    data['Department'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.distplot(data['Performance'], ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    sns.scatterplot(x='Tenure', y='Utilization', hue='Department', data=data, ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Function for Interactive Features in Streamlit
def interactive_features():
    st.title("Interactive Features")

    department = st.sidebar.multiselect('Select Department', data['Department'].unique())
    role = st.sidebar.multiselect('Select Role', data['Role'].unique())
    filtered_data = data[data['Department'].isin(department) & data['Role'].isin(role)]
    st.write(filtered_data)

# Function for Predictive Analytics
def predictive_analytics():
    st.title("Predictive Analytics")
    # ... predictive analytics code ...

# Function for Polish and Styling
def polish_and_styling():
    st.title("Polish and Styling")
    # ... polish and styling information or code ...

# Sidebar for page selection
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Data Exploration", "In-depth Analysis & Visualization", "Interactive Features", "Predictive Analytics", "Polish and Styling"])

# Render content based on selection
if selection == "Home":
    st.title("Welcome to the HR Dashboard!")
    st.write("Choose a section from the sidebar to navigate.")

elif selection == "Data Exploration":
    data_exploration()

elif selection == "In-depth Analysis & Visualization":
    in_depth_analysis()

elif selection == "Interactive Features":
    interactive_features()

elif selection == "Predictive Analytics":
    predictive_analytics()

elif selection == "Polish and Styling":
    polish_and_styling()
