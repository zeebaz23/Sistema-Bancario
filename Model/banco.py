usuarios = {}

class CuentaBancaria:
    def __init__(self, tipo, saldo_inicial=0):
        self.tipo = tipo
        self.saldo = saldo_inicial

    def mostrar_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Cuenta {self.tipo} - Saldo: {self.saldo}"


def registrar_usuario(nombre_usuario, contrasena):
    if nombre_usuario in usuarios:
        return "El usuario ya existe."
    else:
        usuarios[nombre_usuario] = {'contrasena': contrasena, 'cuentas': []}
        return f"Bienvenido, {nombre_usuario}! Has sido registrado exitosamente."

def cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena):
    if nombre_usuario in usuarios:
        if usuarios[nombre_usuario]['contrasena'] == contrasena_actual:
            usuarios[nombre_usuario]['contrasena'] = nueva_contrasena
            return "Contraseña actualizada exitosamente."
        else:
            return "La contraseña actual es incorrecta."
    else:
        return "El usuario no existe."

def iniciar_sesion(nombre_usuario, contrasena):
    if nombre_usuario in usuarios and usuarios[nombre_usuario]['contrasena'] == contrasena:
        return True, f"Inicio de sesión exitoso para {nombre_usuario}."
    else:
        return False, "Nombre de usuario o contraseña incorrectos."

def crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial=0):
    if nombre_usuario in usuarios:
        nueva_cuenta = CuentaBancaria(tipo_cuenta, saldo_inicial)
        usuarios[nombre_usuario]['cuentas'].append(nueva_cuenta)
        return f"Cuenta de tipo {tipo_cuenta} creada exitosamente."
    else:
        return "El usuario no existe."

def mostrar_cuentas(nombre_usuario):
    if nombre_usuario in usuarios:
        cuentas = usuarios[nombre_usuario]['cuentas']
        if cuentas:
            return "\n".join([str(cuenta) for cuenta in cuentas])
        else:
            return "Este usuario no tiene cuentas bancarias."
    else:
        return "El usuario no existe."


