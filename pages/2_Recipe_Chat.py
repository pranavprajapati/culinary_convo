
import streamlit as st
import os
from langchain import OpenAI
import validators
import time
from scrape_recipe import scrape_valid_recipe



def is_valid_url(url):
    return validators.url(url)

def get_recipe_detils():
    #code to get recipe scraped
    ingredients,instructons  = scrape_valid_recipe(st.session_state.recipe_link)

    ingredients_html = "<ul style='line-height: 0.9;'>"
    for ing in ingredients:
        ingredients_html += f"<li>{ing}</li>"
    ingredients_html += "</ul>"
    st.write("Ingredients:")
    st.markdown(ingredients_html, unsafe_allow_html=True)


st.title("Your own Flavor Companion 🤖")

with st.form("my_form"):

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




