opciones_menu = {
    "1": "2d",
    "2d": "2d",
    "2": "3d",
    "3d": "3d",
    "3": "salir",
    "s": "salir",
    "salir": "salir"
}

figuras = {
    "2d":{
        "1": "cuadrilatero",
        "cuadrilatero": "cuadrilatero",
        "2": "circulo",
        "circulo": "circulo",
        "3": "triangulo",
        "triangulo": "triangulo",
        "4":"triangulo rectangulo",
        "triangulo rectangulo": "triangulo rectangulo",
        "5":"salir",
        "salir":"salir"
    },
    "3d": {
        "1": "cubo",
        "cubo": "cubo",
        "2": "tetraedro",
        "tetraedro":"tetraedro",
        "3": "esfera",
        "esfera": "esfera",
        "4":"salir",
        "salir":"salir"
    },
    "salir":{
        "salir":"salir"
    }
}


pi = 3.141592653589793

print("Bienvenido a la calculadora.")

salir_programa = 0
while salir_programa == 0:

    print("Lista de opciones:\n1.Figuras 2D\n2.Figuras 3D\n3.Salir")

    menu = input("Seleccione la opcion: ")
            
    if menu in opciones_menu:
        menu = opciones_menu[menu]
        
        if menu == "2d":
            salir_2d = 0
            while salir_2d == 0:
                print("Lista de figuras 2D:\n1.Cuadrilatero\n2.Circulo\n3.Triangulo\n4.Triangulo rectangulo\n5.Salir")
                eleccion = input("Seleccione la figura: ")
                
                if eleccion in figuras[menu]:
                    eleccion = figuras[menu][eleccion]
                    
                    if eleccion == "cuadrilatero":
                        check = input("Es un cuadrilatero equilatero? (S/N): ").lower().strip()
                        if check == "s":
                            lado = float(input("Ingrese la longitud de un lado del cuadrado (Permite decimales): "))
                            area = lado**2
                            perimetro = lado*4
                            diagonal = lado * (2**(1/2))
                            print(f"Calculos realizados (Cuadrado de lado {lado}m):\n1.Area: {area}m²\n2.Perimetro: {perimetro}m\n3.Diagonal del cuadrado: {diagonal}m")
                        if check == "n":
                            base = float(input("Ingrese la base del rectangulo (Permite decimales): "))
                            altura = float(input("Ingrese la altura del rectangulo (Permite decimales): "))
                            area = base * altura
                            perimetro = (base * 2) + (altura * 2)
                            diagonal = ((base**2)+(altura**2))**(1/2)
                            print(f"Calculos realizados (Rectangulo de base {base}m, y altura {altura}m):\n1.Area: {area}m²\n2.Perimetro: {perimetro}m\n3.Diagonal del rectangulo: {diagonal}m")
                    
                    elif eleccion == "circulo":
                        radio = float(input("Ingrese el radio del circulo (Permite decimales): "))
                        area = pi*(radio**2)
                        circunferencia = 2*pi*radio
                        diametro = radio * 2
                        print(f"Calculos realizados (Circulo de radio {radio}m):\n1.Area: {area}m²\n2.Circunferencia: {circunferencia}m\n3.Diametro: {diametro}m")

                    elif eleccion == "triangulo":
                        lado = float(input("Ingrese un lado del triangulo (Permite decimales): "))
                        area = ((3**(1/2))/4)*(lado**2)
                        perimetro = lado * 3 
                        altura = ((3**(1/2))/2)*lado
                        print(f"Calculos realizados (Triangulo de lado {lado}m):\n1.Area: {area}m²\n2.Perimetro: {perimetro}m\n3.Altura: {altura}m")

                    elif eleccion == "triangulo rectangulo":
                        base = float(input("Ingrese la longitud de la base (Permite decimales): "))
                        altura = float(input("Ingrese la longitud de la altura (Permite decimales): "))
                        if base > altura:
                            catetoopuesto = altura
                            catetoadyacente = base
                        else:
                            catetoopuesto = base
                            catetoadyacente = altura
                        hipotenusa = ((base**2)+(altura**2))**(1/2)
                        seno = catetoopuesto/hipotenusa
                        coseno = catetoadyacente/hipotenusa
                        tangente = catetoopuesto/catetoadyacente
                        print(f"Calculos realizados (Triangulo rectangulo de altura {altura}m y base {base}m):\n1.Hipotenusa: {hipotenusa}m\n2.Seno: {seno}\n3.Coseno: {coseno}\n4.Tangente: {tangente}")
                    elif eleccion == "salir":
                        salir_2d += 1

        elif menu == "3d":
            salir_3d = 0
            while salir_3d == 0:
                print("Lista de figuras 3D:\n1.Cubo\n2.Tetraedro\n3.Esfera\n4.Salir")
                eleccion = input("Seleccione una figura: ")
                if eleccion in figuras[menu]:
                    eleccion = figuras[menu][eleccion]
                    if eleccion == "cubo":
                        arista = float(input("Ingrese el largo de una arista del cubo (Permite decimales): "))
                        volumen = arista**3
                        area = 6 * (arista**2)
                        diagonal_cara = arista * (2**(1/2))
                        diagonal_cubo = arista * (3**(1/2))
                        print(f"Calculos realizados (Cubo de {arista}x{arista}x{arista}m):\n1.Volumen: {volumen}m³\n2.Area: {area}m²\n3.Diagonal cara: {diagonal_cara}\n4.Diagonal cubo: {diagonal_cubo}")



                    elif eleccion == "tetraedro":
                        arista = float(input("Ingrese el largo de la arista (Permite decimales): "))
                        area_cara = ((3**(1/2))/4)*(arista**2)
                        area_total = (3**(1/2))*(arista**2)
                        volumen = ((2**(1/2))/12)*(arista**3)
                        altura = ((6**(1/2))/3)*arista
                        print(f"Calculos realizados (Tetraedro de arista {arista}m):\n1.Area de cara: {area_cara}m²\n2.Area total: {area_total}m²\n3.Volumen: {volumen}m³\n4.Altura: {altura}m")


                    elif eleccion == "esfera":
                        radio = float(input("Ingrese el radio de la esfera (Permite decimales): "))
                        volumen = ((4/3)*pi)*(radio**3)
                        area = (pi*4)*(radio**2)
                        print(f"Calculos realizados (Esfera de {radio}m radio):\n1.Volumen: {volumen}m³\n2.Area: {area}m²")
                    elif eleccion == "salir":
                        salir_3d += 1
                
        elif menu == "salir":
            salir_programa += 1
