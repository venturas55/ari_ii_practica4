import json
import random
import time

ARCHIVO = "datos/sensores.json"

def generar_datos():

    datos = {

        "temperatura_sala": round(random.uniform(19, 26), 1),
        "temperatura_exterior": round(random.uniform(0, 40), 1),
        "temperatura_motor": round(random.uniform(19, 80), 1),

        "humedad_sala": round(random.uniform(45, 80), 1),
        "presion_aire": round(random.uniform(0.9, 1.5), 2),

        "velocidad_ventilador": random.randint(1300, 1500),
        "consumo_kw": round(random.uniform(7, 8), 2),

        "vibracion_motor": round(random.uniform(0.5, 1.5), 1),

        #"contador_horas": round(random.uniform(2000, 4000), 0),

        "estado_sistema": random.choice([True, True, True, False]),
        "modo_operacion": random.choice(["automatico", "manual"]),
        "alarma_activa": random.choice([False, False, False, True]),

        "sensor_filtro": random.choice([False, False, True, True]),
        "nivel_ruido": round(random.uniform(55, 75), 1),
        "flujo_aire": round(random.uniform(340, 360), 1),
    }

    return datos

while True:

    datos = generar_datos()

    with open(ARCHIVO, "r+") as archivo:
        contenido=json.load(archivo)
        datos['contador_horas']=int(contenido['contador_horas'])+1
        archivo.seek(0) #vuelve a indice inicial
        json.dump(datos, archivo, indent=4)
        archivo.truncate() #eliminar sobrante

    print("Datos actualizados")

    time.sleep(1)

