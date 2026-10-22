import pytest

from app.cart import Cart


def test_aplica_desconto_de_10_porcento_quando_subtotal_igual_a_200():
	cart = Cart()
	cart.add_item(price=100, quantity=2)

	assert cart.discount() == pytest.approx(20)
	assert cart.total() == pytest.approx(180)


def test_aplica_desconto_de_10_porcento_quando_subtotal_acima_de_200():
	cart = Cart()
	cart.add_item(price=50, quantity=3)
	cart.add_item(price=25, quantity=4)

	assert cart.discount() == pytest.approx(25)
	assert cart.total() == pytest.approx(225)


def test_nao_aplica_desconto_quando_subtotal_abaixo_de_200():
	cart = Cart()
	cart.add_item(price=199.99, quantity=1)

	assert cart.discount() == 0
	assert cart.total() == pytest.approx(199.99)
