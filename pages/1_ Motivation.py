import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Welcome to FoodFlex", page_icon="", layout="wide"
)

left_column, right_column = st.columns(2)

with left_column:
    image = Image.open("images/Confused_cooking.png")
    new_image = image.resize((600, 600))
    st.image(new_image, caption=None)


with right_column:
    st.markdown(
        """
        ### Motivation
        ## Ignorance for some never explored ingredients:
        - The way I usually handle cooking is buying ingredients that I enjoy and are healthy enough.
        - It usually ends up well, especially with the right Spices.
        - **But** I wanted to explore recipes now, and start learning about and tracking my food's nutrition facts as well.
        ## What should I get from supermarket in total, considering several recipes plan?:
        - If I try to vary the recipes or prepare for several recipes per week, It is hard to know how much to purchase from each ingredients.
        - Many ingredients end up being thrown to trash because they did not fit in a recipe or overflowed from previous recipes.
        """
    )
