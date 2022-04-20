if __name__ == "__main__":  
    main = int(input("Que ejercicio deseas realizar(1,2 o 3):"))
    if main == 1:
        from Clases.ejercicio import *
        mostrar_ok = Mostrar('"OK"') 
        mostrar_ko = Mostrar('"KO"') 
        alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
        bloque_alternativa = Bloque() 
        bloque_alternativa.agregarInstruction(alternativa) 
        bucle = MientrasQue(True, bloque_alternativa)
    if main == 2:
        from Clases.ejercicio2 import *
        linea1 = input("Introduzca la primera linea del archivo:")
        linea2 = input("Introduce la segunda linea del archivo:")
        datos = Entrada(linea1,linea2)
        datosMy = Mayuscula(datos)
    if main == 3:
        from Clases.ejercicio3 import *
        Naturaleza = Naturaleza()

        producto = Producto(Naturaleza.ALIMENTARIA)
        precio_con_impuestos = Factory.crear(producto).facturar()
        print(precio_con_impuestos)
        
        producto = Producto(Naturaleza.SERVICIO)
        precio_con_impuestos = Factory.crear(producto).facturar()
        print(precio_con_impuestos)