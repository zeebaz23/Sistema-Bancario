# Sistema-Bancario
# Descripción del proyecto
Este ejercicio consiste en desarrollar una aplicación que simule las operaciones básicas de un sistema bancario, permitiendo a los usuarios gestionar sus cuentas y realizar transacciones. El objetivo es que los usuarios puedan interactuar con el sistema a través de operaciones como registro, inicio de sesión, creación de cuentas bancarias y la ejecución de transacciones entre ellas. El sistema está diseñado para ser simple y seguro, funcionando inicialmente en una interfaz de consola.

En el sistema bancario, cada usuario registrado puede crear varios tipos de cuentas, como cuentas de ahorro, cuentas corrientes o cuentas de inversión. Estas cuentas tienen saldo asociado, el cual puede incrementarse o disminuirse a través de las transacciones que el usuario realice.

Cuando arranca la aplicación, el sistema permite registrar nuevos usuarios mediante un nombre de usuario y una contraseña, que serán utilizados para acceder al sistema. Cada usuario puede crear diferentes tipos de cuentas bancarias según sus necesidades. Las cuentas disponibles en este sistema son:

- Cuentas de Ahorro: Cuentas en las que el usuario puede depositar dinero y generar intereses en el futuro.
- Cuentas Corrientes: Cuentas que permiten transacciones frecuentes, como pagos y transferencias.
- Cuentas de Inversión: Cuentas diseñadas para gestionar inversiones financieras.

Una vez que el usuario ha iniciado sesión, puede consultar su saldo, ver el historial de transacciones de cada cuenta y realizar transacciones como transferencias entre sus propias cuentas o hacia cuentas de otros usuarios registrados en el sistema. El sistema también permite que los usuarios cambien su contraseña por motivos de seguridad.

Además, el sistema brinda la opción de generar reportes financieros en formato PDF. Estos reportes contienen detalles sobre las cuentas del usuario, como el saldo actual y un historial completo de las transacciones realizadas. También se incluye la posibilidad de bloquear y desbloquear cuentas en caso de que se requiera una medida de seguridad adicional.

La lógica de la aplicación incluye:

- Registro de usuario: El sistema pedirá un nombre de usuario y contraseña para registrar al usuario en la plataforma.
- Inicio de sesión: Los usuarios deberán ingresar su nombre de usuario y contraseña para poder acceder a sus cuentas y realizar operaciones.
- Cambio de contraseña: El usuario puede optar por modificar su contraseña en cualquier momento.
- Gestión de cuentas: Los usuarios podrán crear diferentes tipos de cuentas bancarias y ver los detalles de cada una de ellas.
- Transacciones: Los usuarios podrán transferir dinero entre sus cuentas o a cuentas de otros usuarios.
- Consultas: Los usuarios podrán ver el saldo de sus cuentas y el historial de transacciones.
- Retiro de dinero: Los usuarios podrán retirar dinero de sus cuentas.
- Generación de reportes: Se podrán generar reportes en formato PDF con información detallada sobre las cuentas y transacciones.
- Bloqueo y desbloqueo de cuentas: Se permitirá bloquear cuentas en caso de que sea necesario por seguridad.

La idea es que la aplicación durante una sesión permita a los usuarios realizar todas estas operaciones y mostrarles la información de sus cuentas en cualquier momento. Se espera que el sistema se amplíe en futuras fases para incluir funcionalidades más avanzadas y una interfaz gráfica, proporcionando una experiencia de usuario más amigable.

## Modelado del mundo
![MODELADO drawio](https://github.com/user-attachments/assets/0bba29e6-4e60-4013-a954-956a66dbafd5)



## Requisitos Funcionales

### R1 - Registro de usuario

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir registrar un nuevo usuario para que pueda crear cuentas y realizar operaciones bancarias.                                                                                                                     |
| **Entrada** 	   | - Nombre de usuario<br>-Contraseña 	                                                                                                                                                                             |
| **Resultado** 	 | 1. El sistema muestra un mensaje de éxito o error.<br>2. El usuario es agregado al sistema con su nombre de usuario y contraseña si no existe previamente. n  <br>3. Se muestra el menú principal. 	 |

#### Descomposición 

| Paso                                    | Método                                        | Responsable       |
|-----------------------------------------|-----------------------------------------------|-------------------|
|Solicitar nombre de usuario y contraseña |mostrar_panel_registro()  | BancoGUI        |
|Verificar si el usuario ya existe        |registrar_usuario(nombre_usuario, contrasena)  | banco.py |
|Agregar usuario a la base de datos       |registrar_usuario(nombre_usuario, contrasena)  | banco.py   |
|Retornar mensaje de éxito o error        |registrar_usuario()| BancoGUI     |

                                                                                                                               
### R2 - Cambio de contraseña

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir que el usuario registrado cambie su contraseña por motivos de seguridad.                                                                                                                       |
| **Entrada** 	   | - Nombre de usuario<br>- Contraseña actual<br>- Nueva contraseña 	                                                                                                                                                                             |
| **Resultado** 	 | 1. El sistema verifica la contraseña actual.<br>2. Si la verificación es exitosa, el sistema actualiza la contraseña y muestra un mensaje de confirmación.<br>3. Se regresa al menú principal	 |

| Paso                                         | Método                                                                 | Responsable       |
|----------------------------------------------|------------------------------------------------------------------------|-------------------|
|Solicitar nombre de usuario                   |cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena) | UIConsola         |
|Verificar si el usuario ya existe             |cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena) | SistemaBancario   |
|Verificar si la contraseña actual es correcta |cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena) | SistemaBancario   |
|Actualizar la contraseña en la base de datos  |cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena) | SistemaBancario   |
|Retornar mensaje de éxito o error             |cambiar_contrasena(nombre_usuario, contrasena_actual, nueva_contrasena) | UIConsola         |

### R3 - Inicio de sesión

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir que los usuarios registrados inicien sesión ingresando su nombre de usuario y contraseña para acceder a sus cuentas bancarias.                                                                                         |
| **Entrada** 	   | - Nombre de usuario<br>- Contraseña 	                                                                                                                                                                             |
| **Resultado** 	 | 1.  El sistema verifica las credenciales ingresadas.<br>2. Si la verificación es exitosa, se accede a la sesión del usuario.<br>3.Se muestra el menú de opciones del sistema.	 |

| Paso                                         | Método                                    | Responsable       |
|----------------------------------------------|-------------------------------------------|-------------------|
|Solicitar nombre de usuario                   |iniciar_sesion(nombre_usuario, contrasena) | UIConsola         |
|Verificar credenciales en la base de datos    |iniciar_sesion(nombre_usuario, contrasena) | SistemaBancario   |
|Retornar resultado del inicio de sesión       |iniciar_sesion(nombre_usuario, contrasena) | UIConsola         |


### R4 - Creación de cuentas bancarias

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir que los usuarios creen cuentas bancarias del tipo ahorros, corriente o inversión.                                                                                         |
| **Entrada** 	   | - Tipo de cuenta a crear (Ahorros, Corriente, Inversión)<br>- Saldo inicial(Opcional)	                                                                                                                                                                  |
| **Resultado** 	 | 1.  El sistema confirma la creación de la cuenta seleccionada.<br>2. La cuenta creada se agrega al perfil del usuario.<br>3. El saldo inicial se refleja en la nueva cuenta. |

| Paso                                          | Método                                                  | Responsable       |
|-----------------------------------------------|---------------------------------------------------------|-------------------|
|Solicitar tipo de cuenta                       |crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial) | UIConsola         |
|Solicitar saldo inicial                        |crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial) | UIConsola         |
|Verificar si el usuario está registrado        |crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial) | SistemaBancario   |
|Crear nueva cuenta bancaria                    |crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial) | SistemaBancario   |
|Agregar la nueva cuenta a la lista del usuario |crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial) | SistemaBancario   |
|Retornar mensaje de éxito o error              |crear_cuenta(nombre_usuario, tipo_cuenta, saldo_inicial) | UIConsola         |

### R5 -  Realizar transacciones entre cuentas

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir a los usuarios realizar transacciones entre sus propias cuentas o enviar dinero a cuentas de otros usuarios del banco.                                                                                      |
| **Entrada** 	   | - Cuenta de origen<br>-Cuenta de destino<br>-Monto de la transacción                                                                                                                                                                  |
| **Resultado** 	 | 1. El sistema valida que la cuenta de origen tiene fondos suficientes.<br>2. Efectúa la transacción y actualiza el saldo de ambas cuentas.<br>3. Muestra mensaje de éxito. |


### R6 - Mostrar saldo actual

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir a los usuarios consultar el saldo actual de cualquiera de sus cuentas bancarias.                                                                                     |
| **Entrada** 	   | - Nombre de usuario.<br>-Tipo de cuenta (Ahorros, Corriente, Inversión)                                                                                                                                                            |
| **Resultado** 	 | 1. El sistema el saldo actual de la cuenta solicitada.<br>2. Si no se encuentra la cuenta, muestra un mensaje de error indicando que no existe de lo contrario muestra el saldo. |



### R7 - Retirar dinero de una cuenta

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir a los usuarios retirar dinero de cualquiera de sus cuentas bancarias, siempre que tengan suficiente saldo disponible.                                                                                     |
| **Entrada** 	   | - Cuenta de origen<br>-Cuenta de destino<br>-Monto del retiro                                                                                                                                                                 |
| **Resultado** 	 | 1. El sistema valida que la cuenta tiene fondos suficientes para el retiro.<br>2. Deduce el monto del saldo disponible.<br>3. Muestra mensaje de confirmación |


### R8 -  Generar reporte de cuenta

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | 	El sistema debe permitir a los usuarios generar un reporte en formato PDF que incluya el saldo actual, el historial de transacciones y otros detalles de la cuenta bancaria.                     |
| **Entrada** 	   | - Nombre de usuario<br>-Cuenta de destino<br>-Tipo de cuenta (Ahorros, Corriente, Inversión)                                                                                                                                                            |
| **Resultado** 	 | 1.  El sistema genera un archivo PDF con los detalles solicitados.<br>2. El sistema muestra un mensaje confirmando que el reporte ha sido creado y guardado exitosamente |


### R9 - Bloquear y desbloquear cuentas

| <!-- --> 	      | <!-- --> 	                                                                                                                                                                                         |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Resumen** 	   | El sistema debe permitir a los usuarios bloquear o desbloquear sus cuentas bancarias para evitar movimientos no autorizados.                                                                                      |
| **Entrada** 	   | - Nombre de usuario<br>-Tipo de cuenta (Ahorros, Corriente, Inversión)<br>-Acción (Bloquear o Desbloquear)                                                                                                                                              |
| **Resultado** 	 | 1. El sistema bloquea o desbloquea la cuenta solicitada, según la acción seleccionada.<br>2.El sistema muestra un mensaje confirmando la acción realizada. |
