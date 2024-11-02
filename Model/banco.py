from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Simulando una base de datos
usuarios = {}
cuentas = {}


def registrar_usuario(nombre_usuario, contrasena):
    if nombre_usuario in usuarios:
        return "El usuario ya existe."
    usuarios[nombre_usuario] = contrasena
    return "Usuario registrado con éxito."


def iniciar_sesion(nombre_usuario, contrasena):
    if nombre_usuario not in usuarios:
        return False, "Usuario no encontrado."
    if usuarios[nombre_usuario] != contrasena:
        return False, "Contraseña incorrecta."
    return True, "Inicio de sesión exitoso."

def cambiar_contrasena(nombre_usuario, contrasena_actual, contrasena_nueva):
    if nombre_usuario not in usuarios:
        return "Usuario no encontrado."
    if usuarios[nombre_usuario] != contrasena_actual:
        return "Contraseña actual incorrecta."
    usuarios[nombre_usuario] = contrasena_nueva
    return "Contraseña cambiada con éxito."



def crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial):
    cuenta_id = f"{nombre_usuario}_{tipo_cuenta}"
    if cuenta_id in cuentas:
        return "La cuenta ya existe."
    cuentas[cuenta_id] = {'tipo': tipo_cuenta, 'saldo': saldo_inicial}
    return "Cuenta creada con éxito."


def mostrar_cuentas(nombre_usuario):
    cuentas_usuario = [c for c in cuentas if c.startswith(nombre_usuario)]
    if not cuentas_usuario:
        return "No hay cuentas registradas para este usuario."
    return "\n".join(cuentas_usuario)


def realizar_transaccion(nombre_usuario, nombre_destino, monto):
    cuenta_origen = f"{nombre_usuario}_Ahorros"  # Suponiendo que la cuenta origen es de tipo Ahorros
    cuenta_destino = f"{nombre_destino}_Ahorros"

    if cuenta_origen not in cuentas:
        return "La cuenta de origen no existe."
    if cuenta_destino not in cuentas:
        return "La cuenta de destino no existe."
    if cuentas[cuenta_origen]['saldo'] < monto:
        return "Saldo insuficiente."

    cuentas[cuenta_origen]['saldo'] -= monto
    cuentas[cuenta_destino]['saldo'] += monto
    return "Transacción realizada con éxito."



def consultar_saldo(nombre_usuario):
    cuenta_id = f"{nombre_usuario}_Ahorros"
    if cuenta_id not in cuentas:
        return "La cuenta no existe."
    return f"Saldo: {cuentas[cuenta_id]['saldo']}"



def retirar_dinero(nombre_usuario, monto):
    cuenta_id = f"{nombre_usuario}_Ahorros"
    if cuenta_id not in cuentas:
        return "La cuenta no existe."
    if cuentas[cuenta_id]['saldo'] < monto:
        return "Saldo insuficiente."

    cuentas[cuenta_id]['saldo'] -= monto
    return "Retiro realizado con éxito."



def generar_reporte_pdf(nombre_usuario, tipo_cuenta):
    cuenta_id = f"{nombre_usuario}_{tipo_cuenta}"
    if cuenta_id not in cuentas:
        return "No existe la cuenta para generar el reporte."

    saldo = cuentas[cuenta_id]['saldo']
    filename = f"{nombre_usuario}_reporte.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, f"Reporte de Cuenta para {nombre_usuario}")
    c.drawString(100, 730, f"Tipo de Cuenta: {tipo_cuenta}")
    c.drawString(100, 710, f"Saldo: {saldo}")
    c.save()
    return f"Reporte generado: {os.path.abspath(filename)}"


def bloquear_desbloquear_cuenta(nombre_usuario, tipo_cuenta, accion):
    cuenta_id = f"{nombre_usuario}_{tipo_cuenta}"
    if cuenta_id not in cuentas:
        return "La cuenta no existe."
    # Suponiendo que aquí se implementa la lógica de bloqueo/desbloqueo
    return f"Cuenta {accion} con éxito."
