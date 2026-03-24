from .calculos import *
from .validacion import *


def muestra_proceso(temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire):
    print("-----------------------------------")
    print("        DATOS DEL PROCESO")
    print("-----------------------------------\n\n")    
    print(f"Temperatura de la sala:\t {temperatura_sala}")
    print(f"Temperatura del exterior:\t {temperatura_exterior}")
    print(f"Temperatura del motor:\t {temperatura_motor}")

    print(f"Humedad de la sala:\t {humedad_sala}")
    print(f"Presion del aire:\t {presion_aire}")
    print(f"Velocidad ventilador:\t {velocidad_ventilador}")
    print(f"Flujo de aire:\t {flujo_aire}")
    print(f"Nivel de ruido:\t {nivel_ruido}")
    print(f"Sensor de filtro:\t {sensor_filtro}")

    if alarma_activa:
        print("Tiene alarmas\t ACTIVAS")
    else:
        print("Sin Alarmas")
    print(f"Modo de operacion:\t {modo_operacion}")
    print("\n\n-----------------------------------")
    print("        COMPROBACION DE SEGURIDAD")
    print("-----------------------------------\n\n")
    print(f"Temperatura de la sala:\t {validarTemperaturaSala(temperatura_sala)}")
    print(f"Humedad de la sala:\t {validarHumedad(humedad_sala)}")
    print(f"Velocidad del ventilador:\t {validarVelocidadVentilador(velocidad_ventilador)}")
    print(f"Vibracion del motor:\t {validarVibracion(vibracion_motor)}")
    print("\n\n-----------------------------------")
    print("        CALCULOS DEL SISTEMA")
    print("-----------------------------------\n\n")
    print(f"Salto Termico:     {salto_termico(temperatura_exterior,temperatura_sala)} %")
    print(f"Consumo estimado por turno (8h):     {consumo_por_turno(consumo_kw)} kwh")
    print(f"Consumo estimado diaria (24h):     {consumo_por_dia(consumo_kw)} kwh")
    print(f"Consumo total:     {consumo_total(consumo_kw,contador_horas)} kwh")
    print("\n\n----------------------------------------")
    print("        ESTADO GENERAL DEL SISTEMA")
    print("----------------------------------------\n\n")
    print(f"Sistema Activo: {estado_sistema}\n")

def saliendo():
    print("\nSaliendo del sistema...\nPrograma finalizado")

def registro_log(fecha,hora,operario,temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire):
    archivo=open("./logs/registro.txt","a")
    contenido=f"[{fecha} {hora}]\nOperario: {operario}\nTemp sala: {temperatura_sala}\nTemp ext: {temperatura_exterior}\nTemp Motor: {temperatura_motor}\nHumedad: {humedad_sala}\nPresion: {presion_aire}\nVelocidad ventilador: {velocidad_ventilador} \nConsumo: {consumo_kw} kw\nVibracion motor: {vibracion_motor}\n Contador horas: {contador_horas} h\nEstado: {estado_sistema}\nModo operacion: {modo_operacion}\nalarmas: {alarma_activa}\nSensor filtro: {sensor_filtro}\nNivel ruido: {nivel_ruido}\nFlujo aire: {flujo_aire}\n----------------------------------------------------\n\n"
    archivo.write(contenido)
    archivo.close()
    print("\n----------------------------------------\nRegistro actualizado correctamente\nDatos guardados en logs/registro.txt\n----------------------------------------\n")
