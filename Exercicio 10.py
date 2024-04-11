lista = [2,4,7,2,3,3,1,0,2,6]
ocorrencias = {}
for numero in lista:
    if numero in ocorrencias:
        ocorrencias[numero] += 1
    else:
        ocorrencias[numero] = 1
        numeroMaisRepetido = None
maiorOcorrencia = 0
for numero, quantidade in ocorrencias.items():
    if quantidade > maiorOcorrencia:
        numeroMaisRepetido = numero
        maiorOcorrencia = quantidade
print(f"O Numero Que Se Repete Mais Vezes É: {numeroMaisRepetido}")