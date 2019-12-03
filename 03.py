# Advent of Code - 03

# Init
path=list()
path.append(list())
path[0].append([0,0]) # coordonnées (x,y)
path.append(list())
path[1].append([0,0])
ctr=0

# input
with open('03.txt', 'r') as input:
	for line in input:
		for direction in line.split(","):
			if '\n' in direction:
				direction=direction[:-1]
			if direction[0]=="U":
				for x in range(0,int(direction[1:])):
					path[ctr].append([path[ctr][-1][0],path[ctr][-1][1]+1])
			elif direction[0]=="R":
				for x in range(0,int(direction[1:])):
					path[ctr].append([path[ctr][-1][0]+1,path[ctr][-1][1]])
			elif direction[0]=="D":
				for x in range(0,int(direction[1:])):
					path[ctr].append([path[ctr][-1][0],path[ctr][-1][1]-1])
			elif direction[0]=="L":
				for x in range(0,int(direction[1:])):
					path[ctr].append([path[ctr][-1][0]-1,path[ctr][-1][1]])
		ctr+=1

# intersections
intersections=(set(tuple(x) for x in path[0])).intersection(set(tuple(x) for x in path[1]))

# partie 1
man_distances=list()
for x in intersections:
	if x[0]+x[1]!=0: # pas l'origine
		man_distances.append(x[0]+x[1])
print(min(man_distances))

# partie 2
oth_distances=list()
for x in intersections:
	if x[0]+x[1]!=0: # pas l'origine
		oth_distances.append(path[0].index([x[0],x[1]]) + path[1].index([x[0],x[1]]))
print(min(oth_distances))