#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: plateau.py
@author:

Module qui s'occupe de dessiner l'échequier.
"""

class Plateau:   
	def __init__(self):
	
		# Le nom des pièces dans le dictionnaire sera changé pour la classe de la pièce
		self.pieces_noir = {
						        (7,0): "Tour",
								(7,1): "Cavalier",
								(7,2): "Fou",
								(7,3): "Dame",
								(7,4): "Roi",
								(7,5): "Fou",
								(7,6): "Cavalier",
								(7,7): "Tour",	
						        (6,0): "Pion", 
							    (6,1): "Pion",
							    (6,2): "Pion",
							    (6,3): "Pion",
								(6,4): "Pion",
								(6,5): "Pion",
								(6,6): "Pion",
								(6,7): "Pion"
						   }
		self.pieces_blanc = {
							    (0,0): "Tour",
								(0,1): "Cavalier",
								(0,2): "Fou",
								(0,3): "Dame",
								(0,4): "Roi",
								(0,5): "Fou",
								(0,6): "Cavalier",
								(0,7): "Tour",
								(1,0): "Pion",
								(1,1): "Pion",
								(1,2): "Pion",
								(1,3): "Pion",
								(1,4): "Pion",
								(1,5): "Pion",
								(1,6): "Pion",
								(1,7): "Pion"
							}


	def affichage(self):

		# Représentation graphique des pièces
		PIECE_NOIR = {
    		        	"Roi": 	    "♚",
       		 	      	"Dame":     "♛",
           		 	  	"Tour":     "♜",
           		   		"Fou":      "♝",
 	            	 	"Cavalier": "♞",
   		         	  	"Pion":     "♟"
					 }  
		PIECE_BLANC = {
					   	"Roi":      "♔",
   	   		         	"Dame":     "♕",
   	       		     	"Tour":     "♖",
   	            		"Fou":      "♗",
   	           		 	"Cavalier": "♘",
   	         		   	"Pion":     "♙"
				 	  }

		for x in range (0, 8):
			print(8-x, " ", end="")  # Imprime le numéro de la ligne 
			for y in range (0, 8):
				if (x,y) in self.pieces_blanc:
					print("[" + PIECE_BLANC[self.pieces_blanc[x,y]] + "] ", end="")  # Le + assure qu'il n'y a pas d'espace d'inserré des deux côtés de la figure
				elif (x,y) in self.pieces_noir:
					print("[" + PIECE_NOIR[self.pieces_noir[x,y]] + "] ", end="")		
				else:
					print("[ ] ", end="")  # Imprime les éléments d'une ligne
			print("\n")
		print("    1   2   3   4   5   6   7   8")  # Imprime le numéro des colones

tableau = Plateau()
tableau.affichage()
