matriz = [[], [], []]
somapar = maior = somacoluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f"Digite um valor para [{linha},{coluna}]: ")))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos pares da matriz foi de {somapar}')

for linha in range(0, 3):
    somacoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna foi {somacoluna}')

for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[linha][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor encontrado na segunda linha foi o {maior}')
