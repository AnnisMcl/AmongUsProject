# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:35:04 2020

@author: yanni
"""

''' Global plan '''
#Create a 100players AVL Tree based on their ranking
#Create 10 lists lobbies and fill them with players sorted by their ranking
#Play 3 games
#Reinsert each player of each lobby in the global tree
#Pop the last 10players of the tree
#Create 9 lists lobbies and play 3 games, then eject the last 10, etc...
#It remains 10players
#Reinitialize all scores
#Play 5 games
#Give the podium

'''Code plan'''
#Create a Player class
    #name
	#val
    #left
    #right
#Create a AVL tree class
	#root

import random #We will need this library in order to give a random score to each players at the end of a game
COUNT = [10] # We will use it later in order to have a well displayed tree

'''My Player class isn't complex at all just the classic node's attribute (left right height val), we chose to add a name'''
class Player():
	def __init__(self,val, name="Default",scoreTab = []):
		self.name = name
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

	def __str__(self) : # To have a good display
		return self.name + " : " + str(self.val)
	'''Those are sepcific methods that will help us to compare two players'''
	def __lt__(self,other):
		return (self.val < other.val)
	
	def __gt__(self,other):
		return (self.val > other.val)
	
	def __le__(self,other):
		return (self.val <= other.val)
	
	def __ge__(self,other):
		return (self.val >= other.val)
	
	def __eq__(self, other):
		return self.val == other.val
	
class AVL_Tree():#Here we don't need any attribute
		
	def insertAVL(self, root, player): #Classic insert function for an AVL tree
	#I won't explain the AVL's well known meethods but i'll explain those we created
		if not root:
		    return player
		
		if player >= root:
			root.right = self.insertAVL(root.right, player) 
		else:
			root.left = self.insertAVL(root.left, player) 
		 
		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		 
		balance = self.getBalance(root) 

		if balance > 1 and player <= root.left: 
			return self.rightRotate(root) 

		 
		if balance < -1 and player >= root.right: 
			return self.leftRotate(root) 

		
		if balance > 1 and player > root.left: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		
		if balance < -1 and player < root.right: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root
	
	def delete(self, root, player):
		
		if not root:
			return root
		elif player.val < root.val:
			root.left = self.delete(root.left, player)
		elif player.val > root.val:
			root.right = self.delete(root.right, player)
		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp
			temp = self.minTree(root.right)
			root.val = temp.val
			root.right = self.delete(root.right, temp)
		
		if root is None:
			return root
		
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		
		balance = self.getBalance(root)
		
		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)
		
		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)
		
		if balance > 1 and self.getBalance(root.left) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)
		
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)
		return root

	
	def leftRotate(self, z):
		y = z.right
		T2 = y.left
		y.left = z
		z.right = T2
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
		
		return y
	
	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		
		y.right = z 
		z.left = T3 

		
		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 

		
		return y
	
	def getHeight(self, root): 
		if not root: 
			return 0
		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0
		return self.getHeight(root.left) - self.getHeight(root.right)
	
	'''Different ways to travel through the tree '''
	def preOrder(self,root):
		if not root:
			return
		print(str(root.val) + " ", end="")
		self.preOrder(root.left)
		self.preOrder(root.right)
		
	def inOrder(self,root):
		if not root:
			return
		self.inOrder(root.left)
		print(str(root.val) + " ", end="")
		self.inOrder(root.right)
		
	def postOrder(self, root):
		if not root:
			return
		self.postOrder(root.left)
		self.postOrder(root.right)
		print(str(root.val) + " ", end="")
	
	def recupList(self,root):#This function seems weird but i did that in order to return a list while trave the tree with a recursive function
		L = []
		
		def inOrderList(root):#Simple inOrder function but we append the node to the list L
			if not root:
				return
			inOrderList(root.left)
			L.append(root)
			inOrderList(root.right)
		inOrderList(root)
		return L
	
	def minTree(self,root):#In order to find the child with the lowest score
		if not root:
			return
		if not root.left:
			return root
		else:
			return self.minTree(root.left)
	
	def maxTree(self,root):#For the higher score
		if not root:
			return
		if not root.right:
			return root
		else:
			return self.maxTree(root.right)

	
	'''We're not in the class anymore'''
	
def displayUtil(root,space): #I found this funciton on the internet, it just help us to have a well displayed Tree
	if not root:
		return
	space += COUNT[0]
	displayUtil(root.right,space)
	
	print()
	for i in range(COUNT[0],space):
		print(end=" ")
	print(root.val)
	
	displayUtil(root.left,space)

def display(root): #We use this function to display a tree with its root in paramater
	displayUtil(root,0)


if __name__ == "__main__":
	
	players = [] # Our global list where all the players will be append after being in the global AVL tree
	nombreJoueursVoulu = 100 #This will decreased by 10 after each rounds of 3 games
	
	for i in range(100): #◘Initilization of the 100 players with a score of 0
		players.append(Player(0,"Player n°" + str(i)))
		
		
	for i in range (9): #Game Loop # The 9 first rounds
		
		#Reintilaization of the players' children
		for c in players:
			c.left = None
			c.right = None
			

		lobbies = [[]]*(nombreJoueursVoulu//10) #Creation of the 10 (then 9, then 8, etc) lobbies
		roots = [None]*(len(lobbies)) # Creation of the 10 roots
		'''Those two variables are here to split the global list into different lobbies of 10 players'''
		d=0 
		f=10
	
		for i in range(len(lobbies)):
			lobbies[i] = players[d:f] #Here we split the global list

			d += 10
			f += 10
			
		for i in range(len(lobbies)): # Go through the lobbies
			for j in range (len(lobbies[i])): #For each players we play 3 games and give a random score for each game
				game1 = random.randint(0,100)
				game2 = random.randint(0,100)
				game3 = random.randint(0,100)
				moy = round((game1+game2+game3)/3,6) #Simple mean
				if(lobbies[i][j].val == 0):#If it's the first game
					lobbies[i][j].val = moy
				else:#If it's not
					temp = lobbies[i][j].val
					lobbies[i][j].val = round((temp+moy)/2,6) #This is not the right way to compute a mean BUT as long it's proportional between all the players it still working as a score
		
		myTree = AVL_Tree() #Re-creation of the global AVL tree
		root = None #Ans also his root
	
		for c in players: #We insert all the players into the global AVL tree
			root = myTree.insertAVL(root,c)
		#display(root) #Debug

		for i in range (10): #Here we delete the last 10players
			playerDelete = myTree.minTree(root) #We get the player who has the lowest score
			root = myTree.delete(root, playerDelete) #We delete him

		#display(root) #To debug
		players = myTree.recupList(root)
		print("Nombre de joueurs:",len(players),"(Après élimination)")
		display(root)
		
		nombreJoueursVoulu -= 10

	
	
	'''Here we're not in the global loop anymore'''
	myTree = AVL_Tree()
	root = None
		
	#Total reinitialization of the ten best players
	for c in players :
		c.left = None
		c.right = None
		c.val = 0
	#Playing the last 5games
	for c in players:
		game1 = random.randint(0,12)
		game2 = random.randint(0,12)
		game3 = random.randint(0,12)
		game4 = random.randint(0,12)
		game5 = random.randint(0,12)
		moy = round((game1+game2+game3+game4+game5)/5,6) # Simple mean of the 5 games
		c.val = moy
		
	for c in players: #Insertion of all the players into the global AVL tree
		root = myTree.insertAVL(root,c)
	
	print("\n*******************************PODIUM*******************************\n")
	

	players = myTree.recupList(root) #Get all the players from the tree with an inOrder function
	for i in range (1,len(players)+1):
		print(i,"->",players[-i]) #Print in a reverse way this list
	