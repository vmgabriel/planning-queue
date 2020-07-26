#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dependencias
from nodo import Nodo
from proceso import Proceso

class Cpu:
    def __init__(self):
        self.mensaje_inicio()

        # Bloque de control de proceso
        self.listo = Nodo()
        self.ejecucion = Nodo()
        self.bloqueado = Nodo()
        self.suspendido_listo = Nodo()
        self.suspendido_bloqueado = Nodo()

        print("------------------------")
        print("Iniciando Sesion")

        # Carga de Procesos Prioritarios Basicos
        crear_procesos_nuevos("Alta", "root", 3)
        print("-------------------------")

    def cargar(self):
        pass

    def procesos(self):
        pass

    def carga_kernel(self):


    def mensaje_inicio(self):
        print ("---------------------")
        print ("Bienvenido al Kernel")
        print ("---------------------")
        print ("Iniciando bloque de control de proceso")

    def crear_procesos_nuevos(self, prioridad, usuario, cant):
        for i in range(0:cant):
            if (prioridad == 'Alta'):
                self.listo = self.listo.agregar(Proceso(random(1.1, 999999.89), "proceso-" + i, 7500, prioridad, 'comando - proceos - service', usuario))
            if (prioridad == 'Media'):
                self.listo = self.listo.agregar(Proceso(random(1.1, 999999.99), "proceso-medio-"+i, 3400, prioridad, 'comm- proceso - service - medio', usuario))
            if (prioridad == "Baja"):
                self.listo = self.listo.agregar(Proceso(random(1.1, 999999.99), "Proceso-Bajo-"+i, 1200, prioridad, "systemctl start service basic", usuario))

    def mensaje_fin(self):
        print ("-----------------------")
        print ("Cerrando Sesion")
        print ("-----------------------")
        print ("Apagando SO")
        print ("-----------------------")
