#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Proceso:
    def __init__(self, _id, nombre, rafaga, prioridad, comando, usuario):
        self.id = _id
        self.nombre = nombre
        self.rafaga = rafaga
        self.prioridad = prioridad
        self.comando = comando
        self.usuario= usuario
        self.state = 'inactive'

    def iniciar_ejecucion(self):
        return "proceso {}: {} de usuario {} con comando {} en ejecucion".format(self.id, self.nombre, self.usuario, self.comando)

    def cambiar_estado_ejecucion(self, state, log):
        self.state = state
        if (state == "forced"):
            return "[EE] - Proceso: {} se ha cerrado de forma forzada".format(self.id)
        if (state == "error"):
            return "[EE] - Proceso: {} ha generado un error: {} - cerrando".format(self.id,log)
        if (state == "suspend user"):
            return "[INF] - Proceso: {} pasa a estado suspendido".format(self.id)
        if (state == "suspend timeout"):
            return "[INF] - Proceso: {} pasa a estado suspendido por que agotó su tiempo".format(self.id)
        if (state == "list process"):
            return "[INF] - Proceso: {} se ha pasado a estado listo".format(self.id)
        if (state == "blocked"):
            return "[WN] - Proceso: {} se pasara a estado bloqueado por {}".format(self.id, log)
        if (state == "suspend blocked"):
            return "[WN] - Proceso: {} - Debido a un incidente - {} - el proceso pasara estado Suspendido bloqueado".format(self.id, log)
        if (state == "inactive"):
            return "[INF] - Proceso: {} - Proceso Apagado"
