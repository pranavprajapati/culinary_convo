import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.title("Culinary Convo👋")
st.markdown("<br><br><br>", unsafe_allow_html=True)

cols = st.columns((4, 4))

cols[0].image("static/user_icon.png",width=150,caption = 'IngredientGuru')
recipe_chat = cols[0].button('Recipe Chat')

cols[1].image("static/recipe_maker.png",width=150,caption = 'GourmetGhostwriter')
recipe_maker = cols[1].button('Recipe Blog Post Maker')

if recipe_chat:

    switch_page("Recipe Chat")

if recipe_maker:

    switch_page("Recipe Blog Post")
