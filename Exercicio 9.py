
numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1} número inteiro: "))
    numeros.append(numero)
numerosOrdenados = sorted(numeros)
print(f"Números em ordem crescente: {numerosOrdenados}")
