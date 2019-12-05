# Advent of Code - 05

# Init
numbers=list()

# input
with open('05.txt', 'r') as input:
	for line in input:
		for number in line.split(","):
			if '\n' in number:
				numbers.append(int(number[:-1]))
			else:
				numbers.append(int(number))

# partie 1
def part_1(input_value,data):
	counter=0
	while counter < len(data):
		#try:
		#	print(data[counter:counter+6])
		#except:
		#	print("too close to the end of the data to print!")
		try:
			if str(data[counter])[-2:] == "01" or str(data[counter])[-2:] == "1":
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				try:
					p2=int(str(data[counter])[-4])	
				except:
					p2=0
				if p1==0:
					if p2==0:
						data[data[counter+3]] = data[data[counter+1]] + data[data[counter+2]]
					elif p2==1:
						data[data[counter+3]] = data[data[counter+1]] + data[counter+2]
				elif p1==1:
					if p2==0:
						data[data[counter+3]] = data[counter+1] + data[data[counter+2]]
					elif p2==1:
						data[data[counter+3]] = data[counter+1] + data[counter+2]
				counter=counter+4
			elif str(data[counter])[-2:] == "02" or str(data[counter])[-2:] == "2":
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				try:
					p2=int(str(data[counter])[-4])
				except:
					p2=0
				if p1==0:
					if p2==0:
						data[data[counter+3]] = data[data[counter+1]] * data[data[counter+2]]
					elif p2==1:
						data[data[counter+3]] = data[data[counter+1]] * data[counter+2]
				elif p1==1:
					if p2==0:
						data[data[counter+3]] = data[counter+1] * data[data[counter+2]]
					elif p2==1:
						data[data[counter+3]] = data[counter+1] * data[counter+2]
				counter=counter+4
			elif str(data[counter])[-2:] == "03" or str(data[counter])[-2:] == "3":
				# prend input et le met à la position indiquée par le paramètre
				data[data[counter+1]] = input_value
				counter=counter+2
			elif str(data[counter])[-2:] == "04" or str(data[counter])[-2:] == "4":
				# output la valeur à la position indiquée par le paramètre
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				if p1==0:
					output_value=data[data[counter+1]]
				elif p1==1:
					output_value=data[counter+1]
				counter=counter+2
			elif str(data[counter])[-2:] == "05" or str(data[counter])[-2:] == "5": #jump if true
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				try:
					p2=int(str(data[counter])[-4])
				except:
					p2=0
				if p1==0:
					if p2==0:
						if data[data[counter+1]] != 0:
							counter = data[data[counter+2]]
						else:
							counter=counter+3
					elif p2==1:
						if data[data[counter+1]] != 0:
							counter = data[counter+2]
						else:
							counter=counter+3
				elif p1==1:
					if p2==0:
						if data[counter+1] != 0:
							counter = data[data[counter+2]]
						else:
							counter=counter+3
					elif p2==1:
						if data[counter+1] != 0:
							counter = data[counter+2]
						else:
							counter=counter+3
			elif str(data[counter])[-2:] == "06" or str(data[counter])[-2:] == "6": #jump if false
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				try:
					p2=int(str(data[counter])[-4])
				except:
					p2=0
				if p1==0:
					if p2==0:
						if data[data[counter+1]] == 0:
							counter = data[data[counter+2]]
						else:
							counter=counter+3
					elif p2==1:
						if data[data[counter+1]] == 0:
							counter = data[counter+2]
						else:
							counter=counter+3
				elif p1==1:
					if p2==0:
						if data[counter+1] == 0:
							counter = data[data[counter+2]]
						else:
							counter=counter+3
					elif p2==1:
						if data[counter+1] == 0:
							counter = data[counter+2]
						else:
							counter=counter+3
			elif str(data[counter])[-2:] == "07" or str(data[counter])[-2:] == "7": #less than
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				try:
					p2=int(str(data[counter])[-4])
				except:
					p2=0
				if p1==0:
					if p2==0:
						if data[data[counter+1]] < data[data[counter+2]]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
					elif p2==1:
						if data[data[counter+1]] < data[counter+2]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
				elif p1==1:
					if p2==0:
						if data[counter+1] < data[data[counter+2]]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
					elif p2==1:
						if data[counter+1] < data[counter+2]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
				counter=counter+4
			elif str(data[counter])[-2:] == "08" or str(data[counter])[-2:] == "8": #equals
				try:
					p1=int(str(data[counter])[-3])
				except:
					p1=0
				try:
					p2=int(str(data[counter])[-4])
				except:
					p2=0
				if p1==0:
					if p2==0:
						if data[data[counter+1]] == data[data[counter+2]]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
					elif p2==1:
						if data[data[counter+1]] == data[counter+2]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
				elif p1==1:
					if p2==0:
						if data[counter+1] == data[data[counter+2]]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
					elif p2==1:
						if data[counter+1] == data[counter+2]:
							data[data[counter+3]] = 1
						else:
							data[data[counter+3]] = 0
				counter=counter+4
			elif str(data[counter])[-2:] == "99":
				print("Opcode 99, fin du programme")
				break
			else:
				print("Opcode non reconnu, fin du programme")
				break
		except:
			#print("Problème d'indice, fin du programme")
			break
	return output_value
print("Output for part 1: " + str(part_1(1,numbers.copy())))

# partie 2
print("Output for part 2: " + str(part_1(5,numbers.copy())))
