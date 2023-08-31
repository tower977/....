import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
hr_data = pd.read_csv('HRDataset_v14.csv')
hr_data['DateofHire'] = pd.to_datetime(hr_data['DateofHire'])
hr_data['DateofTermination'] = pd.to_datetime(hr_data['DateofTermination'])
hr_data['Tenure'] = (hr_data['DateofTermination'].fillna(datetime.today()) - hr_data['DateofHire']).dt.days / 365

def main():
    st.title("Employee Utilization Dashboard")

    st.sidebar.header('Navigation')
    page = st.sidebar.radio("Choose an Analysis", ["Homepage", "Demographic Analysis", "Employment Analysis", "Performance Analysis", "Managerial Analysis", "Attendance Analysis"])

    if page == "Homepage":
        st.write("Welcome Vanessa and Lennon to the Employee Utilization Dashboard. Navigate using the sidebar to view different analyses and visualizations. Please ask any questions that peak your interest.")

    elif page == "Demographic Analysis":
        st.header("Demographic Analysis")

        # Gender Distribution
        st.subheader("Distribution by Gender")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=hr_data, x='Sex', ax=ax1, order=hr_data['Sex'].value_counts().index)
        st.pyplot(fig1)

        # Marital Status Distribution
        st.subheader("Distribution by Marital Status")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=hr_data, x='MaritalDesc', ax=ax2, order=hr_data['MaritalDesc'].value_counts().index)
        st.pyplot(fig2)

        # Race Distribution
        st.subheader("Distribution by Race")
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=hr_data, x='RaceDesc', ax=ax3, order=hr_data['RaceDesc'].value_counts().index)
        st.pyplot(fig3)

    elif page == "Employment Analysis":
        st.header("Employment Analysis")

        # Distribution by Position
        st.subheader("Distribution by Position")
        fig1, ax1 = plt.subplots(figsize=(8, 7))
        sns.countplot(data=hr_data, y='Position', ax=ax1, order=hr_data['Position'].value_counts().index)
        st.pyplot(fig1)

        # Distribution by Department
        st.subheader("Distribution by Department")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=hr_data, y='Department', ax=ax2, order=hr_data['Department'].value_counts().index)
        st.pyplot(fig2)

        # Distribution of Reasons for Termination
        st.subheader("Distribution of Reasons for Termination")
        terminated_employees = hr_data[hr_data['Termd'] == 1]
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=terminated_employees, y='TermReason', ax=ax3, order=terminated_employees['TermReason'].value_counts().index)
        st.pyplot(fig3)

        # Distribution by Recruitment Source
        st.subheader("Distribution by Recruitment Source")
        fig4, ax4 = plt.subplots(figsize=(8, 7))
        sns.countplot(data=hr_data, y='RecruitmentSource', ax=ax4, order=hr_data['RecruitmentSource'].value_counts().index)
        st.pyplot(fig4)

    elif page == "Performance Analysis":
        st.header("Performance Analysis")

        # Distribution of performance scores across departments
        st.subheader("Performance Score Distribution by Department")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.countplot(data=hr_data, x='PerformanceScore', hue='Department', ax=ax1)
        st.pyplot(fig1)

        # Correlation between engagement survey results and performance scores
        st.subheader("Engagement Survey vs. Performance Score")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=hr_data, x='PerformanceScore', y='EngagementSurvey', ax=ax2)
        st.pyplot(fig2)

        # Relationship between special projects count and performance score
        st.subheader("Special Projects Count vs. Performance Score")
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=hr_data, x='PerformanceScore', y='SpecialProjectsCount', ax=ax3)
        st.pyplot(fig3)

    elif page == "Managerial Analysis":
        st.header("Managerial Analysis")

        # Number of employees under each manager
        st.subheader("Number of Employees by Manager")
        fig1, ax1 = plt.subplots(figsize=(10, 8))
        sns.countplot(data=hr_data, y='ManagerName', ax=ax1, order=hr_data['ManagerName'].value_counts().index)
        st.pyplot(fig1)

        # Average performance score of employees under each manager
        st.subheader("Average Engagement Survey Score by Manager")
        fig2, ax2 = plt.subplots(figsize=(10, 8))
        sns.barplot(data=hr_data, y='ManagerName', x='EngagementSurvey', ax=ax2, ci=None)
        st.pyplot(fig2)

        # Employee satisfaction score distribution by manager
        st.subheader("Employee Satisfaction by Manager")
        fig3, ax3 = plt.subplots(figsize=(10, 8))
        sns.boxplot(data=hr_data, y='ManagerName', x='EmpSatisfaction', ax=ax3)
        st.pyplot(fig3)

    elif page == "Attendance Analysis":
        st.header("Attendance Analysis")

        # Distribution of the number of times employees were late in the last 30 days
        st.subheader("Distribution of Lateness in the Last 30 Days")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.histplot(hr_data['DaysLateLast30'], kde=True, ax=ax1)
        st.pyplot(fig1)

        # Relationship between lateness and performance scores
        st.subheader("Lateness vs. Performance Score")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=hr_data, x='PerformanceScore', y='DaysLateLast30', ax=ax2)
        st.pyplot(fig2)


    # ... You can continue this structure for Performance Analysis, Managerial Analysis, and Attendance Analysis

if __name__ == "__main__":
    main()
