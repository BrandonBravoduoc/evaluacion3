import os 
os.system("cls")

mascotas=[]
titulo = f'''                       FICHA DE IGRESADOS
{"-"*90}
{"Especie":15}{"Nombre":10}{"Peso":10}{"Cuota consulta":20}{"Impuesto":15}{"Total":15}
{"-"*90}'''

def registrar():
    try: 
        while True: 
            especie = input("Indique la especie de su mascota: ")
            nom = input("Indique el nombre de su mascota: ")
            break
    except:
        print("Error al ingresar")
    try:
        while True:
            peso = int(input("indique el peso de su mascota: "))
            if peso <= 0: 
                print("El peso de tu mascota no puede ser 0, o menor a 0")
            else: 
                break
    except: 
        input("Error al ingresar peso")   
    try: 
        while True: 
            couta = int(input("Ingrese la couta de consulta inicial: "))
            if couta <= 0:
                print("La cuota inicial no puede ser 0")
            else: 
                impuesto = round(couta * 0.08)
                total    = couta + impuesto
                break
    except:
        input("Error al ingresar la cuota")
    mascotas.append([especie,nom,peso,couta,impuesto,total])
    input("Mascota ingresada correctamente. Enter para continuar")

def listar():
    os.system("cls")
    print(titulo)
    for row in mascotas: 
        print(f"{row[0]:15}",end='')
        print(f"{row[1]:15}",end='')
        print(f"{row[2]:10}",end='')
        print(f"{row[3]:20}",end='')
        print(f"{row[4]:15}",end='')
        print(f"{row[5]:15}",end='')
    input("\n")
def imprimir():
    try:
        while True: 
            os.system("cls")
            opc = int(input("""
------- Imprimir ficha de registro --------
1.- Imprimir ficha de todas las mascotas
2.- Filtrar por especie
3.- Volver al menu principal 

Digite opción: """))
            
            if opc <1 or opc > 3: 
                print("Error al seleccionar opción")
            elif opc == 1:
                with open("Ficha de mascotas.txt","w",newline='') as archivo:
                    archivo.write(titulo+"\n")
                    for ficha in mascotas:
                        archivo.write(f"{ficha[0]:15}{ficha[1]:15}{ficha[2]:15}{ficha[3]:15}{ficha[4]:15}{ficha[5]:15}\n")
            elif opc == 2: 
                try: 
                    espe = input("Indique la especie para filtrar: ")
                    encontrados = False
                    with open("Ficha por especie.txt","w",newline='') as ficha: 
                        ficha.write(titulo+"\n")
                        for especi in mascotas:
                            if especi[0].lower() == espe:
                                encontrados = True 
                                ficha.write(f"{especi[0]}{especi[1]:15}{especi[2]:15}{especi[3]:15}{especi[4]:15}{especi[5]:15}\n")
                            else: 
                                print("No se encontraron registros para la especie indicada")
                except:
                    input("Error de ingreso")
    except: 
            input("Error al imprimir la ficha. Enter para continuar")

while True: 
    os.system("cls")
    try:
        opc = int(input("""
------ VETERINARIA -------
1.- Registrar mascota
2.- Listar mascotas
3.- Imprimir fichas de registro
4.- Salir del programa

Digite opción: """))
        if opc < 1 or opc > 4: 
            print("Error al digitar opción")
        elif opc == 1: 
            registrar()
        elif opc == 2:
            listar()
        elif opc == 3: 
            imprimir()
        elif opc == 4: 
            break
    except:
        input("Error de ingreso. Reintentar")