from recipe_scrapers import scrape_me
import streamlit as st

def scrape_valid_recipe(url):
    scraper = scrape_me(url)
    ingredients = scraper.ingredients()
    instructions = scraper.instructions_list()
    title = scraper.title()
    return ingredients,instructions,title


def check_ingredients(user_input, ingredients_list):
    user_ingredients = [ingredient.strip() for ingredient in user_input.split(',')]

    for user_ingredient in ingredients_list:
        # Check if the user ingredient is part of any ingredient in the original recipe
        if any(user_ingredient in ingredient for ingredient in ingredients_list):
            return True
        else:
            st.write(f"{user_ingredient} is not present in the original recipe.")
            return False
            
