import pytest
from app.cart import Cart

def test_quantidade_invalida() -> None:
    cart = Cart()

    with pytest.raises(ValueError, match="Quantidade deve ser maior que 0"):
        cart.add_item(150.00, 0)