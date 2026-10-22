from dataclasses import dataclass


@dataclass
class Item:
    price: float
    quantity: int
# Aplicação do Refactor
    def total(self) -> float:
        return self.price * self.quantity


class Cart:
    DISCOUNT_THRESHOLD = 200.0
    DISCOUNT_RATE = 0.10

    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, price: float, quantity: int) -> None:
        self.items.append(Item(price, quantity))

    def subtotal(self) -> float:
        return sum(item.total() for item in self.items)

    def discount(self) -> float:
        subtotal = self.subtotal()
        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE
        return 0.0

    def total(self) -> float:
        return self.subtotal() - self.discount()
