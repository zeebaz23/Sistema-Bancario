from Model.banco import registrar_usuario, cambiar_contrasena, iniciar_sesion, crear_cuenta, mostrar_cuentas, usuarios


class UIConsola:
    def ejecutar_app(self):
        self.menu_principal()

    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrarse")
            print("2. Iniciar sesión")
            print("3. Cambiar contraseña")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                self.cambiar_contrasena()
            elif opcion == "4":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor intenta de nuevo.")

    def registrar_usuario(self):
        nombre_usuario = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        resultado = registrar_usuario(nombre_usuario, contrasena)
        print(resultado)

    def cambiar_contrasena(self):
        nombre_usuario = input("Nombre de usuario: ")
        contrasena_actual = input("Contraseña actual: ")
        nueva_contrasena = input("Nueva contraseña: ")
        resultado = cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena)
        print(resultado)

    def iniciar_sesion(self):
        nombre_usuario = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        exito, mensaje = iniciar_sesion(nombre_usuario, contrasena)
        print(mensaje)
        if exito:
            self.menu_sistema(nombre_usuario)

    def menu_sistema(self, nombre_usuario):
        while True:
            print(f"\n--- Bienvenido {nombre_usuario} ---")
            print("1. Crear cuenta bancaria")
            print("2. Ver cuentas")
            print("3. Cerrar sesión")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear_cuenta(nombre_usuario)
            elif opcion == "2":
                self.ver_cuentas(nombre_usuario)
            elif opcion == "3":
                print(f"{nombre_usuario} ha cerrado sesión.")
                break
            else:
                print("Opción no válida. Por favor intenta de nuevo.")

    def crear_cuenta(self, nombre_usuario):
        tipo_cuenta = input("Tipo de cuenta (Ahorros, Corriente, Inversión): ")
        saldo_inicial = input("Saldo inicial (opcional, presiona Enter para dejar en 0): ")
        saldo_inicial = float(saldo_inicial) if saldo_inicial else 0
        resultado = crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial)
        print(resultado)

    def ver_cuentas(self, nombre_usuario):
        resultado = mostrar_cuentas(nombre_usuario)
        print(resultado)
