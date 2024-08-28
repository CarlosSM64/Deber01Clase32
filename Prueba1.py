# Variables globales
usuarios = {}
saldo = {}

def mostrar_menu():
    print("Bienvenido al sistema de caja del banco")
    print("1. Registrar usuario")
    print("2. Depósito")
    print("3. Retiro")
    print("4. Consultar saldo")
    print("5. Salir")

def registrar_usuario():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        print("El usuario se encuentra registrado.")
    else:
        usuarios[nombre] = 0
        print(f"Usuario {nombre} registrado con éxito.")

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        if monto > 0:
            usuarios[nombre] += monto
            print(f"Depósito de {monto} realizado con éxito. Nuevo saldo: {usuarios[nombre]}")
        else:
            print("El monto a depositar debe ser positivo.")
    else:
        print("El usuario no existe.")

def retirar():
    nombre = input("Introduce el nombre del usuario: ")
    if nombre in usuarios:
        monto = float(input("Introduce el monto a retirar: "))
        if monto <= usuarios[nombre]:
            usuarios[nombre] -= monto
            print(f"Retiro de {monto} realizado con éxito. Nuevo saldo: {usuarios[nombre]}")
        else:
            print("Fondos insuficientes.")
    else:
        print("El usuario no existe.")

def consultar_saldo():
    try:
        nombre = input("Introduce el nombre del usuario: ")
        saldo = usuarios[nombre]
        print(f"El saldo de {nombre} es: {saldo}")
    except KeyError:
        print("El usuario no existe.")
    
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            consultar_saldo()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
        
main()