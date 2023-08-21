import streamlit as st
from streamlit_extras.colored_header import colored_header
from utilities import check_valid_ingredients
from gourmetghostwriter import generate_blog_post
import pandas as pd

def initialize_session():
    if "ingredients_input" not in st.session_state:
        st.session_state.ingredients_input = ""
    if "instructions_input" not in st.session_state:
        st.session_state.instructions_input = ""
    if "recipe_title" not in st.session_state:
        st.session_state.recipe_title = ""
    if "blog_displayed" not in st.session_state:
        st.session_state.blog_displayed = False

def make_blog_post():
    #check if ingredients are valid
    st.session_state.ingredients_list = [item.split()[-1] for item in st.session_state.ingredients_input.split(',')] if st.session_state.ingredients_input else [] 
    st.session_state.blog_displayed = check_valid_ingredients(st.session_state.ingredients_list)


initialize_session()
st.title("Your own Flavor Fictionist ✏️")

with st.form("my_recipe"):
    # Recipe Title
    recipetitle = st.text_input("Enter Recipe Title:",key="recipe_title")

    # Recipe Ingredients
    ingredientsinput = st.text_area(label = "Enter Ingredients (comma-separated):",key="ingredients_input") 

    # Recipe Instructions
    instructions = st.text_area(label ="Enter Steps or Instructions:",key="instructions_input")
    
    submit_recipe = st.form_submit_button('Submit',on_click=make_blog_post)

    if submit_recipe:
        print("You submitted the following recipe:")

if st.session_state.blog_displayed:


    theme = st.selectbox(label = "Select theme for blog post", options = ["Select","Cultural Exploration", "Healthy Living and Nutritional Focus", "Seasonal and Farm-to-Table Experience","Family and Comfort Cooking"],index = 0)
    blog_post = generate_blog_post(st.session_state.recipe_title,st.session_state.ingredients_list ,st.session_state.instructions_input ,theme)
    if theme != "Select":

        colored_header(
                label="Your blog post is ready! : ",
                description="GourmetGhostwriter",
                color_name="violet-70",
                )
    
        st.write(blog_post['text'])
else:
    st.write("Please enter valid ingredients to generate a blog post.")
    

st.caption("Made with ❤️ by Pranav")