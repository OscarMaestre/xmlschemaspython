#!/usr/bin/env python3

from rich import print
from w3c.tipos import *
import pretty_errors

for i in range(0,2):
    cantidad=GeneradorCantidadTotalConTiposSimples.get()
    print(cantidad.get_descripcion_textual())

e_entre_20_y_30=ElementoRestriccionEnTipoNumerico("edad", "xsd:integer")
e_entre_20_y_30.set_maximo(40)
e_entre_20_y_30.set_minimo(20)
print(e_entre_20_y_30.get_descripcion_textual(), e_entre_20_y_30.get_xml_schema())