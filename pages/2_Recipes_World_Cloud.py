import streamlit as st
from PIL import Image

st.set_page_config(page_title="Recipes Word Cloud", page_icon="", layout="wide")

st.write(" ### Ingredients in Corpus - Word Cloud")


image = Image.open("images/word_cloud.png")
st.image(image, caption=None)
