# -*- coding: utf-8 -*-
"""
Librería de calculos de procesos industriales.
Incluye funciones reutilizables para sensores y actuadores.
"""

def consumo_por_turno(valor):
    return 8*valor

def consumo_por_dia(valor):
    return 24*valor

def consumo_total(consumo,horas):
    return consumo*horas

def salto_termico(temp_ext,temp_int):
    return temp_ext-temp_int

def horas_para_mantenimiento(valor):
    return round((10000-valor)/12)



