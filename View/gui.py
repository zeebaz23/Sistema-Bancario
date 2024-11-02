import tkinter as tk
from tkinter import messagebox, ttk
from Model.banco import (
    registrar_usuario, iniciar_sesion, crear_cuenta,
    mostrar_cuentas, realizar_transaccion, consultar_saldo, retirar_dinero,
    generar_reporte_pdf, bloquear_desbloquear_cuenta, cambiar_contrasena
)

class BancoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bancario")
        self.root.geometry("600x500")
        self.root.config(bg="#e6f2f2")

        self.usuario_actual = None

        self.nombre_usuario = tk.StringVar()
        self.contrasena = tk.StringVar()
        self.contrasena_nueva = tk.StringVar()
        self.tipo_cuenta = tk.StringVar()
        self.saldo_inicial = tk.StringVar()
        self.cuenta_origen = tk.StringVar()
        self.cuenta_destino = tk.StringVar()
        self.monto_transaccion = tk.StringVar()
        self.monto_retiro = tk.StringVar()

        self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Sistema Bancario", font=("Arial", 20, "bold"), bg="#e6f2f2").pack(pady=10)

        btn_iniciar_sesion = tk.Button(self.root, text="Iniciar Sesión", command=self.mostrar_panel_sesion, width=20, bg="#008CBA", fg="white")
        btn_iniciar_sesion.pack(pady=10)

        btn_registrarse = tk.Button(self.root, text="Crear Cuenta", command=self.mostrar_panel_registro, width=20, bg="#4CAF50", fg="white")
        btn_registrarse.pack(pady=10)

    def mostrar_panel_registro(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Registro de Usuario", font=("Arial", 20, "bold"), bg="#e6f2f2").pack(pady=10)

        tk.Label(self.root, text="Nombre de Usuario:", bg="#e6f2f2").pack()
        tk.Entry(self.root, textvariable=self.nombre_usuario, width=30).pack(pady=5)

        tk.Label(self.root, text="Contraseña:", bg="#e6f2f2").pack()
        tk.Entry(self.root, textvariable=self.contrasena, show="*", width=30).pack(pady=5)

        btn_registrar = tk.Button(self.root, text="Registrar", command=self.registrar_usuario, width=20, bg="#4CAF50", fg="white")
        btn_registrar.pack(pady=10)

        btn_volver = tk.Button(self.root, text="Volver", command=self.mostrar_menu_principal, width=20, bg="#f44336", fg="white")
        btn_volver.pack(pady=5)

    def mostrar_panel_sesion(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Inicio de Sesión", font=("Arial", 20, "bold"), bg="#e6f2f2").pack(pady=10)

        tk.Label(self.root, text="Nombre de Usuario:", bg="#e6f2f2").pack()
        tk.Entry(self.root, textvariable=self.nombre_usuario, width=30).pack(pady=5)

        tk.Label(self.root, text="Contraseña:", bg="#e6f2f2").pack()
        tk.Entry(self.root, textvariable=self.contrasena, show="*", width=30).pack(pady=5)

        btn_iniciar_sesion = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion, width=20, bg="#008CBA", fg="white")
        btn_iniciar_sesion.pack(pady=10)

        btn_volver = tk.Button(self.root, text="Volver", command=self.mostrar_menu_principal, width=20, bg="#f44336", fg="white")
        btn_volver.pack(pady=5)

    def mostrar_panel_cuenta(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Operaciones Bancarias", font=("Arial", 20, "bold"), bg="#e6f2f2").pack(pady=10)

        panel_cuenta = tk.LabelFrame(self.root, text="Cuenta", padx=20, pady=20, bg="#f2f2f2", font=("Arial", 12))
        panel_cuenta.pack(fill="both", padx=20, pady=10)

        tk.Label(panel_cuenta, text="Tipo de Cuenta:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
        ttk.Combobox(panel_cuenta, textvariable=self.tipo_cuenta, values=["Ahorros", "Corriente", "Inversión"], width=28).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(panel_cuenta, text="Saldo Inicial:", bg="#f2f2f2").grid(row=1, column=0, sticky="w")
        tk.Entry(panel_cuenta, textvariable=self.saldo_inicial, width=30).grid(row=1, column=1, padx=5, pady=5)

        btn_crear_cuenta = tk.Button(panel_cuenta, text="Crear Cuenta", command=self.crear_cuenta, width=20, bg="#4CAF50", fg="white")
        btn_crear_cuenta.grid(row=2, columnspan=2, pady=5)

        btn_ver_cuentas = tk.Button(panel_cuenta, text="Ver Cuentas", command=self.ver_cuentas, width=20, bg="#008CBA", fg="white")
        btn_ver_cuentas.grid(row=3, columnspan=2, pady=5)

        panel_transaccion = tk.LabelFrame(self.root, text="Transacciones", padx=20, pady=20, bg="#f2f2f2", font=("Arial", 12))
        panel_transaccion.pack(fill="both", padx=20, pady=10)

        tk.Label(panel_transaccion, text="Nombre Destino:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
        tk.Entry(panel_transaccion, textvariable=self.cuenta_destino, width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(panel_transaccion, text="Monto:", bg="#f2f2f2").grid(row=1, column=0, sticky="w")
        tk.Entry(panel_transaccion, textvariable=self.monto_transaccion, width=30).grid(row=1, column=1, padx=5, pady=5)

        btn_transaccion = tk.Button(panel_transaccion, text="Realizar Transacción", command=self.realizar_transaccion, width=20, bg="#4CAF50", fg="white")
        btn_transaccion.grid(row=2, columnspan=2, pady=5)

        btn_consultar_saldo = tk.Button(panel_transaccion, text="Consultar Saldo", command=self.consultar_saldo, width=20, bg="#008CBA", fg="white")
        btn_consultar_saldo.grid(row=3, columnspan=2, pady=5)

        panel_retiro = tk.LabelFrame(self.root, text="Retirar Dinero", padx=20, pady=20, bg="#f2f2f2", font=("Arial", 12))
        panel_retiro.pack(fill="both", padx=20, pady=10)

        tk.Label(panel_retiro, text="Monto a Retirar:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
        tk.Entry(panel_retiro, textvariable=self.monto_retiro, width=30).grid(row=0, column=1, padx=5, pady=5)

        btn_retirar_dinero = tk.Button(panel_retiro, text="Retirar Dinero", command=self.retirar_dinero, width=20, bg="#FF5733", fg="white")
        btn_retirar_dinero.grid(row=1, columnspan=2, pady=5)

        panel_reportes = tk.LabelFrame(self.root, text="Reportes", padx=20, pady=20, bg="#f2f2f2", font=("Arial", 12))
        panel_reportes.pack(fill="both", padx=20, pady=10)

        btn_generar_reporte = tk.Button(panel_reportes, text="Generar Reporte PDF", command=self.generar_reporte_pdf, width=20, bg="#FF5733", fg="white")
        btn_generar_reporte.pack(pady=5)

        panel_cambiar_contrasena = tk.LabelFrame(self.root, text="Cambiar Contraseña", padx=20, pady=20, bg="#f2f2f2", font=("Arial", 12))
        panel_cambiar_contrasena.pack(fill="both", padx=20, pady=10)

        tk.Label(panel_cambiar_contrasena, text="Contraseña Actual:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
        tk.Entry(panel_cambiar_contrasena, textvariable=self.contrasena, show="*", width=30).grid(row=0, column=1,
                                                                                                  padx=5, pady=5)

        tk.Label(panel_cambiar_contrasena, text="Nueva Contraseña:", bg="#f2f2f2").grid(row=1, column=0, sticky="w")
        tk.Entry(panel_cambiar_contrasena, textvariable=self.contrasena_nueva, show="*", width=30).grid(row=1, column=1,
                                                                                                        padx=5, pady=5)

        btn_cambiar_contrasena = tk.Button(panel_cambiar_contrasena, text="Cambiar Contraseña",
                                           command=self.cambiar_contrasena, width=20, bg="#4CAF50", fg="white")
        btn_cambiar_contrasena.grid(row=2, columnspan=2, pady=5)

        btn_cerrar_sesion = tk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion, width=20,
                                      bg="#f44336", fg="white")
        btn_cerrar_sesion.pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_usuario.get()
        contrasena = self.contrasena.get()
        mensaje = registrar_usuario(nombre, contrasena)
        messagebox.showinfo("Registro", mensaje)

    def cambiar_contrasena(self):
        actual = self.contrasena.get()
        nueva = self.contrasena_nueva.get()
        mensaje = cambiar_contrasena(self.usuario_actual, actual, nueva)
        messagebox.showinfo("Cambiar Contraseña", mensaje)

    def iniciar_sesion(self):
        nombre = self.nombre_usuario.get()
        contrasena = self.contrasena.get()
        exito, mensaje = iniciar_sesion(nombre, contrasena)
        messagebox.showinfo("Inicio de Sesión", mensaje)
        if exito:
            self.usuario_actual = nombre
            self.mostrar_panel_cuenta()

    def crear_cuenta(self):
        nombre = self.nombre_usuario.get()
        tipo = self.tipo_cuenta.get()
        saldo = self.saldo_inicial.get()
        if saldo.isdigit():
            saldo = float(saldo)
            mensaje = crear_cuenta(nombre, tipo, saldo)
            messagebox.showinfo("Crear Cuenta", mensaje)
        else:
            messagebox.showerror("Error", "El saldo inicial debe ser un número.")

    def ver_cuentas(self):
        nombre = self.nombre_usuario.get()
        cuentas = mostrar_cuentas(nombre)
        messagebox.showinfo("Cuentas", cuentas)

    def realizar_transaccion(self):
        destino = self.cuenta_destino.get()
        monto = self.monto_transaccion.get()
        if monto.isdigit():
            monto = float(monto)
            mensaje = realizar_transaccion(self.usuario_actual, destino, monto)
            messagebox.showinfo("Transacción", mensaje)
        else:
            messagebox.showerror("Error", "El monto debe ser un número.")

    def consultar_saldo(self):
        saldo = consultar_saldo(self.usuario_actual)
        messagebox.showinfo("Consulta de Saldo", saldo)

    def retirar_dinero(self):
        monto = self.monto_retiro.get()
        if monto.isdigit():
            monto = float(monto)
            mensaje = retirar_dinero(self.usuario_actual, monto)
            messagebox.showinfo("Retiro", mensaje)
        else:
            messagebox.showerror("Error", "El monto debe ser un número.")

    def generar_reporte_pdf(self):
        nombre = self.nombre_usuario.get()
        tipo = self.tipo_cuenta.get()
        mensaje = generar_reporte_pdf(nombre, tipo)
        messagebox.showinfo("Reporte PDF", mensaje)

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.mostrar_menu_principal()

