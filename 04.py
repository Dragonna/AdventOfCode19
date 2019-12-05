# Advent of Code - 04

# Init
possible=list()
possible2=list()

def Doublet(nombre):
	for x in range(0,len(str(nombre))-1):
		if str(combo)[x]==str(combo)[x+1]:
			return True
	return False

def VraiDoublet(nombre):
	for x in range(0,len(str(nombre))-1):
		if str(combo)[x]==str(combo)[x+1]:
			if str(combo)[x]*3 not in str(combo):
				return True
	return False

def Croissant(nombre):
	for x in range(0,len(str(nombre))-1):
		if int(str(combo)[x]) > int(str(combo)[x+1]):
			return False
	return True

# partie 1
# six chiffres, >input[0], <input[1], combo[x,x+1] pareil, for x in combo[:-1], combo[x+1]>x
for combo in range(307237,769058):
	#six chiffres
	if len(str(combo))!=6:
		break
	if Doublet(combo)==True and Croissant(combo)==True:
		possible.append(combo)
print(len(possible))
		
# partie 2
# six chiffres, >input[0], <input[1], combo[x,x+1] pareil, mais différent de combo[x+2], for x in combo[:-1], combo[x+1]>x
for combo in range(307237,769058):
	#six chiffres
	if len(str(combo))!=6:
		break
	if VraiDoublet(combo)==True and Croissant(combo)==True:
		possible2.append(combo)
print(len(possible2))