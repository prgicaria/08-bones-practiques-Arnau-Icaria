#!usr/bin/env python

'''Divisió entera. Aquest programa fa una divisió entera de dos números

Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

Aquest programa demana dos números: dividend i divisor,
  fa una divisió entera dels dos números entrats i mostra per pantalla
 la divisio, el quocient i el residu.
'''

__author__ = "Arnau Roca-Cusachs Valls"
__email__ = "aroca-cusachs@instituticaria.cat"
__date__ = "16/10/2024"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor

print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
