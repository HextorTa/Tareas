import re
import datetime

asientos = ["O"] * 100
asistentes = [""] * 100
precios = {"Platinum": 120_000, "Gold": 80_000, "Silver": 50_000}
ganancias_totales = 0

def mostrar_ubicaciones_disponibles():
    print("----- Ubicaciones Disponibles -----")
    print("")
    for i in range(0, 100, 10):
        for j in range(i + 1, i + 11):
            print("{:<4}".format(j if asientos[j-1] == "O" else "X"), end="")
        print()
    print("")
def mostrar_precios_entradas():
    print("\nPrecios de las entradas:")
    print("• Platinum, $120.000. (Asientos del 1 al 20).")
    print("• Gold, $80.000. (Asientos del 21 al 50).")
    print("• Silver, $50.000. (Asientos del 51 al 100).")
    print("")

def comprar_entradas():
    print("----- Comprar entradas -----")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
            if cantidad < 1 or cantidad > 3:
                print("Cantidad de entradas no válida. Ingrese un número entre 1 y 3.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número válido.")

    mostrar_ubicaciones_disponibles()
    mostrar_precios_entradas()

    asientos_disponibles = asientos.count("O")

    if asientos_disponibles == 0:
        print("Ya no quedan entradas disponibles.")
        return

    if cantidad > asientos_disponibles:
        print("No hay suficientes asientos disponibles. Por favor, seleccione una cantidad menor.")
        return

    for i in range(cantidad):
        print("Entrada", i+1)
        while True:
            try:
                ubicacion = int(input("Seleccione una ubicación disponible: "))
                if ubicacion < 1 or ubicacion > 100 or asientos[ubicacion-1] == "X":
                    print("Ubicación no disponible. Seleccione otra ubicación.")
                else:
                    break
            except ValueError:
                print("Error: Ingrese un número válido.")

        while True:
            run = input("Ingrese el RUN del asistente (sin guiones ni dígito verificador): ")
            run = run.replace(".", "").replace("-", "").upper()

            if not re.match(r"^\d{7,8}[0-9K]$", run):
                print("RUN inválido. Ingrese un RUN válido.")
            elif run in asistentes:
                print("El RUN ingresado ya ha sido registrado. Ingrese otro RUN.")
            else:
                break

        asistentes[ubicacion-1] = run
        asientos[ubicacion-1] = "X"

    print("Entradas compradas correctamente.")

def mostrar_listado_asistentes():
    print("----- Listado de Asistentes -----")
    asistentes_ordenados = sorted([(i+1, asistente) for i, asistente in enumerate(asistentes) if asistente != ""])
    if not asistentes_ordenados:
        print("")
        print("Sin asistentes disponibles.")
        print("")
    else:
        print("")
        for asiento, asistente in asistentes_ordenados:
            print(f"{asiento}.-{asistente}")
        print("")
        
def mostrar_ganancias_totales():
    print("------------ Mostrar ganancias totales ------------")
    ganancias_platinum = asientos[:20].count("X") * precios["Platinum"]
    ganancias_gold = asientos[20:50].count("X") * precios["Gold"]
    ganancias_silver = asientos[50:].count("X") * precios["Silver"]
    ganancias_totales = ganancias_platinum + ganancias_gold + ganancias_silver

    if ganancias_totales == 0:
        print("Aún no se ha añadido ninguna ganancia.")
    else:
        print("┌───────────────────┬──────────────┬─────────────┐")
        print("│   Tipo Entrada    │   Cantidad   │    Total    │")
        print("├───────────────────┼──────────────┼─────────────┤")
        print("│ Platinum $120.000 │      {:<8}│  ${:<10,.0f}│".format(asientos[:20].count("X"), ganancias_platinum))
        print("├───────────────────┼──────────────┼─────────────┤")
        print("│ Gold $80.000      │      {:<8}│  ${:<10,.0f}│".format(asientos[20:50].count("X"), ganancias_gold))
        print("├───────────────────┼──────────────┼─────────────┤")
        print("│ Silver $50.000    │      {:<8}│  ${:<10,.0f}│".format(asientos[50:].count("X"), ganancias_silver))
        print("├───────────────────┼──────────────┼─────────────┤")
        print("│       Total       │      {:<8}│  ${:<10,.0f}│".format(sum([asientos[:20].count("X"), asientos[20:50].count("X"), asientos[50:].count("X")]), ganancias_totales))
        print("└───────────────────┴──────────────┴─────────────┘")

def salir():
    print("Saliendo del sistema...")
    fecha_actual = datetime.date.today()
    fecha_actual_formateada = fecha_actual.strftime("%d/%m/%Y")
    print("Fecha actual:", fecha_actual_formateada)
    print("Nombre creador: Hector Tapia")
    print("¡Gracias por usar el sistema de venta de entradas!")

print("----- Menú Principal -----")
while True:
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    print("")
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        comprar_entradas()
    elif opcion == "2":
        mostrar_ubicaciones_disponibles()
    elif opcion == "3":
        mostrar_listado_asistentes()
    elif opcion == "4":
        mostrar_ganancias_totales()
    elif opcion == "5":
        salir()
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
