import requests
import logging
from bs4 import BeautifulSoup
from Products.product import ScrapedProduct
from Helpers.utils import get_scrapeops_url


logger= logging.getLogger(__name__)

def search_products( product_name: str, page_number: int=1, location:str="us", retries: int=2):
    scraped_products= []
    attempts =0
    success = False

    while attempts < retries and not success:
        try: 
            search_url = get_scrapeops_url(f"https://www.amazon.com/s?k={product_name}&page={page_number}",location)
            logger.info ( f" Fetching: {search_url}")
            response= requests.get(search_url)
            if response.status_code!=200:
                raise Exception (f"Status code: { response.status_code}")
            
            logger.info( "Successfull fetched page")
            soup= BeautifulSoup( response.text, "html.parser")
            for ad_div in soup.find_all("div",class_="AdHolder"):
                ad_div.decompose()
            
            product_divs = soup.find_all("div")
            for product_div in product_divs:
                h2 = product_div.find("h2")
                if not h2 or not h2.text.strip():
                    continue
                product_title = h2.text.strip()
                a=h2.find("a")
                product_url = a.get("href") if a and a.get("href") else "no product url"
                name = product_div.get("data-asin")
                if not name: 
                    continue

                is_sponsored= "sspa" in product_url.lower()

                price_currency=product_div.find("span", class_="a-price-symbol")

                currency= price_currency.text if price_currency else ""

                prices = product_div.find_all("span", class_="a-offscreen")
                try: 

                    current_price = float(prices[0].text.replace(currency, "").replace(",","").strip()) if prices else 0.0
                    original_price = float(prices[1].text.replace(currency,"").replace(",","").strip()) if len(prices)>1 else current_price
                except:
                 continue

                rating_tag= product_div.find("span", class_="a-icon-alt")
                try:
                    rating = float(rating_tag.text[0:3]) if rating_tag else 0.0
                except: 
                    rating= 0.0
                
                product = ScrapedProduct(
                    name=name, 
                    product_title=product_title,
                    product_url=product_url,
                    current_price=current_price,
                    original_price=original_price,
                    currency=currency,
                    rating=rating,
                    is_sponsored=is_sponsored  
                )
                scraped_products.append(product)
            
            success = True

        except Exception as e: 
            logger.warning(f"Attempts {attempts +1 } failed: {e}")
            attempts+=1
    
    if not success:
        logger.error(" scraping failed")
    

    return scraped_products