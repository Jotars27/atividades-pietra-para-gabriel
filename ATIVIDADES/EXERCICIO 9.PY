mercado = {
    "Arroz": 5.99,
    "Feijão": 7.49,
    "Macarrão": 4.29
}

print("="*120)
print("=== Produtos do Mercado ===")
produto = input("Digite o nome do produto desejado: ").title()
if produto in mercado:
    preco = mercado[produto]
    print(f"Temos o produto: {produto} e está por: R${preco} reais.")
else:
    print("Produto nao encontrado!")