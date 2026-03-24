from config.constantes import *

def validarTemperaturaSala(variable):
    if variable>TEMP_MAX or variable<TEMP_MIN:
        print("ALERTA Temperatura fuera de rango")
        return "nOK"
    return "OK"

def validarHumedad(variable):
    if variable>HUMEDAD_MAX or variable<HUMEDAD_MIN:
        print("ALERTA Humedad fuera de rango")
        return "nOK"
    return "OK"



def validarVelocidadVentilador(variable):
    if variable>VELOCIDAD_MAX or variable<VELOCIDAD_MIN:
        print("ALERTA Velocidad fuera de rango")
        return "nOK"
    return "OK"

def validarVibracion(variable):
    if variable>VIBRACION_MAX or variable<VIBRACION_MIN:
        print("ALERTA Velocidad fuera de rango")
        return "nOK"
    return "OK"




