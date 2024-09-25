usuarios = {}

class CuentaBancaria:
    def __init__(self, tipo, saldo_inicial=0):
        self.tipo = tipo
        self.saldo = saldo_inicial
        self.historial_transacciones = []

    def mostrar_saldo(self):
        return self.saldo

    def agregar_transaccion(self, monto):
        self.historial_transacciones.append(monto)

    def mostrar_historial(self):
        return self.historial_transacciones

def registrar_usuario(nombre_usuario, contrasena):
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[nombre_usuario] = {'contrasena': contrasena, 'cuentas': []}
        print(f"Bienvenido, {nombre_usuario}! Has sido registrado exitosamente.")

def cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena):
    if nombre_usuario in usuarios:
        if usuarios[nombre_usuario]['contrasena'] == contrasena_actual:
            usuarios[nombre_usuario]['contrasena'] = nueva_contrasena
            print("Contraseña actualizada exitosamente.")
        else:
            print("La contraseña actual es incorrecta.")
    else:
        print("El usuario no existe.")

def iniciar_sesion(nombre_usuario, contrasena):
    if nombre_usuario in usuarios and usuarios[nombre_usuario]['contrasena'] == contrasena:
        print(f"Inicio de sesión exitoso para {nombre_usuario}.")
        return True
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return False

def crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial=0):
    if nombre_usuario in usuarios:
        nueva_cuenta = CuentaBancaria(tipo_cuenta, saldo_inicial)
        usuarios[nombre_usuario]['cuentas'].append(nueva_cuenta)
        print(f"Cuenta de tipo {tipo_cuenta} creada exitosamente.")
    else:
        print("El usuario no existe.")
