import streamlit as st
from multiapp import MultiApp
from apps import data, model # import your app modules here
from PIL import Image

app = MultiApp()

# Set the wide range of Dashboard
st.set_page_config(layout="wide")

# Logo of Resoluteai.in
image = Image.open("ri.jpg")
st.image(image, width=600)

# title of Dashboard
st.title("Resoluteai.in Data Science Tool")
st.write("Welcome to the Dashboard Tool and Predictive Tool")

# Add all your application here
app.add_app("Data Explore", data.app)
app.add_app("Predictive Analysis", model.app)

# Run the app
app.run()
