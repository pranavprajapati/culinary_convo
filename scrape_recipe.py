from recipe_scrapers import scrape_me


def scrape_valid_recipe(url):
    scraper = scrape_me(url)
    ingredients = scraper.ingredients()
    instructions = scraper.instructions_list()
    return ingredients,instructions


