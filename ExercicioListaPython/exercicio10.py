'''
par ou impar
'''

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

resultado = verificar_par_ou_impar(7)
print(f"O número 7 é {resultado}.")
