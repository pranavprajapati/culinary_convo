# Culinary Convo
A project that combines natural language processing and culinary creativity, enabling users to engage in dynamic recipe adjustments through interactive conversations

## Features

- Generate Ingredient Replacements 
- Send grocery list to Whatsapp
- Generate themed blog posts for your recipes
- Version Control your Prompts
- Scrape your favorite recipes
  
# Demo

## Ingredients Guru
![Alt Text](https://github.com/pranavprajapati/culinary_convo/blob/main/static/recipe_chat.gif)

## Gourmet Ghostwriter
![Alt Text](https://github.com/pranavprajapati/culinary_convo/blob/main/static/recipe_blog.gif)

## How to Run the project

1. Get a free API Key from [OpenAI](https://platform.openai.com/account/api-keys) & [PromptLayer](https://promptlayer.com/)

To run this project, you will need to add the following environment variables to your .env file or .streamlit/secrets.toml file

`OPENAI_API_KEY`

`PROMPTLAYER_API_KEY`

3. Clone the repo
   ```sh
   git clone https://github.com/pranavprajapati/culinary_convo.git
   ```
4. Install required python packages
   ```sh
   cd repository
   conda create --name convo
   conda activate convo
   conda install --file requirements.txt
   ```
5. Start Streamlit Application
   ```sh
   streamlit run Home.py
   ```

### Images Used
<br>
<a href="https://www.flaticon.com/free-icons/recipe" title="recipe icons">Recipe icons created by Freepik - Flaticon</a>
<a href="https://www.flaticon.com/free-icons/chef" title="chef icons">Chef icons created by Freepik - Flaticon</a>

## Roadmap

- [ ] Add Support for different LLMs providers
- [ ] Import Prompt templates from PromptLayer 
- [ ] Add Restaurant Recommendation for a recipe in your city
- [ ] Custom Chat bot 
- [ ] Add Recipes from other sources  
    - [ ] Youtube
    - [ ] Images

Please create a pull request if you wish to contribute!

## Authors

- [@pranavprajapati](https://www.github.com/pranavprajapati)

