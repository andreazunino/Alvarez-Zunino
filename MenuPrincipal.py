from AgregarCancion import NuevaCancion
from BuscarCancion import buscarCancion
from ModificarCancion import modificacionCantante



cancion1 ={"Titulo": "Titi me pregunto", "Cantante":"Bud Bunny", "Letra":"Ey, Tití me preguntó " 
           "Si tengo muchas novia " 
           "Muchas novia "
           "Hoy tengo a una, mañana otra "
           "Ey, pero no hay boda" }
cancion2 ={"Titulo": "Despecha", "Cantante":"Rosalia", "Letra":"Baby, no me llame "
            "Que yo estoy ocupá olvidando tus male "
            "Ya decidí que esta noche se sale "
            "Con toa mis motomami, con toda mis gyales "}
cancion3 ={"Titulo": "Quedate", "Cantante":"Quevedo", "Letra":"Y nos fuimos en una "
            "Empezamo a la una "
            "Y con la nota rápido"
            "Nos dieron las tre"
            "Perreamos toda la noche"
            "Y nos dormimo a las die"}
cancion4 = {"Titulo": "Tu y yo", "Cantante" : "La konga" , "Letra": "Tú y yo "
            "Pasamos de ser todo a nada"
            "De comernos con la mirada"
            "Y ahora estamos frente a frente"
            "Y ni siquiera puedes mirarme a la cara"}
cancion5 = {"Titulo": "No se olvida", "Cantante": "Wisin y Yandel", "Letra":"Dime que es mentira "
            "Que ya no piensas en mí"
            "Aunque él te dé todo"
            "No te vas a enamorar"}

listaCanciones = [cancion1, cancion2, cancion3, cancion4, cancion5]



def textoMenu():
    print("Si quiere AGREGAR una cancion, ingresar 1")
    print("Si quiere BUSCAR una cancion, ingresar 2")
    print("Si quiere MODIFICAR el nombre de un cantante, ingrear 3")
    print("Si quiere SALIR del menu, ingrese otro valor")
    elecUser = int(input())
    if elecUser == 1:
        NuevaCancion(listaCanciones)
    elif elecUser == 2:
        buscarCancion(listaCanciones)
    elif elecUser == 3:
        modificacionCantante(listaCanciones)
    else:
        print ("Salir del menu") 
#print ("eligio", textoMenu()) 

textoMenu()