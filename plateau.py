#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
@file: board.py
@author:

Module qui s'occupe de dessiner l'échequier.
"""

def draw():
	for i in range (0, 8):
		print(8-i, " ", end="")
		for j in range (0, 8):
			print("[ ] ", end="")
		print("\n")
	print("    1   2   3   4   5   6   7   8")
draw()
