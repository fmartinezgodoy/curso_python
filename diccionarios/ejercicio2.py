user = {}

user["name"] = input("Ingrese su nombre: ")
user["age"] = input("Ingrese su edad: ")
user["address"] = input("Ingrese su dirección: ")
user["phone"] = input("Ingrese su número de teléfono: ")

message = (
      "{} tiene {} años, vive en {} y su número de teléfono es {}."
            .format(
                  user.get("name"), 
                  user.get("age"),
                  user.get("address"), 
                  user.get("phone")
            )
)

print(message)
