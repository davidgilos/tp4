#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: plateau.py
@author:

Module qui s'occupe de dessiner l'échequier.
"""

class Plateau:
	def affichage(self):
		for i in range (0, 8):
			print(8-i, " ", end="")  # Imprime le numéro de la ligne 
			for j in range (0, 8):
				print("[ ] ", end="")  # Imprime les éléments d'une ligne
			print("\n")
		print("    1   2   3   4   5   6   7   8")  # Imprime le numéro des colones

tableau = Plateau()
tableau.affichage()
