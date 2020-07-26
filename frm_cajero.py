#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dependencias
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class frm_cajero(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Banco")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.connect("destroy", Gtk.main_quit)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

    def run(self):
        self.show_all()

win = frm_cajero()
win.run()
Gtk.main()
