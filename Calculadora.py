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
            "3.Cerrar programa"
        ]).ask()
    
    if menu == "1.Figuras 2D":  
        salir_2d = 0
        while salir_2d == 0:
            
            eleccion_2d = questionary.select(
                "Seleccione el tipo de figura:",
                choices=[
                    "1.Poligonos",
                    "2.Figuras circulares",
                    "3.Salir al menu principal"
                ]
            ).ask()
            
            if eleccion_2d == "1.Poligonos":
                salir_poli = 0
                while salir_poli == 0:

                    eleccion_poli = questionary.select(
                        "Lista de poligonos:",
                        choices=[
                            "1.Cuadrado",
                            "2.Rectangulo",
                            "3.Triangulo",
                            "4.Triangulo rectangulo",
                            "5.Pentagono",
                            "6.Salir al menu de figuras 2D"
                        ]).ask()
                            
                    if eleccion_poli == "1.Cuadrado":
                        loopcuadrado = 0
                        while loopcuadrado == 0:
                            try:
                                lado = float(questionary.text(
                                    "Ingrese la longitud de un lado del cuadrado (Permite decimales): "
                                ).ask())
                                if lado <= 0:
                                    print("Ingresa un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            area = lado**2
                            perimetro = lado*4
                            diagonal = lado * (2**(1/2))
                            print(f"Calculos realizados (Cuadrado de lado {lado}m):\n1.Area: {area:.2f}m²\n2.Perimetro: {perimetro:.2f}m\n3.Diagonal del cuadrado: {diagonal:.2f}m")
                            
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                loopcuadrado = 1                          

                    elif eleccion_poli == "2.Rectangulo":
                        looprectangulo = 0
                        while looprectangulo == 0:
                            try:
                                base = float(questionary.text("Ingrese la base del rectangulo (Permite decimales): ").ask())
                                if base <= 0:
                                    print("Ingrese un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            altura = 0
                            while altura <= 0:
                                try:
                                    altura = float(questionary.text("Ingrese la altura del rectangulo (Permite decimales): ").ask())
                                    if altura <= 0:
                                        print("Ingrese un numero valido!")
                                except ValueError:
                                    print("Ingrese un numero valido!")
                            area = base * altura
                            perimetro = (base * 2) + (altura * 2)
                            diagonal = ((base**2)+(altura**2))**(1/2)
                            print(f"Calculos realizados (Rectangulo de base {base}m, y altura {altura}m):\n1.Area: {area:.2f}m²\n2.Perimetro: {perimetro:.2f}m\n3.Diagonal del rectangulo: {diagonal:.2f}m")
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                looprectangulo = 1

                    elif eleccion_poli == "3.Triangulo":
                        looptriang = 0
                        while looptriang == 0:
                            try:
                                lado = float(questionary.text("Ingrese un lado del triangulo (Permite decimales): ").ask())
                                if lado < 0:
                                    print("Ingrese un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            area = ((3**(1/2))/4)*(lado**2)
                            perimetro = lado * 3 
                            altura = ((3**(1/2))/2)*lado
                            print(f"Calculos realizados (Triangulo de lado {lado}m):\n1.Area: {area:.2f}m²\n2.Perimetro: {perimetro:.2f}m\n3.Altura: {altura:.2f}m")
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                looptriang += 1
                                                
                    elif eleccion_poli == "4.Triangulo rectangulo":
                        looptrirec = 0
                        while looptrirec == 0:
                            try:
                                base = float(questionary.text("Ingrese la longitud de la base (Permite decimales): ").ask())
                                if base <= 0:
                                    print("Ingrese un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            altura = 0
                            while altura <= 0:
                                try:
                                    altura = float(questionary.text("Ingrese la longitud de la altura (Permite decimales): ").ask())
                                    if altura <= 0:
                                        print("Ingrese un numero valido!")
                                except ValueError:
                                    print("Ingrese un numero valido!")

                            hipotenusa = ((base**2)+(altura**2))**0.5
                            seno = altura / hipotenusa
                            coseno = base / hipotenusa
                            tangente = altura / base
                            print(f"Calculos realizados (Triangulo rectangulo de altura {altura}m y base {base}m):\n1.Hipotenusa: {hipotenusa:.2f}m\n2.Seno: {seno:.2f}\n3.Coseno: {coseno:.2f}\n4.Tangente: {tangente:.2f}")
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                looptrirec += 1
                    
                    elif eleccion_poli == "5.Pentagono":
                        looppenta = 0
                        while looppenta == 0:
                            try: 
                                lado = float(questionary.text("Ingrese la longitud de un lado del pentagono (Permite decimales): ").ask())
                                if lado <= 0:
                                    print("Ingrese un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            apotema = lado * 0.688
                            perimetro = 5 * lado
                            area = (perimetro*apotema)/2
                            angulo = ((5-2)*180)/5
                            suma_angulos = (5-2)*180
                            print(f"Calculos realizados (Pentagono de lado {lado}m):\n1.Apotema: {apotema:.2f}m\n2.Perimetro: {perimetro:.2f}m\n3.Area: {area:.2f}m²\n4.Angulos: {angulo:.2f}°")
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                looppenta += 1
                                               
                    elif eleccion_poli == "6.Salir al menu de figuras 2D":
                        salir_poli += 1

            elif eleccion_2d == "2.Figuras circulares":
                salir_circu = 0
                while salir_circu == 0:

                    eleccion_circu = questionary.select(
                        "Lista de figuras circulares:",
                        choices=[
                            "1.Circulo",
                            "2.Elipse",
                            "3.Salir al menu de figuras 2D"
                        ]).ask()

                    if eleccion_circu == "1.Circulo":
                        loopcircu = 0
                        while loopcircu == 0:
                            try:
                                radio = float(questionary.text("Ingrese el radio del circulo (Permite decimales): ").ask())
                                if radio <= 0:
                                    print("Ingrese un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            area = pi*(radio**2)
                            circunferencia = 2*pi*radio
                            diametro = radio * 2
                            print(f"Calculos realizados (Circulo de radio {radio}m):\n1.Area: {area:.2f}m²\n2.Circunferencia: {circunferencia:.2f}m\n3.Diametro: {diametro:.2f}m")
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                loopcircu += 1
                                              
                    elif eleccion_circu == "2.Elipse":
                        loopelipse = 0
                        while loopelipse == 0:
                            try:
                                smayor = float(questionary.text("Ingrese la longitud del semieje mayor: ").ask())
                                if smayor <= 0:
                                    print("Ingrese un numero valido!")
                                    continue
                            except ValueError:
                                print("Ingrese un numero valido!")
                                continue
                            
                    
                            smenor = 0
                            while smenor <= 0:
                                try:
                                    smenor = float(questionary.text("Ingrese la longitud del semieje menor: ").ask())
                                    if smenor <= 0:
                                        print("Ingrese un numero valido!")
                                except ValueError:
                                    print("Ingrese un numero valido!")
                                
                            if smenor > smayor:
                                smayor, smenor = smenor, smayor
                                print("Nota: Se han intercambiado los valores para que el radio mayor sea correcto.")
                            area = pi * smenor * smayor
                            perimetro = pi*((3*(smayor+smenor))-((((3*smayor)+smenor)*(smayor+(3*smenor)))**0.5))
                            dis_focal = ((smayor**2)-(smenor**2))**0.5
                            excentricidad = dis_focal/smayor
                            lado_recto = (2*(smenor**2))/smayor
                            print(f"Calculos realizados (Elipse de radios {smayor}m y {smenor}m):\n1.Area: {area:.2f}m²\n2.Perimetro: {perimetro:.2f}m\n3.Distancia focal: {dis_focal:.2f}m\n4.Excentricidad: {excentricidad:.2f}\n5.Lado recto: {lado_recto:.2f}m")
                            if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                                loopelipse += 1
                    
                    elif eleccion_circu == "3.Salir al menu de figuras 2D":
                        salir_circu += 1
                        
            elif eleccion_2d == "3.Salir al menu principal":
                salir_2d += 1
                    
    elif menu == "2.Figuras 3D":
        salir_3d = 0
        while salir_3d == 0:
            
            eleccion_3d = questionary.select(
                "Lista de figuras 3D:",
                choices=[
                    "1.Cubo",
                    "2.Tetraedro",
                    "3.Esfera",
                    "4.Salir al menu principal"
                ]
            ).ask()

            if eleccion_3d == "1.Cubo":
                loopcubo = 0
                while loopcubo == 0:
                    try:
                        arista = float(questionary.text("Ingrese el largo de una arista del cubo (Permite decimales): ").ask())
                        if arista <= 0:
                            print("Ingrese un numero valido!")
                            continue
                    except ValueError:
                        print("Ingrese un numero valido!")
                        continue
                    volumen = arista**3
                    area = 6 * (arista**2)
                    diagonal_cara = arista * (2**(1/2))
                    diagonal_cubo = arista * (3**(1/2))
                    print(f"Calculos realizados (Cubo de {arista}m):\n1.Volumen: {volumen:.2f}m³\n2.Area: {area:.2f}m²\n3.Diagonal cara: {diagonal_cara:.2f}\n4.Diagonal cubo: {diagonal_cubo:.2f}")
                    if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                        loopcubo += 1                    

            elif eleccion_3d == "2.Tetraedro":
                looptetra = 0
                while looptetra == 0:
                    try:
                        arista = float(questionary.text("Ingrese el largo de la arista (Permite decimales): ").ask())
                        if arista <= 0:
                            print("Ingrese un numero valido!")
                            continue
                    except ValueError:
                        print("Ingrese un numero valido!")
                        continue
                    area_cara = ((3**(1/2))/4)*(arista**2)
                    area_total = (3**(1/2))*(arista**2)
                    volumen = ((2**(1/2))/12)*(arista**3)
                    altura = ((6**(1/2))/3)*arista
                    print(f"Calculos realizados (Tetraedro de arista {arista}m):\n1.Area de cara: {area_cara:.2f}m²\n2.Area total: {area_total:.2f}m²\n3.Volumen: {volumen:.2f}m³\n4.Altura: {altura:.2f}m")
                    if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                        looptetra += 1
                    
            elif eleccion_3d == "3.Esfera":
                loopesfera = 0
                while loopesfera == 0:
                    try:
                        radio = float(questionary.text("Ingrese el radio de la esfera (Permite decimales): ").ask())
                        if radio <= 0:
                            print("Ingrese un numero valido!")
                            continue
                    except ValueError:
                        print("Ingresa un numero valido!")
                        continue
                    volumen = ((4/3)*pi)*(radio**3)
                    area = (pi*4)*(radio**2)
                    print(f"Calculos realizados (Esfera de {radio}m radio):\n1.Volumen: {volumen:.2f}m³\n2.Area: {area:.2f}m²")
                    if not questionary.confirm("Quiere realizar una nueva operacion?").ask():
                        loopesfera += 1
                                
            elif eleccion_3d == "4.Salir al menu principal":
                salir_3d += 1

    elif menu == "3.Cerrar programa":
        if questionary.confirm("Realmente quieres salir? ").ask():
            salir_programa += 1
