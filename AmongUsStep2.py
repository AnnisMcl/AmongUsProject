# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:24:26 2020

@author: yanni
"""
class Node: #Simple Node class
	'''We just need a "listVoisins" attribute and an iD'''
	def __init__(self,iD,listVoisins=[]):
		self.iD = iD
		self.listVoisins = listVoisins
	
	def __str__(self): #To have a nice display
		return str(self.iD)
	
	def printSituation(self): #In order to have a better visualization of the game
		res = ""
		for c in self.listVoisins:
			res += str(c.iD)
		return str(self.iD) + " -> " + res
	
	def __eq__(self,other): #In order to compute the equality between to nodes
		return self.iD == other.iD
	
	def voisins(self): # To get all the neighboors of a node into a string.
		res = ""
		for c in self.listVoisins:
			res += str(c.iD)
		return res
	
if __name__ == "__main__":
	
	'''Creation of 10 players'''
	p0 = Node(0)
	p1 = Node(1)
	p2 = Node(2)
	p3 = Node(3)
	p4 = Node(4)
	p5 = Node(5)
	p6 = Node(6)
	p7 = Node(7)
	p8 = Node(8)
	p9 = Node(9)
	
	'''Initialization of the neighboors list for each players'''
	p0.listVoisins = [p1,p4,p5]
	p1.listVoisins = [p0,p2,p6]
	p2.listVoisins = [p1,p3,p7]
	p3.listVoisins = [p2,p4,p8]
	p4.listVoisins = [p0,p3,p9]
	p5.listVoisins = [p0,p7,p8]
	p6.listVoisins = [p1,p8,p9]
	p7.listVoisins = [p2,p5,p9]
	p8.listVoisins = [p3,p5,p6]
	p9.listVoisins = [p4,p6,p7]
	
	'''Creation and filling of a list where all the players will be stored'''
	G = []
	G.append(p0)
	G.append(p1)
	G.append(p2)
	G.append(p3)
	G.append(p4)
	G.append(p5)
	G.append(p6)
	G.append(p7)
	G.append(p8)
	G.append(p9)
	
	print("\n\n******************************EMERGENCY MEETING******************************\n")
	joueurMort = input("Quel est le joueur que vous avez trouvé ?\n") #Ask the user which player is dead
	print("\nLe corps du joueur n°", joueurMort," à été retrouvé dans electrical, voyons voir ce que les autres joueurs ont vu.\n")
	
	for g in G: #Print for each players, the players he saw during the game
		print(g.printSituation())
	imposteurPot = G[int(joueurMort)].listVoisins #We know that the potential first impostor is in the 3 players the dead one saw before dying
	print("Il y a donc un imposteur parmis les joueurs suivants: ", G[int(joueurMort)].voisins())
	T =[]
	for c in imposteurPot:#Now we search the players who were never with the potential first impostor
		for g in G:
			if(c not in g.listVoisins and c != g and g not in imposteurPot):
				T.append([c,g])
	
	print("\nVoici les couples d'imposteur potentiels\n")
	for t in T: #Print of all the potential impostors couples
		print(t[0], "&", t[1])
	
	
			
			
			
			