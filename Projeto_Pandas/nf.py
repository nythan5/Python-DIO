def calcular_custo_compra(quantidade_itens):
    custo_total = 0  # Inicializa o custo total como zero

    # Define as faixas e os respectivos custos por item
    faixas = [(12000, 16.83), (10000, 3.54), (10000, 3.47), (10000, 3.4), (10000, 3.36), (1000000, 3.36)]

    for faixa, custo_por_item in faixas:
        if quantidade_itens > faixa:
            custo_total += faixa * custo_por_item  # Adiciona o custo da faixa completa
            quantidade_itens -= faixa  # Atualiza a quantidade de itens restantes
        else:
            custo_total += quantidade_itens * custo_por_item  # Adiciona o custo da quantidade restante na faixa
            quantidade_itens = 0  # Define a quantidade restante como zero, pois todos os itens foram cobrados

    # Cobrar 3,33 para quantidades acima da última faixa
    custo_total += quantidade_itens * 3.33

    return custo_total

# Exemplo de uso
quantidade_itens = 280000  # Altere a quantidade de itens conforme necessário
custo = calcular_custo_compra(quantidade_itens)
print(f'O custo da compra de {quantidade_itens} itens é R${custo:.2f}')
