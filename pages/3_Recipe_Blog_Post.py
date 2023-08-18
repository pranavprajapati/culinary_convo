import streamlit as st
from streamlit_extras.colored_header import colored_header
from utilities import check_ingredients

def initialize_session():
    if "ingredientsinput" not in st.session_state:
        st.session_state.ingredientsinput = []
    if "instructions" not in st.session_state:
        st.session_state.instructions = ""
    if "recipe_title" not in st.session_state:
        st.session_state.recipe_title = ""
    if "theme" not in st.session_state:
        st.session_state.theme = ""
    if "blog_displayed" not in st.session_state:
        st.session_state.blog_displayed = False

def make_blog_post():
    #check if ingredients are valid
    st.session_state.blog_displayed = check_ingredients(st.session_state.ingredientsinput)
    #code to get recipe scraped

initialize_session()
st.title("Your own Flavor Fictionist ✏️")

with st.form("my_recipe"):
    # Recipe Title
    recipetitle = st.text_input("Enter Recipe Title:",key="recipe_title")

    # Recipe Ingredients
    ingredientsinput = st.text_area(label = "Enter Ingredients (comma-separated):",key="ingredients_input")
    ingredients_list = [item.strip() for item in ingredientsinput.split(',')] if ingredientsinput else [] 

    # Recipe Instructions
    instructions = st.text_area(label ="Enter Steps or Instructions:",key="instructions_input")
    
    theme = st.selectbox(label = "Select theme for blog post", options = ["Cultural Exploration", "Healthy Living and Nutritional Focus", "Seasonal and Farm-to-Table Experience","Family and Comfort Cooking"],key="theme_input")

    submit_recipe = st.form_submit_button('Submit',on_click=make_blog_post)

    if submit_recipe:
        print("You submitted the following recipe:")

if st.session_state.blog_displayed:
        
        colored_header(
                label="Your blog post is ready!: ",
                description="GourmetGhostwriter",
                color_name="violet-70",
            )
        
st.caption("Made with ❤️ by Pranav")