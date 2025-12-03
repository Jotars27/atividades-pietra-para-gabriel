print("="*120)
print("=== Preencha o formulario a seguir ===")
nome = input("Digite o nome: ").title()
idade = int(input("Digite a idade: "))
curso = input("Digite o nome da cidade: ").title()

dicionario = {
     "nome": nome,
     "idade": idade,
     "curso": curso

     }
print("="*120)
print("Dados Digitados")
print(f"Nome: {dicionario['nome']}.\nIdade: {dicionario['idade']}.\nCurso: {dicionario['curso']}")
print("="*120)
print("Dados dentro do dicionario")
print(f"{dicionario['nome']}. {dicionario['idade']}. {dicionario['curso']}")