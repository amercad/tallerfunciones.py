def clasificar(numero):
    return numero % 2 == 0


clasificar2 = lambda numero : numero & 2 == 0


numero = 100

print(clasificar(numero))
print(clasificar2(numero))


if (clasificar2(numero)):
    print(f'El numero { numero } es par')
else:
    print(f'El numero { numero } es impar')