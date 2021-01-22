#!/usr/bin/env python3

from rich import print
from w3c.tipos import GeneradorCantidadTotalConTiposSimples
import pretty_errors

cantidad=GeneradorCantidadTotalConTiposSimples.get()

print(cantidad.get_descripcion_textual())