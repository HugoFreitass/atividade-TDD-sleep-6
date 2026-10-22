import pytest
from app.cart import Cart


def test_carrinho_vazio() -> None:
    cart = Cart()

    assert cart.total() == 0.0