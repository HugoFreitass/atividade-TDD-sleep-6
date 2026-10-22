import pytest
from app.calcularPreco import calculate_price


def test_carrinho_vazio() -> None:
    produtos: list[tuple[int, int]] = []

    assert calculate_price(produtos) == 0.0

def test_preco_negativo() -> None:
    produtos: list[tuple[int, int]] = []
    produtos.append([-50.00, 1])

    with pytest.raises(ValueError, match="Preco não pode ser negativo"):
        calculate_price(produtos)

def test_quantidade_invalida() -> None:
    produtos: list[tuple[int, int]] = []
    produtos.append([50.00, 1])
    produtos.append([150.00, 0])
    produtos.append([250.00, -1])

    with pytest.raises(ValueError, match="Quantidade deve ser maior que 0"):
        calculate_price(produtos)