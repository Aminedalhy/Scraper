from Controllers.scraper_controller import search_products
from Pipelines.data_pipeline import DataPipeline


PRODUCTS = ["MAC"]
MAX_RETRIES = 3

for product in PRODUCTS:
    product_pipeline = DataPipeline(csv_filename=f"{product}.csv")
    search_products(product,retries=MAX_RETRIES, data_pipeline=product_pipeline)
    product_pipeline.close_pipeline()

        