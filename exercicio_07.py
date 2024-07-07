valor_1 = 4
valor_2 = 6

def somar_valores(valor_1_para_somar: float , valor_2_para_somar: float)-> float: 
    
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    
    return resultado_da_soma

soma_valores_1_e_2 = somar_valores(valor_1, valor_2)

print(soma_valores_1_e_2)