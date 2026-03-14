import questionary

pi = 3.141592653589793

print("Bienvenido a la calculadora.")

salir_programa = 0
while salir_programa == 0:

    menu = questionary.select(
        "Lista de opciones:",
        choices=[
            "1.Figuras 2D",
            "2.Figuras 3D",
            "3.Salir"
        ]).ask()
    
    if menu == "1.Figuras 2D":
        salir_2d = 0
        while salir_2d == 0:
            eleccion = questionary.select(
                "Lista de figuras 2D:",
                choices=[
                    "1.Cuadrado",
                    "2.Rectangulo",
                    "3.Circulo",
                    "4.Triangulo",
                    "5.Triangulo rectangulo",
                    "6.Salir"
                ]).ask()
                      
            if eleccion == "1.Cuadrado":
                loopcuadrado = 0
                while loopcuadrado == 0:
                    try:
                        lado = float(questionary.text(
                            "Ingrese la longitud de un lado del cuadrado (Permite decimales): "
                        ).ask())
                        if lado <= 0:
                            print("Ingresa un numero valido!")
                        else:
                            area = lado**2
                            perimetro = lado*4
                            diagonal = lado * (2**(1/2))
                            print(f"Calculos realizados (Cuadrado de lado {lado}m):\n1.Area: {area}m²\n2.Perimetro: {perimetro}m\n3.Diagonal del cuadrado: {diagonal}m")
                            
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                loopcuadrado += 0
                            elif salir == False:
                                loopcuadrado += 1
                    except ValueError:
                                print("Ingrese un numero valido!")

            elif eleccion == "2.Rectangulo":
                looprectangulo = 0
                while looprectangulo == 0:
                    try:
                        base = float(questionary.text("Ingrese la base del rectangulo (Permite decimales): ").ask())
                        altura = float(questionary.text("Ingrese la altura del rectangulo (Permite decimales): ").ask())
                        if base <= 0 or altura <= 0:
                            print("Ingresa un numero valido!")
                        else:
                            area = base * altura
                            perimetro = (base * 2) + (altura * 2)
                            diagonal = ((base**2)+(altura**2))**(1/2)
                            print(f"Calculos realizados (Rectangulo de base {base}m, y altura {altura}m):\n1.Area: {area}m²\n2.Perimetro: {perimetro}m\n3.Diagonal del rectangulo: {diagonal}m")
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                looprectangulo += 0
                            elif salir == False:
                                looprectangulo += 1
                    except ValueError:
                        print("Ingrese un numero valido!")

            elif eleccion == "3.Circulo":
                loopcircu = 0
                while loopcircu == 0:
                    try:
                        radio = float(questionary.text("Ingrese el radio del circulo (Permite decimales): ").ask())
                        if radio <= 0:
                            print("Ingrese un numero valido!")
                        else:
                            area = pi*(radio**2)
                            circunferencia = 2*pi*radio
                            diametro = radio * 2
                            print(f"Calculos realizados (Circulo de radio {radio}m):\n1.Area: {area}m²\n2.Circunferencia: {circunferencia}m\n3.Diametro: {diametro}m")
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                loopcircu += 0
                            elif salir == False:
                                loopcircu += 1
                    except ValueError:
                        print("Ingrese un numero valido!")
            
            elif eleccion == "4.Triangulo":
                looptriang = 0
                while looptriang == 0:
                    try:
                        lado = float(questionary.text("Ingrese un lado del triangulo (Permite decimales): ").ask())
                        if lado < 0:
                            print("Ingrese un numero valido!")
                        else:
                            area = ((3**(1/2))/4)*(lado**2)
                            perimetro = lado * 3 
                            altura = ((3**(1/2))/2)*lado
                            print(f"Calculos realizados (Triangulo de lado {lado}m):\n1.Area: {area}m²\n2.Perimetro: {perimetro}m\n3.Altura: {altura}m")
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                looptriang += 0
                            elif salir == False:
                                looptriang += 1
                    except ValueError:
                        print("Ingrese un numero valido!")
            
            elif eleccion == "5.Triangulo rectangulo":
                looptrirec = 0
                while looptrirec == 0:
                    try:
                        base = float(questionary.text("Ingrese la longitud de la base (Permite decimales): ").ask())
                        altura = float(questionary.text("Ingrese la longitud de la altura (Permite decimales): ").text())
                        if base <= 0 or altura <= 0:
                            print("Ingrese un numero valido!")
                        else:
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
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                looptrirec += 0
                            elif salir == False:
                                looptrirec += 1
                    except ValueError:
                        print("Ingrese un numero valido!")
            
            elif eleccion == "6.Salir":
                salir_2d += 1

    elif menu == "2.Figuras 3D":
        salir_3d = 0
        while salir_3d == 0:
            eleccion = questionary.select(
                "Lista de figuras 3D:",
                choices=[
                    "1.Cubo",
                    "2.Tetraedro",
                    "3.Esfera",
                    "4.Salir"
                ]
            ).ask()

            if eleccion == "1.Cubo":
                loopcubo = 0
                while loopcubo == 0:
                    try:
                        arista = float(questionary.text("Ingrese el largo de una arista del cubo (Permite decimales): ").ask())
                        if arista <= 0:
                            print("Ingrese un numero valido!")
                        else:
                            volumen = arista**3
                            area = 6 * (arista**2)
                            diagonal_cara = arista * (2**(1/2))
                            diagonal_cubo = arista * (3**(1/2))
                            print(f"Calculos realizados (Cubo de {arista}x{arista}x{arista}m):\n1.Volumen: {volumen}m³\n2.Area: {area}m²\n3.Diagonal cara: {diagonal_cara}\n4.Diagonal cubo: {diagonal_cubo}")
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                loopcubo += 0
                            elif salir == False:
                                loopcubo += 1
                    except ValueError:
                        print("Ingrese un numero valido!")

            elif eleccion == "2.Tetraedro":
                looptetra = 0
                while looptetra == 0:
                    try:
                        arista = float(questionary.text("Ingrese el largo de la arista (Permite decimales): ").ask())
                        if arista <= 0:
                            print("Ingrese un numero valido!")
                        else:
                            area_cara = ((3**(1/2))/4)*(arista**2)
                            area_total = (3**(1/2))*(arista**2)
                            volumen = ((2**(1/2))/12)*(arista**3)
                            altura = ((6**(1/2))/3)*arista
                            print(f"Calculos realizados (Tetraedro de arista {arista}m):\n1.Area de cara: {area_cara}m²\n2.Area total: {area_total}m²\n3.Volumen: {volumen}m³\n4.Altura: {altura}m")
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                looptetra += 0
                            elif salir == False:
                                looptetra += 1
                    except ValueError:
                        print("Ingrese un numero valido!")

            elif eleccion == "3.Esfera":
                loopesfera = 0
                while loopesfera == 0:
                    try:
                        radio = float(questionary.text("Ingrese el radio de la esfera (Permite decimales): ").ask())
                        if radio <= 0:
                            print("Ingrese un numero valido!")
                        else:
                            volumen = ((4/3)*pi)*(radio**3)
                            area = (pi*4)*(radio**2)
                            print(f"Calculos realizados (Esfera de {radio}m radio):\n1.Volumen: {volumen}m³\n2.Area: {area}m²")
                            salir = questionary.confirm("Quiere realizar una nueva operacion?").ask()
                            if salir == True:
                                loopesfera += 0
                            elif salir == False:
                                loopesfera += 1
                    except ValueError:
                        print("Ingresa un numero valido!")
            
            elif eleccion == "4.Salir":
                salir_3d += 1


    elif menu == "3.Salir":
        salir_programa += 1
