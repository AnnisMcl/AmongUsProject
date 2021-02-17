# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:27:37 2020

@author: yanni
"""

'''Simple dictionnary where the nodes are the key and their values are the rooms next to them in the real map'''
graph  ={"Cafete": ["Medbay","UpperE","Storage","Admin","Weapons"],
		 "Reactor": ["UpperE","LowerE","Security"],
         "Security": ["UpperE","LowerE","Reactor"],
         "Electrical": ["LowerE","Storage"],
         "Storage": ["Electrical","LowerE","Cafete","Admin","Salle","Shield"],
         "Admin": ["Cafete","Storage"],
         "Salle": ["Storage","Shield"],
         "Medbay": ["Cafete","UpperE"],
         "UpperE": ["Cafete","Medbay","LowerE","Reactor","Security"],
         "LowerE": ["UpperE","Reactor","Security","Electrical","Storage"],
		 "Shield": ["Storage","Salle","O2","Weapons","Navigation"],
         "O2": ["Shield","Navigation","Weapons"],
         "Navigation": ["Shield","O2","Weapons"],
         "Weapons": ["Cafete","O2","Shield","Navigation"]
}

'''Hamilton's well known algorithm adapted to our situation'''
def hamilton(graph, start_v):# Since it's a known algorithm i won't explain it
  size = len(graph)
  to_visit = [None, start_v]
  path = []
  while(to_visit):
    v = to_visit.pop()
    if v : 
      path.append(v)
      if len(path) == size:
        break
      for x in set(graph[v])-set(path):
        to_visit.append(None)
        to_visit.append(x)
    else:
      path.pop()
  return path

for c in hamilton(graph,"Navigation"): #Print the list that Hamilton's algorithm gave us
	print(c,"-> ",end='')









