import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Welcome to FoodFlex",
    page_icon="",
    layout="wide"
)

left_column, right_column = st.columns(2)

with left_column:
	image = Image.open('images/recipes.png')
	new_image = image.resize((600, 600))
	st.image(new_image, caption=None)

with right_column:
	st.markdown(
		"""
		## Welcome to FoodFlex - Your Fooood Explorer!

		Are you tired of staring at your refrigerator, wondering what to cook with the ingredients you have on hand? Or perhaps you're looking for exciting new recipes that match your taste preferences? Look no further - FoodFlex is here to revolutionize your cooking experience!

		## Discover Your Culinary Matches

		With FoodFlex, finding the perfect recipe is a breeze. You have two fantastic options to explore:

		### 1. Recipe Matching:

		Have a favorite recipe in mind but want to try something similar? Simply enter the name of your beloved dish, and FoodFlex will work its magic to recommend recipes that share similar ingredients and flavors. Expand your culinary horizons with ease!

		### 2. Ingredients Input:

		Got a list of ingredients you frequently buy? Use our convenient input feature to enter those items, and FoodFlex will curate a selection of mouthwatering recipes that perfectly complement your shopping preferences. Say goodbye to wasted ingredients and hello to delicious possibilities!

		### 3. Watch your recipes nutritional facts:

		Stay aware of the nutrients and the calories of the recommended recipes :)
		"""
	)	

