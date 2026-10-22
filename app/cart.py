from dataclasses import dataclass


@dataclass
class Item:
    price: float
    quantity: int
# Aplicação do Refactor
    def total(self) -> float:
        return self.price * self.quantity


class Cart:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, price: float, quantity: int) -> None:
        self.items.append(Item(price, quantity))

    def subtotal(self) -> float:
        return sum(item.total() for item in self.items)
