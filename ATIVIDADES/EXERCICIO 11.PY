print("="*90)
print("==== Calculando notas e mostrando a mésia ====")
lista_notas = []
def informa_nota():
  for i in range(4):
   notas = float(input(f"Didite a {i+1}ª nota: "))
   lista_notas.append(notas)
informa_nota () 

def media_nota(lista_notas):
    soma = sum(lista_notas)
    quantidade = len(lista_notas)
    media = soma / quantidade 
    print(f"As notas digitadas foram: {lista_notas} ")
    print (f"A média das notas é: {media}.")
                
media_nota(lista_notas)