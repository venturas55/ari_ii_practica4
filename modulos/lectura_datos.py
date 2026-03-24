import json
from .calculos import *
from .validacion import *

def login():
    operario=input("Introduzca nombre de operario")
    fecha=input("Introduzca la fecha dd/mm/yyyy")
    hora=input("Introduzca la hora en formato hh:mm")

    print("\n===================SISTEMA DE MONITORIZACION=================\n\n")
    print(f"Operario: {operario}")
    print(f"Fecha: {fecha}")
    print(f"Hora: {hora}\n")
    return operario,fecha,hora
    
def leer_datos_plc():
    archivo=open("datos/sensores.json","r", encoding="utf-8")
    datos = json.load(archivo)

    temperatura_sala = float(datos['temperatura_sala'])
    temperatura_exterior = float(datos['temperatura_exterior'])
    temperatura_motor = float(datos['temperatura_motor'])

    humedad_sala = float(datos['humedad_sala'])
    presion_aire = float(datos['presion_aire'])

    velocidad_ventilador = int(datos['velocidad_ventilador'])
    consumo_kw = float(datos['consumo_kw'])

    vibracion_motor = float(datos['vibracion_motor'])

    contador_horas = int(datos['contador_horas'])

    estado_sistema = datos['estado_sistema']
    modo_operacion = datos['modo_operacion']
    alarma_activa = datos['alarma_activa']

    sensor_filtro = datos['sensor_filtro']
    nivel_ruido = float(datos['nivel_ruido'])
    flujo_aire = float(datos['flujo_aire'])

    archivo.close()
    return temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire

def traducir_booleanos(estado_sistema, modo_operacion, alarma_activa, sensor_filtro):
    estado_sistema = str(estado_sistema).lower() == 's'
    modo_operacion = 'automatico' if str(modo_operacion).lower() == 'a' else 'manual'
    alarma_activa = str(alarma_activa).lower() == 's'
    sensor_filtro = str(sensor_filtro).lower() == 's'
    return estado_sistema, modo_operacion, alarma_activa, sensor_filtro

def introduccion_Datos():
    print("====INTRODUCCION MANUAL DE DATOS=====\n")
    temperatura_sala = float(input("Introduzca temperatura sala"))
    temperatura_exterior = float(input("Introduzca temperatura exterior"))
    temperatura_motor = float(input("Introduzca temperatura motor"))

    humedad_sala = float(input("Introduzca humedad sala"))
    presion_aire = float(input("Introduzca presion sala"))

    velocidad_ventilador = int(input("Introduzca velocidad ventilador"))
    consumo_kw = float(input("Introduzca consumo kw"))

    vibracion_motor = float(input("Introduzca vibracion"))

    contador_horas = int(input("Introduzca contador de horas"))

    estado_sistema = input("Introduzca estado del sistema (s/n)")
    modo_operacion = input("Introduzca modo de operacion (a)utomatico")
    alarma_activa = input("Introduzca si existen alarmas (s/n)")

    sensor_filtro = input("Introduzca sensor de filtro (s/n)")
    nivel_ruido = float(input("Introduzca nivel de ruido"))
    flujo_aire = float(input("Introduzca flujo de aire"))
    
    print("\n")
    return temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire

