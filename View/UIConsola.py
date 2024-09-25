# UIConsola.py
from Model.banco import registrar_usuario, cambiar_contrasena, iniciar_sesion, crear_cuenta, usuarios

class UIConsola:
    def ejecutar_app(self):
        while True:
            print("\n--- Sistema Bancario ---")
            print("1. Registrar usuario")
            print("2. Cambiar contraseña")
            print("3. Iniciar sesión")
            print("4. Crear cuenta")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.registrar_usuario()
            elif opcion == '2':
                self.cambiar_contrasena()
            elif opcion == '3':
                self.iniciar_sesion()
            elif opcion == '4':
                self.crear_cuenta()
            elif opcion == '5':
                print("Saliendo del sistema. Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    def registrar_usuario(self):
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        registrar_usuario(nombre_usuario, contrasena)

    def cambiar_contrasena(self):
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contrasena_actual = input("Ingrese la contraseña actual: ")
        nueva_contrasena = input("Ingrese la nueva contraseña: ")
        cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena)

    def iniciar_sesion(self):
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        contrasena = input("Ingrese la contraseña: ")
        if iniciar_sesion(nombre_usuario, contrasena):
            print(f"Bienvenido, {nombre_usuario}!")

    def crear_cuenta(self):
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorros, Corriente, Inversión): ")
        saldo_inicial = input("Ingrese el saldo inicial (deje vacío si no desea establecer uno): ")
        saldo_inicial = float(saldo_inicial) if saldo_inicial else 0
        crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial)

