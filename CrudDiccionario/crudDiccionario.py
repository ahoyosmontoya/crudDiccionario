misDatos = {
    'lugarNacimiento': 'urrao',
    'name': 'Alexander',
    'last_name': 'Hoyos',
    'age': 50
}

print(misDatos)

#el tamanio del diccionario
print(len(misDatos))

#imprimiendo una llave 
print(misDatos['age'])

print('name' in misDatos)
print('other' in misDatos)
# Borrar la clave 'age'
del misDatos['age']

print(misDatos)
# Añadir una nueva clave y valor
misDatos['estudios'] = 'programación'

print(misDatos)
