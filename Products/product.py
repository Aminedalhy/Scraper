from dataclasses import dataclass, fields

@dataclass
class ScrapedProduct:
    name: str =""
    product_title: str=""
    product_url: str=""
    current_price: float =None
    original_price: float=None
    currency: str=""
    rating:float=None
    is_sponsored: bool = False