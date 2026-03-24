from config.constantes import *

def validarTemperaturaSala(variable):
    if variable>TEMP_MAX or variable<TEMP_MIN:
        return "ALERTA Temperatura fuera de rango"
    return "OK"

def validarHumedad(variable):
    if variable>HUMEDAD_MAX or variable<HUMEDAD_MIN:
       return "ALERTA Humedad fuera de rango"
    return "OK"

def validarVelocidadVentilador(variable):
    if variable>VELOCIDAD_MAX or variable<VELOCIDAD_MIN:
        return "ALERTA Velocidad fuera de rango"
    return "OK"

def validarVibracion(variable):
    if variable>VIBRACION_MAX or variable<VIBRACION_MIN:
        return "ALERTA Vibracion excesiva"
    return "OK"




