'''
media das notas
'''
def calcular_media(notas):
    return sum(notas) / len(notas)

notas = [8.5, 9.0, 7.5]
media = calcular_media(notas)
print(f"A média é {media:.2f}.")
