# Contar Valores Únicos em uma Lista

minha_lista = [1, 1, 3, 8, 16, 16, 19.99, 19.99, 50, 45, 45]

def contar_valores_distintos(lista: list) -> float: 
    resultado = []
    nova_lista = len(set(lista))
    resultado.append(nova_lista)

    return resultado

print(contar_valores_distintos(minha_lista))