from app.calcularPreco import calculate_price


def test_carrinho_vazio_retorna_zero() -> None:
    produtos: list[tuple[int, int]] = []

    assert calculate_price(produtos) == 0.0
