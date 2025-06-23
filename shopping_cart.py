from typing import List

class ShoppingCart:
    def __init__(self, max_size:int) -> None:
        """Initialize the shopping cart with a maximum size."""
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str):
        """Add an item to the shopping cart."""
        if self.size() == self.max_size:
            raise OverflowError("Cannot add more items, cart is full.")
        self.items.append(item)

    def size(self) -> int:
        """Return the number of items in the shopping cart."""
        return len(self.items)

    def get_items(self) -> List[str]:
        """Return a list of items in the shopping cart."""
        return self.items.copy()

    def get_total_price(self, price_map):
        """Return the total price of items in the shopping cart."""
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price


