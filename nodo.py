#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Nodo:
    def __init__(self, valor=None, sig=None):
        self.valor = valor;
        self.siguiente = sig;

    def agregar(self, valor):
        if (self.siguiente == None):
            if (self.valor == None):
                return Nodo(valor)
            else:
                return Nodo(self.valor, Nodo(valor))
        else:
            return Nodo(self.valor, self.siguiente.agregar(valor));

    def remover(self):
        if (self.siguiente == None):
            return self.valor,None
        return self.valor,self.siguiente;

    def __str__(self):
        if (self.siguiente == None):
            return str(self.valor)
        else:
            return "{},{}".format(str(self.valor), self.siguiente);

