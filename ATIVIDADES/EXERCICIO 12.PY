print("="*120)
print("=== CADASTRO DE PESSOAS ===")
def cadastrar_pessoa(): 
    nome = input("Digite o nome: ").title()
    idade = int(input("Digite a idade: "))
    cidade = input("Digite o nome da cidade: ").title()

    cadastro = {
     "idade": idade,
     "cidade": cidade

     }
    return cadastro

lista_cadastro = [] 


while True:
    cadastro = cadastrar_pessoa() 
    lista_cadastro.append(cadastro) 
    sair = input("Para encerrar digite a palavra (Sair) ou ENTER para continuar:").lower() 
    print("-"*90)
    if sair == 'sair':
        print("Encerrando os cadastros de nomes no sistema!\n")
        break
    print("="*120)

print("==== CADASTROS DE NOMES ====\n")
for i in range(len(lista_cadastro)):
    pessoa = lista_cadastro[i]
    print("-"*120)
    print(f"{i+1}º Cadastro:\nNome: {pessoa['nome']}. \nIdade: {pessoa['idade']}. \nCidade: {pessoa['cidade']}.\n\n")
    print("==== NOVO CADASTRO ====")







