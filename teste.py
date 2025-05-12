from main import analisar_numeros

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

media, maior, menor, pares = analisar_numeros(numeros)

print(f"Média: {media:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Quantidade de números pares: {pares}")
