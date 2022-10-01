numeros = [12, 4, 5, 7, 9]

numerosMayores = lambda numero : numero > 10

for numero in numeros:
    if (numerosMayores( numero )):
        print(f'El numero { numero } es mayor que 10')
    else:
        print(f'El numero { numero } es menor que 10')