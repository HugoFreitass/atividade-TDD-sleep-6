def calculate_price(produtos: list[tuple[int, int]]) -> float:
    """
    Calcula o preço total dos produtos no carrinho.

    produto = (preço, quantidade).
    """
    if not produtos:
        return 0.0

    return -1.0  # Falhou
