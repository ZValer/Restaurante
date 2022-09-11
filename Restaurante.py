
"""
Programa para restaurantes

"""
def propinaCalc(porcentaje, cuenta):
    print ("Con propina de: ", porcentaje, "%")
    print ("Su cuenta Total es: $", cuenta*(1+(porcentaje/100)))
    
    
def main ():
    
    print ("Bienvenidos")
    print ("Restaurante Itálico\n")
    
    print ("Menú")
 #Colocar platillos y precios
    for contador in range (25):
        print ("_", end="")
        
    print ("\n\n1. Pizza $300")
    print ("2. Pasta $200")
    print ("3. Ensalada $100")
    print ("4. Ravioles $250")
    
    for contador in range (25):
        print ("_", end="")
        
    cuenta=0
    x=""
    
    while x!="no":
        x=str(input("\n¿Desea agregar un platillo? (si/no): "))
        
        if x=="si":
            num=int(input("Introduce el número de platillo: "))
            if num==1:
                cuenta+=300
            elif num==2:
                cuenta+=200
            elif num==3:
                cuenta+=100
            elif num==4:
                cuenta+=250
                
        elif x!="si" and x!="no":
            print ("Opción no válida, vuelva a intentarlo")
            
    
    print ("\n\n Su cuenta total es de: $", cuenta)
    propina=float(input("\n¿Qué porcentaje de propina desea agregar?: "))
    propinaCalc(propina, cuenta)
    
    
    
    

main()