def analisar_numeros(lista):
    if not lista:
        return "A lista não pode estar vazia"
    
    media = sum(lista) / len(lista)        
    maior = max(lista)                     
    menor = min(lista)                    
    pares = len([n for n in lista if n % 2 == 0])  

    return media, maior, menor, pares
