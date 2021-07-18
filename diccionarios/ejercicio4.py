months = {
    1:'Enero',
    2:'Febrero', 
    3:'Marzo', 
    4:'Abril', 
    5:'Mayo', 
    6:'Junio', 
    7:'Julio', 
    8:'Agosto', 
    9:'Septiembre', 
    10:'Octubre', 
    11:'Noviembre', 
    12:'Diciembre'
}

date = input("Ingrese la fecha en formato dd/mm/aaaa: ").split("/")

print(
    "{} de {} de {}"
        .format(
            date[0],
            months[
                int(
                    date[1]
                )
            ],
            date[2]
        )
)
