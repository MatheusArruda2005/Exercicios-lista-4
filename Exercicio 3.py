while True:
 num = int(input("Digite Um Numero De 1 a 10: "))
 if 1 <= num <= 10:
    print(f"Tabuada Do Numero: {num}")
    for i in range(1,11):
        print(num, "X", i, "=", num * i)
 if num > 10 or num < 0:
  print("Insira um numero valido\n")
  continue
       
