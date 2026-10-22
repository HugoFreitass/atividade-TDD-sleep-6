from app.cart import Cart


def test_subtotal_soma_preco_de_cada_produto_multiplicado_pela_quantidade():
	cart = Cart()
	cart.add_item(price=10, quantity=2)
	cart.add_item(price=5, quantity=3)

	assert cart.subtotal() == 35
