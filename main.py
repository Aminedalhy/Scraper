from Controllers.scraper_controller import search_products


PRODUCTS = ["MAC"]
MAX_RETRIES = 3

for product in PRODUCTS:
    results = search_products(product,retries=MAX_RETRIES)

    for items in results:
        print(items)
        