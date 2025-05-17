import streamlit as st
import pandas as pd
import os
from Controllers.scraper_controller import search_products
from Pipelines.data_pipeline import DataPipeline

st.set_page_config (page_title="Amazon Scraper", page_icon="AS")
st.title("Amazon Product Scraper")
product_name = st.text_input ("Enter the name of the product to search for: ")


if st.button("Scrape"):
    filename = f"{product_name}.csv"
    pipeline = DataPipeline(csv_filename=filename)

    try:
        search_products(product_name, data_pipeline=pipeline)
        pipeline.close_pipeline()
        if os.path.exists(filename):
            df= pd.read_csv(filename)
            st.success("scraping complete")
            st.dataframe(df)
            st.download_button("Download CSV", df.to_csv(index=False), file_name=filename, mime="text/csv")
        else:
            st.warning("no results were found")
    
    except ValueError as ve:
        st.error(f"Error: {ve}")
        
