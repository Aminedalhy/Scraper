from Helpers.config import API_KEY
from urllib.parse import urlencode

def get_scrapeops_url (url, location):
    if not API_KEY:
        raise ValueError ("API KEY is missing from environment")
    payload = {
        "api_key": API_KEY,
        "url":url,
        "country": location
    }
    return "https://proxy.scrapeops.io/v1/?" + urlencode(payload)