
dentroIntervalo = 0
foraIntervalo = 0
for i in range(10):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        dentroIntervalo += 1
    else:
        foraIntervalo += 1
print(f"Quantidade de números dentro do intervalo [10, 20]: {dentroIntervalo}")
print(f"Quantidade de números fora do intervalo [10, 20]: {foraIntervalo}")
