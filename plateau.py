#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: plateau.py
@author:

Module qui s'occupe de dessiner l'échequier.
"""

from tour import Tour

class Plateau:   
    def __init__(self):
		
    #    Initialise le plateau avec un damier vide
    #    self.damier = {(0,0):Tour(0,0,0), (0,7):Tour(0,7,0), (7,0):Tour(7,0,1), (7,7):Tour(7,7,1)}
    
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
							

    def getPiece(self,line,col):
        #Retourne la piece à la position (line,col) ou None sinon
        return self.damier.get((line,col))
#  Identique a :        
#        if (line,col) in self.damier.keys() :
#            return self.damier[(line,col)]
#        else:
#            return None


    def affichage(self):

		# Représentation graphique des pièces
        PIECE_BLANC = {
	   		        	"Roi": 	    "♚",
						"Dame":     "♛",
						"Tour":     "♜",
						"Fou":      "♝",
						"Cavalier": "♞",
						"Pion":     "♟"
					 }  
        PIECE_NOIR = {
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
                if (x,y) in self.pieces_blanc:  # Vérifie si la case contient une pièce blanche
                    print("[" + PIECE_BLANC[self.pieces_blanc[x,y]] + "] ", end="")  # Imprime la pièce.  Le + assure qu'il n'y a pas d'espace d'inserré des deux côtés de la figure
                elif (x,y) in self.pieces_noir:  # Vérifie si la case contient une pièce noire
                    print("[" + PIECE_NOIR[self.pieces_noir[x,y]] + "] ", end="")  # Imprime la pièce		
                else:
                    print("[ ] ", end="")  # Aucune pièce présente, case vide
            print("\n")
        print("    1   2   3   4   5   6   7   8")  # Imprime le numéro des colones

tableau = Plateau()
tableau.affichage()
