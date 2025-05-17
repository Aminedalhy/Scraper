import streamlit as st
import pandas as pd
import os
from Controllers.scraper_controller import search_products
from Pipelines.data_pipeline import DataPipeline
from Agents.Agent_feedback import recommend_best_deal_with_ai

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

    
st.markdown("---")
if product_name and os.path.exists (f"{product_name}.csv"):
    if st.button("recommend the best deal"):
         with st.spinner ("the AI agent is thinking..."):
            product, reason = recommend_best_deal_with_ai (f"{product_name}.csv")
            st.success (f" Recommended product : *** {product}***")
            st.info (f" Reason {reason}")

