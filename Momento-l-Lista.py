# Alumno: Hernandez Agudelo Esteban


catalogo = []


catalogo.append('World of Warcraft')
catalogo.append('Lost Ark') 
catalogo.append('Smite')
catalogo.append('Elden Ring') 

indice = 4

respuesta = 1


    
while (respuesta==1) :
   respuestaOperacion = int(input('Digite la operacion que quiere realizar \n 1 Crear \n 2 Consultar \n 3 Actualizar \n 4 Eliminar \n : '))
   if respuestaOperacion== 1 :
        respuestaNuevo = input('¿Que valor quiere ingresar? ') 
        indice=indice+1
        catalogo[indice]=respuestaNuevo
        print(f"Nuevo valor agregado al diccionario ")
        print({catalogo.index(respuestaNuevo)})
        
   elif respuestaOperacion==2 :
        respuestaBuscar = input('Que valor quiere buscar: ')
        if respuestaBuscar in catalogo:
            print("Valor encontrado en el catalogo")
            print(catalogo.index(respuestaBuscar))       
        else:
            print("Ese valor no existe en el diccionario")
   elif respuestaOperacion==3 :
        respuestaReemplazar = input('¿Que campo desea reemplazar? ')
        if respuestaReemplazar in catalogo:
            respuestaReemplazo = input('¿Por cual valor desea reemplazarlo? ')
            catalogo[respuestaReemplazar]=respuestaReemplazo
        else:
            print('Ese valor no existe en el catalogo')
   elif respuestaOperacion==4 :
        respuestaEliminar = input('¿Que valor desea eliminar? ')
        if respuestaEliminar in catalogo:
            catalogo.pop(respuestaEliminar)
        else:
            print('Ese valor no existe en el catalogo')
   respuestaReingreso= int(input('¿Desea hacer otra operacion en el catalogo? 1 para si, 2 para no')) 
    
   if respuestaReingreso==1:
       respuesta=1
   else :
       print("Saliendo del programa...")
       respuesta=2
            
print(catalogo)
