# Filtrar Dados Acima de um Limite

minha_lista: list = [15, 44, 60.8, 99, 275, 500, 813, 1075 ]

limite: float = 500

def filtrar_valores_acima_do_limite(valores: list, valor_do_limite: float) -> float:
    resultado = []
    for valor in valores:
     if valor < valor_do_limite:
      resultado.append(valor)
    return resultado

print(filtrar_valores_acima_do_limite(minha_lista, limite))
