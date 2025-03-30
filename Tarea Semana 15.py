# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Fernando Caicedo",
    "edad": 41,
    "ciudad": "Cuenca",
    "profesion": "Albañil"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor para "telefono" si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0933903757"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)