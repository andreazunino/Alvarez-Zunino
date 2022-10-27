"""También debe permitir almacenar nuevas canciones a la lista."""



def NuevaCancion (lista):
   
    nuevaCancion = input("Ingresar nombre de la nueva cancion: ")
    lista[len(lista):] = [nuevaCancion]
    print (lista)
    
    
"""def nuevaCancion(listaCanciones, cancionNueva):  #a lista agregale el elemento
    cancionNueva=input ("ingrese nueva cancion: ")
    listaCanciones.append (cancionNueva)
    print (listaCanciones)"""
    
 