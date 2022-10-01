
imprimirPersona = lambda nombre, edad, ocupacion: { nombre, edad, ocupacion }

nombre = input('Digite su nombre: ')
edad = int(input('Digite su edad: '))
ocupacion = input('Digite su ocupación: ')

resultado = imprimirPersona(nombre, edad, ocupacion)

print(resultado)