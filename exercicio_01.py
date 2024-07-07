# Calcular Média de Valores em uma Lista

minha_lista: list = [15, 500, 375, 57, 98]

def calcular_a_media_de_uma_lista_de_valores(lista: list)-> float:
    media_valores = sum(lista) / len(lista)
    return media_valores

resultado = calcular_a_media_de_uma_lista_de_valores(minha_lista)

print(resultado)