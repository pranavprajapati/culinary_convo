import streamlit as st
from streamlit_extras.switch_page_button import switch_page


# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

st.title("Culinary Convo👋")
st.image("static/user_icon.png",width=32)

cols = st.columns((2, 2))

recipe_chat = cols[0].button('Recipe Chat')

recipe_maker = cols[1].button('Recipe Blog Post Maker')

if recipe_chat:

    switch_page("Recipe Chat")

if recipe_maker:

    switch_page("Recipe Blog Post")
