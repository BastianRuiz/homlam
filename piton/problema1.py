#realizar un programa de ventas para una empresa tecnologica en la cual
#tiene 8 categorias de producto, en la primera tienen monitor, en la 
#segunda placa madre, en la tercera procesadores, en la cuarta memoria RAM,
#quinta disco duro, sexta fuente de poder y septima gavinete y en la octava
#tarjeta grafica

#en los monitores hay 2 tipos, 60hrz o 144 hrz
#en la placa madre busque los sockets de 13 gen intel y amd
#en la ram es ddr5
#en los discos duros hdd 500gb, 1tb, 2tb, y ssd de 256 gb y 500gb 
#fuente de poder de bronce, oro y blanca 
#grafica amd o nvidia 

opcion=0


while(opcion>=1 & opcion<=8) :

    print("bienvenido a nuestra tienda mipiton")
    print("nuestros productos son: ")
    print("1.-monitor")
    print("2.-placa madre")
    print("3.-procesador")
    print("4.-memoria RAM") 
    print("5.-disco duro")
    print("6.-fuente de poder")
    print("7.-gavinete")
    print("8.-tarjeta grafica")
    print("9.-compra")

    opcion=int(input("ingresar opcion: "))

    match opcion :
 

        case 1 :

            print("¿cual monitor va a querer?")
            monitor=int (input ("¿60hrz o 144hrz?: "))
            if(monitor==60) :
                print("usted eligue el monitor 60hrz")
            elif(monitor==144):
                print("usted eligue el monitor 144hrz")
        

            print("¿desea volver al inicio?: ")
            Inicio=int (input("seleccione 1 si quiere regresar a inicio o seleccionar 2 si desea comprar:  "))
            if(Inicio==1) : 
                Inicio==opcion

            

            elif(Inicio==2) :
                compra=int (input("eliga metodo de compra, seleccione 1 si desea pagar con efectivo, o seleccione 2 si desea pagar con tarjeta: "))
    
                if(compra==1) :
                    print("usted a pagado con efectivo")       
                    break
                elif(compra==2) :
                 print("usted a pagado con tarjeta, por ende se le aplicara un 15% de descuento")

            print("¿desea volver al inicio?: ")
            Inicio=int (input("seleccione 1 si quiere regresar a inicio o seleccionar 2 si desea comprar:  "))
            
            

        
        


        case 2 :

            print("¿cual placa madre va querer?")
            PlacaMadre=int (input ("¿Intel core i9 13900K Socket 1700 o Chipset AMD X570? :"))
            if (PlacaMadre==1) :
             print("usted eligue el Intel core i9 13900K Socket 1700")
            elif(PlacaMadre==2) :
             
             print("usted eligue el Chipset AMD X570")

            print("¿desea volver al inicio?: ")
            Inicio=int (input("seleccione 1 si quiere regresar a inicio o seleccionar 2 si desea comprar:  "))
            if(Inicio==1) : 
                Inicio==opcion

            

            elif(Inicio==2) :
                compra=int (input("eliga metodo de compra, seleccione 1 si desea pagar con efectivo, o seleccione 2 si desea pagar con tarjeta: "))
    
                if(compra==1) :
                    print("usted a pagado con efectivo")       
                    break
                elif(compra==2) :
                 print("usted a pagado con tarjeta, por ende se le aplicara un 15% de descuento")

            print("¿desea volver al inicio?: ")
            Inicio=int (input("seleccione 1 si quiere regresar a inicio o seleccionar 2 si desea comprar:  "))
            
            

        case 3 :
            print("nuestra memoria RAM es ddr5")
            ram=int (input("¿va a querer la memoria RAM? seleccione 1 si desea la memoria RAM o 2 si es que no: "))
            if(ram==1) :
             print("usted eligue memoria RAM")
            elif(ram==2) :
               print("compra cancelada")

            elif(Inicio==2) :
                compra=int (input("eliga metodo de compra, seleccione 1 si desea pagar con efectivo, o seleccione 2 si desea pagar con tarjeta: "))
    
                if(compra==1) :
                    print("usted a pagado con efectivo")       
                    break
                elif(compra==2) :
                 print("usted a pagado con tarjeta, por ende se le aplicara un 15% de descuento")

            print("¿desea volver al inicio?: ")
            Inicio=int (input("seleccione 1 si quiere regresar a inicio o seleccionar 2 si desea comprar:  "))
            
            



        case 4 :
            print("¿cual disco duro va a querer?")
            Discoduro=int (input("seleccione 1 si quiere hdd 500gb, 2 si quiere hdd 1tb, 3 si quiere hdd 2tb, 4 s i quiere sdd 256gb o 5 si quiere ssd 500gb: "))
            if (Discoduro==1) :
               print("usted eligue disco duro hdd 500gb")

            elif(Discoduro==2) :
               print("usted eligue disco duro hdd 1tb")

            elif(Discoduro==3) :
               print("usted eligue disco duro hdd 2tb") 

            elif(Discoduro==4) :
               print("usted eligue ssd 256gb")  

            elif(Discoduro==5) :
               print("usted eligue ssd 500gb")   

            elif(Inicio==2) :
                compra=int (input("eliga metodo de compra, seleccione 1 si desea pagar con efectivo, o seleccione 2 si desea pagar con tarjeta: "))
    
                if(compra==1) :
                    print("usted a pagado con efectivo")       
                    break
                elif(compra==2) :
                 print("usted a pagado con tarjeta, por ende se le aplicara un 15% de descuento")

            print("¿desea volver al inicio?: ")
            Inicio=int (input("seleccione 1 si quiere regresar a inicio o seleccionar 2 si es que no:  "))
            
            





        case 5 :
          print("¿cual fuente de poder va querer?")
          Fuentepoder=int (input("seleccione 1 si desea de bronce, 2 si desea de oro, o 3 si desea de blanca: "))
          if (Fuentepoder==1) :
           input("usted eligue fuente de poder de bronce")

          elif (Fuentepoder==2) :
             input("usted eligue fuente de poder de oro")

          elif(Fuentepoder==3) :
             input("usted eligue fuente de poder de blanca")

          elif(Inicio==2) :
                compra=int (input("eliga metodo de compra, seleccione 1 si desea pagar con efectivo, o seleccione 2 si desea pagar con tarjeta: "))
    
                if(compra==1) :
                    print("usted a pagado con efectivo")       
                    break
                elif(compra==2) :
                 print("usted a pagado con tarjeta, por ende se le aplicara un 15% de descuento")

                print("¿desea volver al inicio?: ")
                Inicio=int (input("seleccione 1 si quiere regresar a inicio o 2 si es que no:  "))
          elif(Inicio==2) :
                print("usted se quedara aqui para siempre")
            
            
        case 9:
            compra=int (input("eliga metodo de compra, seleccione 1 si desea pagar con efectivo, o seleccione 2 si desea pagar con tarjeta: "))
    
            if(compra==1):
                print("usted a pagado con efectivo")       
            elif(compra==2):
                print("usted a pagado con tarjeta, por ende se le aplicara un 15% de descuento")
                print("¿desea volver al inicio?: ")
                Inicio=int (input("seleccione 1 si quiere regresar a inicio o 2 si es que no:  "))
            elif(Inicio==2) :
                print("usted se quedara aqui para siempre")
           
    


               
            
          


            

                



