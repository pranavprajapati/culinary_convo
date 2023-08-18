from recipe_scrapers import scrape_me
import streamlit as st
from datetime import datetime
import pywhatkit
import time,webbrowser,pyautogui
import pandas as pd

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
            
def replace_ingredients(output, ingredients, replacement_list):
    # Iterate through the replacement list
    for initial_ingredient in replacement_list:
        # Check if the initial ingredient is mentioned in any of the sentences in the output
        for sentence in output:
            if initial_ingredient.lower() in sentence.lower():
                # Extract the replacement ingredient from the sentence
                replacement = sentence.split(":")[1].split(".")[0].strip().lower()
                if 'could be' in replacement:
                    replacement = replacement.split('could be')[1].strip()
                elif 'would be' in replacement:
                    replacement = replacement.split('would be')[1].strip()
                # Replace the initial ingredient with the replacement ingredient in the original ingredients list
                ingredients = [ingredient.lower().replace(initial_ingredient.lower(), replacement) for ingredient in ingredients]
                break  # Move to the next initial ingredient
    return ingredients

def check_ingredients(ingredients_input):
    all_products_loaded_df = pd.read_csv('all_products.csv')
    all_products_loaded = all_products_loaded_df['product_name'].values
    ingredients_list = [item.strip().lower() for item in ingredients_input]
    return all(any(ingredient in product for product in all_products_loaded) for ingredient in ingredients_list)
