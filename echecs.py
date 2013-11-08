#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: echecs.py
@author:

Fichier principale du programme
"""

import os
import sys

def main():
	os.system('clear')

	print("Bienvenu aux échecs!\nQue souhaitez-vous faire?\n")
	print("1. Lancer une nouvelle partie")
	print("2. Charger une partie sauvegardée")
	print("3. Visioner l'aide")

	choix = False

	while choix == False:
		option = input("Sélection: ")
		if option == "1":
			# Charger paramètres d'initialisation par défaut
			print("À venir")
			choix = True
		elif option == "2":
			# Charger une partie sauvegardée
			print("À venir")
			choix = True
		elif option == "3":
			# Afficher l'aide
			print("À venir")
			choix = True
		else:
			print("Sélectionnez un des choix de 1 à 3")
"""
	# Boucle principale du jeux
	try:
		while True:
			# Afficher jeux
			# Utilisateur rentre un déplacement
			# Vérification si move légal
			# Effectue les changements de positions
			# Vérifie si échec
			print("À venir")
	except echec:	 
		print("Fin de la partie")
"""

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\nÀ la prochaine!")
		sys.exit()
