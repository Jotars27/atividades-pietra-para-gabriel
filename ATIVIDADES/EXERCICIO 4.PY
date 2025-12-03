cesta_de_frutas = ("maçã", "banana", "uva", "morango", "laranja", "abacaxi", "manga", "kiwi")

print("="*120)
print("\n==== Lista com 8 frutas ====")
fruta = input("Digite o nome da fruta que você procura: ").title()
print("="*120)

if fruta.lower() in cesta_de_frutas:
    print(f"\nA fruta {fruta} está na cesta de frutas.")
    
else:
    print(f"A fruta {fruta} não foi encontarada!")