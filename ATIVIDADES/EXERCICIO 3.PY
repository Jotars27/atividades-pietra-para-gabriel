nomes = ()
print("="*120)
print("\n==== DIGITE OS NOMES QUE DESEJA ADICIONAR A LISTA E (sair) PARA ENCERRAR ====")
while True:
 
    cadastro = input("Digite o nome desejado: ").title()# .title() irá colocar as primeiras letras de cada palavra maiuscula

    if cadastro.lower() == 'sair': #.lower() irá colocar todas as letras em minuscula 
      print("Saindo do sistema! Até logo.")
      break
    nomes.append(cadastro)

print(f"Foram adicionaddos {len(cadastro)} nomes.")
print(f"Os nomes digitados foram {nomes}.\n")