
from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.chat_models import ChatOpenAI
import streamlit as st

def get_suggestions(title,ing,ins,rep):

    llm = ChatOpenAI(temperature=0.6,model_name = "gpt-3.5-turbo",openai_api_key=st.secrets["OPENAI_API_KEY"])

    template = """You are an expert chef, specializing in ingredient substitutions. You have the title, 
    ingredients, and instructions of a specific recipe. The user will provide you with certain ingredients 
    they wish to replace in this recipe. Your task is to suggest ideal replacements for each specified 
    ingredient, ensuring that the substitutes belong to the same food group and have a similar flavor profile. 
    Along with each substitution, please provide a brief explanation as to why the chosen replacement is suitable, 
    considering factors such as taste, texture, and culinary use. Focus solely on providing ingredient replacements 
    without altering the original recipe or offering any additional information or guidance.

    Title: {title}
    Ingredients: {ingredients}
    Instructions: {instructions}
    Ingredients that require replacement: {replacements}
    Suggestions: Here are the suggestions:"""
    
    prompt_template = PromptTemplate(input_variables=["title", "ingredients","instructions","replacements"], template=template)
    
    llm_chain = LLMChain(llm = llm, prompt = prompt_template)

    output = llm_chain(inputs={"title":title,"ingredients":ing,"instructions":ins,"replacements":rep})

    return output


