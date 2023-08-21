
import streamlit as st
import os
from langchain import OpenAI
import validators
import time
from utilities import scrape_valid_recipe,check_ingredients,replace_ingredients
from ingredientguru import get_suggestions
from streamlit_extras.colored_header import colored_header
import promptlayer

import pywhatkit
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
promptlayer.api_key = os.environ['PROMPTLAYER_API_KEY']

def is_valid_url(url):
    return validators.url(url)

def initialize_session_state():
    if "recipe_link" not in st.session_state:
        st.session_state.recipe_link = ''
    if "ingredients" not in st.session_state:
        st.session_state.ingredients = []
    if "instructions" not in st.session_state:
        st.session_state.instructions = []
    if "title" not in st.session_state:
        st.session_state.title = ""
    if "recipe_displayed" not in st.session_state:
        st.session_state.recipe_displayed = False

def get_recipe_detils():
    #code to get recipe scraped
    st.session_state.ingredients,st.session_state.instructions,st.session_state.title  = scrape_valid_recipe(st.session_state.recipe_link)
    st.session_state.recipe_displayed = True

initialize_session_state()


st.title("Your own Flavor Companion 🤖")

with st.form("my_replacement"):

    # Take user input and placeholder write full url of recipe
    recipe_link = st.text_input(label = 'What Recipe do you like ? ',placeholder= "Full url of recipe", key="recipe_link")
    submit_link = st.form_submit_button('Submit',on_click=get_recipe_detils)

    if submit_link:
        if is_valid_url(recipe_link):
            st.write("You submitted the following link:", recipe_link)
            st.write("Please wait while we process your request")
        else:
            st.write("Please enter a valid url")
            st.stop()

ingredients_html = "<ul style='line-height: 0.9;'>"
for ing in st.session_state.ingredients:
    ingredients_html += f"<li>{ing}</li>"
ingredients_html += "</ul>"
st.markdown("**Recipe**: " + st.session_state.title)
st.write("Ingredients:")
st.markdown(ingredients_html, unsafe_allow_html=True)

st.write("Instructions:")
instructions_html = "<ol style='line-height: 0.9;'>"
for ins in st.session_state.instructions:
    instructions_html += f"<li>{ins}</li>"
instructions_html += "</ol>"
st.markdown(instructions_html, unsafe_allow_html=True)


if st.session_state.recipe_displayed:

    cols = st.columns([0.5,0.5])
    help_choice = st.radio(
        "Would you like help with the ingredient replacements?",
        ("No, thank you", "Help with ingredient replacements")
        )
    if help_choice == "No, thank you":
        st.write("Thank you for using Flavor Companion 🤖")
    if help_choice == "Help with ingredient replacements":
        user_input = st.text_input(label = "What do you want to replace ?",placeholder = "Enter the ingredients you wish to replace, separated by commas")
        if user_input:
            
            colored_header(
                label="Your suggestions are ready: ",
                description="IngredientGuru",
                color_name="violet-70",
            )

            if check_ingredients(user_input,st.session_state.instructions):
                replacements = [ingredient.strip() for ingredient in user_input.split(',')]

                suggestions = get_suggestions(st.session_state.title,st.session_state.ingredients,st.session_state.instructions,replacements)

                formatted_suggestions = [line for line in suggestions['text'].split('- ') if line.strip()]

                new_ingredients = replace_ingredients(formatted_suggestions, st.session_state.ingredients , replacements)
                message = '\n'.join(new_ingredients)
                # Start the HTML unordered list
                html_output = '<ul>'
                
                # Iterate through the suggestions, applying the alternate colors
                for idx, topic in enumerate(formatted_suggestions):
                    color = 'darkblue' if idx % 2 == 0 else 'darkgreen'
                    html_output += f"<li style='color: {color};'>{topic}</li>"

                # Close the HTML unordered list
                html_output += '</ul>'

                # Write the HTML to the Streamlit app
                st.markdown(html_output, unsafe_allow_html=True)
                if st.button('Send the grocery list to my phone'):
                    
                    pywhatkit.sendwhatmsg_to_group_instantly(st.secrets["group_link"], message)
                st.stop()
            
st.caption("Made with ❤️ by Pranav")