from modulos.lectura_datos import * 
from modulos.muestreo_datos import * 
from modulos.calculos import *

operario,fecha,hora=login()
while True:
    entrada=int(input("\n\t1 - Ver datos del sistema\n\t2 - Introducir nuevos datos manualmente\n\t3 - Salir del sistema\n"))
    match entrada:
        case 1:
            temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire=leer_datos_plc()
            muestra_proceso(temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire)
        case 2:
            temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire=introduccion_Datos()
            muestra_proceso(temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire)
        case 3:
            saliendo()
    if entrada==3:
            break
    registro_log(fecha,hora,operario,temperatura_sala,temperatura_exterior,temperatura_motor,humedad_sala,presion_aire,velocidad_ventilador,consumo_kw,vibracion_motor,contador_horas,estado_sistema,modo_operacion,alarma_activa,sensor_filtro,nivel_ruido,flujo_aire)

