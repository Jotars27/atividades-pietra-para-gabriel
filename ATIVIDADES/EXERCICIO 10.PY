print("="*90)
print("\n==== Função de Saudação Personalizada ====")

def saudar(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")
    
for i in range(3):
     usuario = input(f"Digite o {i+1}° nome: ").title().strip()
     saudar(usuario)