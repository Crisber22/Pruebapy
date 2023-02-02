nombres=[]
apellidos=[]
numeros=[]


def  recop_nombre ():
    nombre = input("Dige su nombre:")
    return nombre 


def  recop_apellido ():
    apellido = input("Dige su apellido:")
    return apellido     
    

def  recop_numero ():
    numero = input("Dige su numero:")
    return numero  


def savelist (): 
    nombres.append (recop_nombre())
    apellidos.append (recop_apellido())
    numeros.append(recop_numero())

#--------------------------------------#

opcion = 0 
while (opcion !=3):
    opcion= int(input("Escoja una opcion. \n 1.Inresar Data \n 2.Imprimnir Listas \n 3.Finalizar Programa."))
    if (opcion == 1):
        savelist()
    if (opcion == 2):
        print (nombres, apellidos, numeros)
    if (opcion == 3):
        print ("Gracias por usar el programa")

print ("probando el git")