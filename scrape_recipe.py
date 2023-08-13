from recipe_scrapers import scrape_me


def scrape_it(url):
    scraper = scrape_me(url)
    ing = scraper.ingredients()
    return ing


