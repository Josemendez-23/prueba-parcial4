


stock_concepcion = 500
stock_puente_alto = 1300
stock_baron = 100
stock_vergara = 50


compradores = []

def mostrar_menu():
    """Muestra el menú principal"""
    print("totem autoservicio gira rock and chile in chile")
    print("1. Comprar entrada en Concepción.")
    print("2. Comprar entrada en Puente Alto.")
    print("3. Comprar entrada en Muelle Barón, Valparaíso.")
    print("4. Comprar entrada en Muelle Vergara, Viña del Mar.")
    print("5. Salir.")

def validar_codigo_confirmacion(codigo):
    """Valida el código de confirmación según los criterios establecidos"""
    
    if len(codigo) < 6:
        return False
    
   
    if ' ' in codigo:
        return False
    
   
    tiene_mayuscula = False
    tiene_numero = False
    
    for caracter in codigo:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True
    
    return tiene_mayuscula and tiene_numero

def comprar_concepcion():
    """Función para comprar entrada en Concepción"""
    global stock_concepcion, compradores
    
    print("\n-- Compra en Concepción --")
    
    
    if stock_concepcion <= 0:
        print("Error: No hay stock disponible para esta locación.")
        return
    
    
    nombre = input("Nombre del comprador: ")
    
    
    if nombre in compradores:
        print("Error: el nombre de comprador ya está registrado.")
        return
    
    
    codigo = input("Código de confirmación: ")
    
    
    if not validar_codigo_confirmacion(codigo):
        print("Error: código de confirmación inválido.")
        return
    
   
    compradores.append(nombre)
    stock_concepcion = stock_concepcion - 1
    print("Entrada registrada! Stock restante:", stock_concepcion)

def comprar_puente_alto():
    """Función para comprar entrada en Puente Alto"""
    global stock_puente_alto, compradores
    
    print("\n-- Compra en Puente Alto --")
    
    
    if stock_puente_alto <= 0:
        print("Error: No hay stock disponible para esta locación.")
        return
    
  
    nombre = input("Nombre del comprador: ")
    
   
    if nombre in compradores:
        print("Error: el nombre de comprador ya está registrado.")
        return
    
   
    try:
        cantidad = int(input("Cantidad de entradas (máx 3): "))
    except:
        print("Error: debe ingresar un número válido.")
        return
    
    
    if cantidad < 1 or cantidad > 3:
        print("Error: solo se permiten entre 1 y 3 entradas por persona.")
        return
    
   
    if cantidad > stock_puente_alto:
        print("Error: no hay suficiente stock disponible.")
        return
    
   
    compradores.append(nombre)
    stock_puente_alto = stock_puente_alto - cantidad
    print("Entradas registradas! Stock restante:", stock_puente_alto)

def comprar_baron():
    """Función para comprar entrada en Muelle Barón"""
    global stock_baron, compradores
    
    print("\n-- Compra en Muelle Barón, Valparaíso --")
    
   
    if stock_baron <= 0:
        print("Error: No hay stock disponible para esta locación.")
        return
    
    
    nombre = input("Nombre del comprador: ")
    
    
    if nombre in compradores:
        print("Error: el nombre de comprador ya está registrado.")
        return
    
   
    print("Tipo de entrada asignado: G")
    
    
    compradores.append(nombre)
    stock_baron = stock_baron - 1
    print("Entrada registrada! Stock restante:", stock_baron)

def comprar_vergara():
    """Función para comprar entrada en Muelle Vergara"""
    global stock_vergara, compradores
    
    print("\n-- Compra en Muelle Vergara, Viña del Mar --")
    
    
    if stock_vergara <= 0:
        print("Error: No hay stock disponible para esta locación.")
        return
    
    
    nombre = input("Nombre del comprador: ")
    
    
    if nombre in compradores:
        print("Error: el nombre de comprador ya está registrado.")
        return
    
    
    tipo_entrada = input("Tipo de entrada (Sun=Sunset, Ni=Night): ")
    
    
    if tipo_entrada.lower() != 'sun' and tipo_entrada.lower() != 'ni':
        print("Error: tipo de entrada inválido.")
        return
    

    compradores.append(nombre)
    stock_vergara = stock_vergara - 1
    print("Entrada registrada! Stock restante:", stock_vergara)

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            comprar_concepcion()
        elif opcion == '2':
            comprar_puente_alto()
        elif opcion == '3':
            comprar_baron()
        elif opcion == '4':
            comprar_vergara()
        elif opcion == '5':
            print("\nPrograma terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()