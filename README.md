# ari_ii_practica4
Proceso industrial: Sistema HVAC industrial (climatización de nave industrial)
Descripción del sistema
En una nave industrial se utiliza un sistema HVAC (Heating, Ventilation and Air Conditioning) para controlar la temperatura, humedad y calidad del aire del edificio.
Este sistema incluye ventiladores, compresores, sensores de temperatura y sensores de flujo de aire.
Tu programa debe simular un sistema de supervisión de climatización industrial similar a los que se utilizan en edificios industriales o centros de datos.
El programa deberá realizar las siguientes tareas:
1.	Solicitar el nombre del operario que supervisa el sistema HVAC.
2.	Leer el archivo JSON que contiene los datos de sensores del sistema.
3.	Mostrar en pantalla todos los valores del sistema junto con fecha, hora y nombre del operario.
4.	Permitir al usuario elegir entre visualizar datos del sistema o introducir valores manualmente para simular diferentes condiciones.
5.	Validar que parámetros como temperatura de la sala, humedad o velocidad del ventilador estén dentro de rangos seguros.
6.	Si algún sensor supera el rango permitido, el programa deberá mostrar un mensaje de alarma.
7.	Calcular valores adicionales como:
    o	diferencia entre temperatura exterior e interior
    o	consumo energético estimado.
8.	Mantener el sistema funcionando mediante un bucle continuo de supervisión.
9.	Guardar información relevante en un archivo de registro (log).
10.	Organizar el programa en módulos y generar finalmente un ejecutable del sistema.



El contador de horas en el simulador_plc.py se ha modificado para que vaya incrementando de a uno, siempre.



##REALIZAR EJECUTABLE
Instalar pyinstaller con:   python -m pip install pyinstaller
Ejecutarlo correctamente:   python -m PyInstaller --onefile main.py
Comprobar instalacion :     python -m PyInstaller --version


CREAR EL EJECUTABLE CON:
    python -m PyInstaller --onefile --name HVAC --icon assets\icono.ico  --add-data "datos/sensores.json;datos" --add-data "logs/registro.txt;registro"  main.py 

Y copiarlo en el raiz, al mismo nivel que main.py para que funcione el acceso a archivos.
En la lectura por teclado, se tratan las variables True/False o automatico/manual con una nueva funcion