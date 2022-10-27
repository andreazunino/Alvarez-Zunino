"""Por otro lado debe dar la posibilidad de buscar una canción por su nombre y en caso que la
encuentre mostrar sus datos por pantalla, en caso de no encontrarse debe indicar que la
canción no se halla en la lista."""



def buscarCancion (listaCanciones):
    buscoCancion = input("Ingrese el nombre de la cancion que desea buscar: ")

    #for buscarCancion in listaCanciones:
    def imprimirCancion (cancion):
        print ("El nombre es:", cancion ["Titulo"]) 
        print ("El cantante es:", cancion ["Cantante"]) 
        print ("La letra es:", cancion ["Letra"])         
    #for buscarCancion in range(len(listaCanciones)):
       #if buscarCancion ["Titulo"] == buscarCancion:
      # print (listaCanciones.index(listaCanciones))
    
    for cancion in listaCanciones:
        if cancion ["Titulo"] == buscoCancion:
            imprimirCancion (cancion)
            #print ("encontrado")
            return
    print ("no encontrado")
    
#BuscarCancion(listaCanciones)
# listaCanciones.index(buscarCancion)
    