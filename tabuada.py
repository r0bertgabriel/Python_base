#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1

"""

__version__ = "0.1.0"

__author__ = "r0bert"

# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("------------------------")
