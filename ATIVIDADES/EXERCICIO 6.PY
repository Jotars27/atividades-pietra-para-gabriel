numeros_inteiro = [35, 7, 12, 21, 41, 56, 68, 59, 74, 92]
print("="*80)
print("\n=== Encontrando número e posição na tupla ====")
numero = int(input("Digite um número para ver se está na tupla: "))

if numero in numeros_inteiro:
 posicao_indice = numeros_inteiro.index(numero)+ 1 
 print(f"Todos números da lista são {numeros_inteiro}.")
 print(f"O número {numero} está na lista.")
 print(f"O número {numero} está na posição (indice): {posicao_indice} da tupla.")
else:
  print("Número não encontrado!") 
  print(f"Todos números da lista são {numeros_inteiro }.") 
  print("="*80)