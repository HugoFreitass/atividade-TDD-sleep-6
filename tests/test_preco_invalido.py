import pytest
from app.cart import Cart

def test_preco_negativo() -> None:
    cart = Cart()

    with pytest.raises(ValueError, match="Preco não pode ser negativo"):
        cart.add_item(-50.00, 1)