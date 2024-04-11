num = int(input("Digite Um Numero Positivo: "))
if num > 0:
    print(f"Divisores de {num}:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
else:
    print("Por Favor Digite Um Numero Positivo.")