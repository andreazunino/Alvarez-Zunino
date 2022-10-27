
def modificacionCantante(listaCanciones):
    cantanteBuscado= input ("Ingrese el cantante que desea buscar: ")    
    encontradoEn =-1 
    
    for i in range (len(listaCanciones)):    
        if (listaCanciones[i]["Cantante"] == cantanteBuscado): 
            encontradoEn = i
    
    if encontradoEn != -1:
        nuevoCantante = input("Ingrese el nuevo nombre de cantante: ")
        listaCanciones[encontradoEn]["Cantante"] = nuevoCantante
        print ("Esta es la nueva lista de canciones: ", listaCanciones)
    else:
        print ("El nombre del cantante NO esta en la lista actual")