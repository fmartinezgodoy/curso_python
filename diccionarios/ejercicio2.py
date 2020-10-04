datos_usuario = {"nombre" : "n/a", "edad" : "n/a", "direccion" : "n/a", "numero" : "n/a"}

datos_usuario["nombre"] = input("Ingrese su nombre: ")
datos_usuario["edad"] = input("Ingrese su edad: ")
datos_usuario["direccion"] = input("Ingrese su dirección: ")
datos_usuario["numero"] = input("Ingrese su número de teléfono: ")
print("{} tiene {} años, vive en {} "
      "y su número de teléfono es {}."
      .format(datos_usuario.get("nombre"), datos_usuario.get("edad"),
              datos_usuario.get("direccion"), datos_usuario.get("numero")))
