from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.chat_models import ChatOpenAI
import streamlit as st


## Router Chain

comfort_template = """
You are an expert food blogger, who values family traditions and comfort cooking.\
The user has provided the title, ingredients, and instructions for a specific recipe. The user will also provide some \
Create a heartfelt 300-word blog post focusing on family memories, passed-down secrets, and the joy of bonding over cooking. \
The post should concentrate on the narrative and not include the recipe details.


Title: {title}
Ingredients: {ingredients}
Instructions: {instructions}

Write Blog Post:
"""


seasonal_farm_two_table_template = """
You are an expert food blogger, passionate about seasonal and farm-to-table cuisine. \
The user has provided the title, ingredients, and instructions for a specific recipe. User also talks about \
Compose a 300-word blog post highlighting the seasonality of the ingredients and the farm-to-table philosophy.\
Discuss freshness, support for local farmers, and seasonal availability. \
The post should consist solely of the narrative, without the recipe details.

Title: {title}
Ingredients: {ingredients}
Instructions: {instructions}

Write Blog Post:
"""

healthy_living_template = """
You are an expert food blogger, with a focus on healthy living and nutrition.\
The user has provided the title, ingredients, and instructions for a specific recipe.\
Craft a 300-word blog post emphasizing its nutritional benefits and alignment with a healthy lifestyle.\
Explore aspects such as nutritional value, diet-friendly variations, and organic ingredient options. \
The post should contain only the narrative, excluding the recipe details.

    Title: {title}
    Ingredients: {ingredients}
    Instructions: {instructions}

Write Blog Post:
"""


cultural_exploration_template = """ 
You are an expert food blogger, specializing in culinary cultural exploration. \
The user has provided the title, ingredients, and instructions for a specific recipe. \
Your task is to write a concise 300-word blog post focusing on its cultural origins and significance.\
Delve into the history, traditional cooking methods, and cultural variations of the dish.\
Please note that the blog post should only include the narrative and not the recipe details.

Title: {title}
Ingredients: {ingredients}
Instructions: {instructions}

Write Blog Post:
"""
theme_templates = {
    "Select": "",
    "Cultural Exploration": cultural_exploration_template,
    "Healthy Living and Nutritional Focus": healthy_living_template,
    "Seasonal and Farm-to-Table Experience": seasonal_farm_two_table_template,
    "Family and Comfort Cooking": comfort_template
}

def generate_blog_post(title,ing,ins,theme):
    if theme == "Select":
        st.write("Your GourmetGhostwriter is ready!")
    else:
        llm = ChatOpenAI(temperature=0.6,model_name = "gpt-3.5-turbo",openai_api_key=st.secrets["OPENAI_API_KEY"])
        selected_template = theme_templates[theme]
        prompt_template = PromptTemplate(input_variables=["title", "ingredients","instructions"], template=selected_template)
        llm_chain = LLMChain(llm = llm, prompt = prompt_template)
        output = llm_chain(inputs={"title":title,"ingredients":ing,"instructions":ins})
        return output