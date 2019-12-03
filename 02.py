# Advent of Code - 02

# Init
numbers=list()

# input
with open('02.txt', 'r') as input:
	for line in input:
		for number in line.split(","):
			if '\n' in number:
				numbers.append(int(number[:-1]))
			else:
				numbers.append(int(number))

# partie 1
def part_1(x,y,data):
	data[1]=x
	data[2]=y
	for counter in range(0,len(data),4):
		try:
			if data[counter] == 1:
				data[data[counter+3]] = data[data[counter+1]] + data[data[counter+2]]
			elif data[counter] == 2:
				data[data[counter+3]] = data[data[counter+1]] * data[data[counter+2]]
			elif data[counter] == 99:
				#print("Opcode 99, fin du programme")
				break
			else:
				#print("Opcode non reconnu, fin du programme")
				break
		except:
			#print("Problème d'indice, fin du programme")
			break
	return data[0]
print(part_1(12,2,numbers.copy()))

# partie 2
# data[0] = 19690720
for x in range(0,100):
	for y in range(0,100):
		if part_1(x,y,numbers.copy()) == 19690720:
			print(x)
			print(y)
			print(100*x+y)
			break

