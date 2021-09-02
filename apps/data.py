# import Dependencies
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image



def app():
    
    # Title of Data Visualization App
    st.header("Data Visualization Dashboard")

    # Create the file uploader for upload the file
    upload_file = st.sidebar.file_uploader(
        "Upload the CSV and Excel File...", type=["csv", "xlsx"])


    # Create a function to upload the excel file in dataframe
    def upload(upload_file):
        if upload_file is not None:
            try:
                df = pd.read_csv(upload_file)
            except Exception as e:
                print(e)
                df = pd.read_excel(upload_file)

            return df


    df = upload(upload_file)

    st.write(df)

    # Create the Date , month , year filters for Schedule Delievery.
    st.sidebar.header("Enter the Schedule Delievery Date, Month and Year")


    date_filter = st.sidebar.text_input("Date Filter:")
    month_filter = st.sidebar.text_input("Month Filter:")
    year_filter = st.sidebar.text_input("Year Filter:")

    # Create a function to analysis all the information


    def data_analysis(df, date_filter, month_filter, year_filter):
        """
        Function to Create all the bar charts and show all the 
        information about the data of the particular day

        Arguments :
            df :- Uploaded dataframe
            data_filter :- Take Date as an input
            month_filter :- Take month as an input
            year_filter :- Take year as an input
            country_filter : Take country as an input
        """

        st.header("All Information Acoording to Schedule Delievery Date")
        try:
            df1 = df.loc[df["Scheduled Delivery Date"] ==
                        date_filter+"-"+month_filter+"-"+year_filter]
            st.dataframe(df1)
        except Exception as e:
            st.warning("Warning , There is an Issue with your Data.")

        col1, col2 = st.columns([2, 2])
        col3, col4 = st.columns([2, 2])
        col5, col6 = st.columns([2, 2])
        col7, col8 = st.columns([2, 2])
        col9, col10 = st.columns([2, 2])
        col11, col12 = st.columns([2, 2])
        col13, col14 = st.columns([2, 2])

        try:
            plot1 = px.histogram(df1, x='Country', title="Country", color_discrete_sequence=[
                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Country")
            col1.plotly_chart(plot1)

            plot2 = px.histogram(df1, x="Shipment Mode", title="Shipment Mode", color_discrete_sequence=[
                                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Shipment Mode")
            col2.plotly_chart(plot2)

            plot3 = px.histogram(df1, x="Fulfill Via", title="FulFill Mode", color_discrete_sequence=[
                                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Fulfill Via")
            col3.plotly_chart(plot3)

            plot4 = px.histogram(df1, x="Sub Classification", title="Sub Classification", color_discrete_sequence=[
                                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Sub Classification")
            col4.plotly_chart(plot4)

            plot5 = px.histogram(df1, x="Vendor INCO Term", title="Vendor INCO Term", color_discrete_sequence=[
                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Vendor INCO Term")
            col5.plotly_chart(plot5)

            plot6 = px.histogram(df1, x="Managed By", title="Managed Companies", color_discrete_sequence=[
                                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Managed By")
            col6.plotly_chart(plot6)

            plot7 = px.histogram(df1, x="Manufacturing Site", title="Top Manufacturing Site", color_discrete_sequence=[
                                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Manufacturing Site")
            col7.plotly_chart(plot7)

            plot8 = px.histogram(df1, x="Molecule/Test Type", title="Compare Different Test Type", color_discrete_sequence=[
                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Molecule/Test Type")
            col8.plotly_chart(plot8)

            plot9 = px.histogram(df1, x="Dosage Form", title="Different Dosage Form", color_discrete_sequence=[
                "rgb(244,109,67)", "rgb(224,243,248)", "rgb(244,109,67)", "magenta", "rgb(254,224,144)", "green", "red", "#00D", "goldenrod"], color="Dosage Form")
            col9.plotly_chart(plot9)

            # Each and Every Vendor Name
            with col10:
                st.subheader("Vendors Name According to Schedule Delivery Date")
                for i in df1["Vendor"].unique():
                    st.write("-", i)

            with col11:
                # Brand Name
                st.subheader("Brand Name According to Schedule Delivery Date")
                for i in df1["Brand"].unique():
                    st.write("-", i)

            with col12:
                # Create the table to show the Dosage Forms
                st.subheader("Different Dosage Forms According to Test Type")
                dosage_form = df1.groupby(
                    ["Dosage Form", "Molecule/Test Type"]).size().reset_index(name="Counts")
                st.write(dosage_form)

            with col13:
                # Eahc and Every Dosage Form
                st.subheader("Total Dosage Form")
                for i in df1["Dosage Form"].unique():
                    st.write("-", i)

            with col14:
                # Total Vendor INCO Terms
                st.subheader("Total Vendor INCO Terms (Rules)")
                for i in df1["Vendor INCO Term"].unique():
                    st.write("-", i)

            # Total Manufactoring Site
            st.subheader("Different Manufactoring Site")
            for i in df1["Manufacturing Site"].unique():
                st.write("-", i)

            # Total Pack Price
            st.subheader("Total Pack Price")
            st.text(df1["Pack Price"].sum())

            # Total Unit Price
            st.subheader("Total Unit Price")
            st.text(df1["Unit Price"].sum())

        except Exception as e:
            st.warning("Warning , There is an issue with Your Input.")


    if st.sidebar.button("Process", key="1"):
        data_analysis(df, date_filter, month_filter, year_filter)