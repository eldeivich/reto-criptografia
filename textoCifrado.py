abecedario = 'abcdefghijklmnñopqrstuvwxyz'
abecedarioMay = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
numeros = '1234567890'

vocalesAc = 'áéíóú'
vocales = 'aeiou'
trans = str.maketrans(vocalesAc, vocales)

textoS = input("Introduzca el texto: ")
texto = ''
texto = textoS.translate(trans)

valorDesp = int(input("Introduzca el valor de desplazamiento: "))
cifrad = ''
for contar in texto:
    if contar in abecedario:
        cifrad += abecedario[(abecedario.index(contar) + valorDesp)%(len(abecedario))]
    elif contar in abecedarioMay:
        cifrad += abecedarioMay[(abecedarioMay.index(contar) + valorDesp)%(len(abecedarioMay))]
    elif contar in numeros:
        cifrad += numeros[(numeros.index(contar) + valorDesp)%(len(numeros))]
    else:
        cifrad += contar

cifrac = ''
for descontar in cifrad:
    if descontar in abecedario:
        cifrac += abecedario[(abecedario.index(descontar) - valorDesp)%(len(abecedario))]
    elif descontar in abecedarioMay:
        cifrac += abecedarioMay[(abecedarioMay.index(descontar) - valorDesp)%(len(abecedarioMay))]
    elif descontar in numeros:
        cifrac += numeros[(numeros.index(descontar) - valorDesp)%(len(numeros))]
    else:
        cifrac += descontar

print("El texto cifrado con valor de desplazamiento de {} es: {}".format(valorDesp, cifrad))
print("Se vuelve a descifrar el texto: {}".format(cifrac))