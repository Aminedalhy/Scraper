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


    def __post_init_(self):
        for field in fields (self):
            value = getattr(self, field.name)
            if isinstance( value, str):
                setattr(self, field.name, value.strip() if value.strip() else f" No {field.name}")