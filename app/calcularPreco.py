def calculate_price(produtos: list[tuple[int, int]]) -> float:
    """
    Calcula o preço total dos produtos no carrinho.

    produto = (preço, quantidade).
    """
    if not produtos:
        return 0.0
    
    for [price, quantidade] in produtos:
        if(price < 0):
            raise ValueError("Preco não pode ser negativo")
        if(quantidade < 1):
            raise ValueError("Quantidade deve ser maior que 0")



    return -1.0  # Falhou
