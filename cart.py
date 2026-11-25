from settings import PRODUCTS
from texts import TEXTS


class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, key):
        self.items.append(key)
        
    def is_empty(self):
        return len(self.items) == 0
    
    def total(self):
        return sum(PRODUCTS[key][1] for key in self.items)
    
    def text(self, lang):
        t = TEXTS[lang]
        if self.is_empty():
            return t["cart_empty"]
        lines = [t["cart_title"]]
        for key in self.itmes:
            name, price = PRODUCTS[key]
            lines.append(f"  {name} - {price} so'm ")
        lines.append(f"\n{t['total']}: {self.total()} so'm") 
        return "\n".join(lines)                     