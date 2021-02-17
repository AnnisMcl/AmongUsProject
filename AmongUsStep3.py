# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:31:32 2020

@author: yanni
"""
#Classical Floyd Warshall's algorithm
def floydWarshall(graph,n):
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist
#Function we'll use to compute the difference between two matrix   
def diffGraph(graph1,graph2):
    graph3=[[0 for i in range (len(graph1))]for j in range(len(graph1))]
    for i in range (len(graph1)):#Go through the lines
        for j in range (len(graph1)):#The columns (but it is a sqared matrix so it doesn't matter)
            graph3[i][j]=graph1[i][j]-graph2[i][j]#Here we do the difference
    return graph3
  
if __name__ == "__main__":
    
    
    INF=9999#Just to be sure
	#Simple dictionnary whre the keys are the iD and the values are the rooms that correspond
    indexSalle={0:'cafe',1:'wea',2:'coul',3:'nav',4:'shi',5:'O2',6:'stor',7:'adm',8:'elec',9:'low',10:'reac',11:'sec',12:'upp',13:'med'}

    #We inserted the room in raws and columns by following this order:
	# cafete - weapon - coul - navigation - shield - O2 - storage - admin - electrical - lowEngine - reactor - security - upperEngine - medbay            
	#The values are the distance between rooms
    graphCrewmate= [[0  ,3  ,INF,INF,INF,INF,5  ,4  ,INF,INF,INF,INF,7  ,  6],
                    [3  ,0  ,3  ,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
                    [INF,3  ,0  ,2  ,4  ,3  ,INF,INF,INF,INF,INF,INF,INF,INF],
                    [INF,INF,2  ,0  ,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
                    [INF,INF,4  , INF,0  ,INF,5  ,INF,INF,INF,INF,INF,INF,INF],
                    [INF,INF,3  , INF,INF,0  ,INF,INF,INF,INF,INF,INF,INF,INF],
                    [5  ,INF,INF, INF,5  ,INF,0  ,4  ,6  ,8  ,INF,INF,INF,INF],
                    [4  ,INF,INF, INF,INF,INF,4  ,0  ,INF,INF,INF,INF,INF,INF],
                    [INF,INF,INF, INF,INF,INF,6  ,INF,0  ,6  ,INF,INF,INF,INF],
                    [INF,INF,INF, INF,INF,INF,8  ,INF,6  ,0  ,4  ,4  ,5  ,INF],
                    [INF,INF,INF, INF,INF,INF,INF,INF,INF,4  ,0  ,INF,4  ,INF],
                    [INF,INF,INF, INF,INF,INF,INF,INF,INF,4  ,INF,0  ,4  ,INF],
                    [7  ,INF,INF, INF,INF,INF,INF,INF,INF,5  ,4  ,4  ,0  ,6  ],
                    [6  ,INF,INF, INF,INF,INF,INF,INF,INF,INF,INF,INF,6  ,0  ]]


    #For the impostors it's slightly different because the ncan use the vents to travel between rooms.
	#We used the same order to insert the rooms into the matrix.

    graphImpostor= [[0  ,3  ,0  , INF,INF,INF,5  ,1  ,INF,INF,INF,INF,7  ,  6],
                    [3  ,0  ,3  , 0  ,INF,INF,INF,INF,INF,INF,INF,INF,INF,INF],
                    [0  ,3  ,0  , 2  ,4  ,3  ,INF,0  ,INF,INF,INF,INF,INF,INF],
                    [INF,0  ,2  , 0  ,0  ,INF,INF,INF,INF,INF,INF,INF,INF,INF],
                    [INF,INF,4  , 0  ,0  ,INF,5  ,INF,INF,INF,INF,INF,INF,INF],
                    [INF,INF,3  , INF,INF,0  ,INF,INF,INF,INF,INF,INF,INF,INF],
                    [5  ,INF,INF, INF,5  ,INF,0  ,4  ,6  ,8  ,INF,INF,INF,INF],
                    [1  ,INF,0  , INF,INF,INF,4  ,0  ,INF,INF,INF,INF,INF,INF],
                    [INF,INF,INF, INF,INF,INF,6  ,INF,0  ,6  ,INF,1  ,INF,1  ],
                    [INF,INF,INF, INF,INF,INF,8  ,INF,6  ,0  ,0  ,4  ,5  ,INF],
                    [INF,INF,INF, INF,INF,INF,INF,INF,INF,0  ,0  ,INF,0  ,INF],
                    [INF,INF,INF, INF,INF,INF,INF,INF,1  ,4  ,INF,0  ,4  ,1  ],
                    [7  ,INF,INF, INF,INF,INF,INF,INF,INF,5  ,0  ,4  ,0  ,6  ],
                    [6  ,INF,INF, INF,INF,INF,INF,INF,1  ,INF,INF,1  ,6  ,0  ],]
    
	#Print the situation
    print("\nEn tant que crewmate | Distance entre les salles\n",floydWarshall(graphCrewmate,14),"\n")
    print("\nEn tant qu'imposteur | Distance entre les salles\n",floydWarshall(graphImpostor,14),"\n")       
    print("\nDifférence de distance entre les deux rôles\n")#Now let's compute the difference
        
    diff=diffGraph(floydWarshall(graphCrewmate,14),floydWarshall(graphImpostor,14))
	#In this dictionnary I wrote the names of the rooms in a shrot way to fill in the console but it doesn't fit perfectly   
    dictSalle={0:'caf',1:'wea',2:'coul',3:'navig',4:'shi',5:'O2',6:'sto',7:'adm ',8:'elec ',9:'low  ',10:'reac',11:'sec',12:'upp',13:'med'}
    #Here we write the names of the columns
    for i in range (len(diff)):
            print(dictSalle[i],end='\t')   
	#We began to fill it		 
    for i in range (len(diff)):
        if i==0:
            print(' ')
        else:
            print(indexSalle[i-1])#Just print the index of the room
        #Let's print the distances between rooms now
        for j in range (len(diff)):
            print(diff[i][j], end='\t')
            if i==13 and j==13:
                print(indexSalle[i],end=' ')