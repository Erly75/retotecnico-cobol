# retotecnico-cobol
Reto técnico COBOL

## 1. Introducción:
Desarrollar una aplicación en Linea de Comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya
* Balance Final
* Transacción de Mayor Monto
* Conteo de Transacciones

## 2. Instrucciones de Ejecución:
Esta aplicacion esta hecha en Python, es necesario utilizar un entorno virtual para poder utilizar el proyecto
* Asegurarse de tener instalado Python y de tener el comando de "python" y "virtualenv" en las variables de entorno del sistema
* Asegurar de contar con Git instalado en sus sistema operativo
* Dirigirse a la ruta donde se quiere guardar el proyecto y abrir una ventana de Git Bash para clonar el proyecto con el siguiente comando: 
"git clone https://github.com/Erly75/retotecnico-cobol.git"
* Digirise a la carpeta del proyecto con el comando: 
"cd retotecnico-cobol"
* Crear el entorno virtual a través del comando:
"virtualenv -p python env"
* Desde la terminal activar el entorno virtual con el comando:
"source env/Scripts/activate"
* Instalar las librerias del proyecto para su uso con el comando:
"pip install -r requirements.txt"
* Ejecutar la aplicacion con el comando:
"python main.py"

## 3. Enfoque y Solución:
Debido a que es una aplicación no tam compleja, no vi la necesidad de utilizar en enfoque de POO para poder desarrollar la solución.
La lógica se organiza en funciones modulares que leen el archivo CSV, calculan el balance final, identifican la transacción con el mayor monto y cuentan las transacciones de cada tipo. El manejo de errores se realiza con bloques try-except, lo que asegura robustez ante fallos.
La aplicación utilizar las siguientes funciones:
* leer_csv(ruta_archivo)
* retornar_balance_final(df)
* retornar_max_transaccion(df)
* retornar_conteo_transacciones(df)
* reporte_transacciones(df)

Las 4 primeras funciones permiten devolver los resutlados aplicados a los datos, mientras que la última función permite imprimir los resutlados en pantalla donde se utilizan las otras funciones

## 4. Estructura del Proyecto
La estructura de archivos para la solución es la siguiente

retotecnico-cobol/

|-- env/                # carpeta donde se almacenan los archivos necesarios del entorno virtual

|-- .gitignore          # Archivo que especifica qué archivos y carpetas deben ser ignorados por Git (como el entorno virtual y archivos temporales).

|-- exaple.csv          # Archivo CSV de ejemplo con datos de transacciones.

|-- main.py             # Archivo principal que ejecuta la lógica de procesamiento y generación del reporte.

|-- README.md           # Documentación del proyecto con instrucciones de uso.

|-- requirements.txt    # Archivo que lista las dependencias necesarias para el proyecto.