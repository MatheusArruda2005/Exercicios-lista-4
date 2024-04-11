pares = 0 
impares = 0
for i in range(10):
    Num = int(input("Digite Um Numero: "))
    if Num % 2 == 0:
        pares += 1
    else: 
        impares += 1
print(f"\nQuantidade De Numeros Impares: {impares}\n")
print(f"\nQuantidade De Numeros Pares: {pares}\n")