# Advent of Code - 07

import itertools

# Init
numbers=list()

# input
with open('07.txt', 'r') as input:
	for line in input:
		for number in line.split(","):
			if '\n' in number:
				numbers.append(int(number[:-1]))
			else:
				numbers.append(int(number))

# partie 1
def Read_Program(input_value1,input_value2,data,partie_2,counter):
	#counter=0
	counter_input=0
	while counter < len(data):
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
				if counter_input==0:
					data[data[counter+1]] = input_value1
					counter_input+=1
				elif counter_input==1:
					data[data[counter+1]] = input_value2
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
				if partie_2 ==1:
					return (output_value,data,counter+2)
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
				#print("Opcode 99, fin du programme")
				if partie_2 ==1:
					return ("kaput",data,counter)
				break
			else:
				print("Opcode non reconnu, fin du programme")
				#return ("kaput-" + str(output_value))
				break
		except:
			print("Problème d'indice, fin du programme")
			#return ("kaput-" + str(output_value))
			break
	return (output_value,data,counter)

#partie 1
max_output=0
for x in list(itertools.permutations([0,1,2,3,4])):
	curr_output=Read_Program(x[4],Read_Program(x[3],Read_Program(x[2],Read_Program(x[1],Read_Program(x[0],0,numbers.copy(),0,0)[0],numbers.copy(),0,0)[0],numbers.copy(),0,0)[0],numbers.copy(),0,0)[0],numbers.copy(),0,0)[0]
	if max_output < curr_output:
		max_output = curr_output
print("Output for part 1: " + str(max_output))

# partie 2
max_output=0
for x in itertools.permutations([5,6,7,8,9]): #[[9,8,7,6,5]]:
	y=-1
	curr_output=0
	last_e = 0
	ampli=[[],[],[],[],[]]
	indice=[0,0,0,0,0]
	broke=0
	while broke==0:
		y+=1
		try:
			if y<5:
				#print("Program on amp " + str(y) + " started with input:" + str(curr_output) + " and counter:" + str(indice[y]))
				(curr_output,ampli[y],indice[y])=Read_Program(x[y],curr_output,numbers.copy(),1,0)
				#print("Program on amp " + str(y) + " ended with curr_output:" + str(curr_output) + " and counter:" + str(indice[y]))
				if isinstance(curr_output, str):
					broke=1
					break
			else:
				#print("Program on amp " + str(y%5) + " started with input:" + str(curr_output) + " and counter:" + str(indice[y%5]))
				(curr_output,ampli[y%5],indice[y%5])=Read_Program(curr_output,curr_output,ampli[y%5],1,indice[y%5])
				#print("Program on amp " + str(y%5) + " ended with curr_output:" + str(curr_output) + " and counter:" + str(indice[y%5]))
				if isinstance(curr_output, str):
					broke=1
					break
			if y%5==4:
				last_e = curr_output
		except:
			#print("Reached exception")
			#print(last_e)
			broke=1
			curr_output = last_e
	if max_output < last_e:
		max_output = last_e
print("Output for part 2: " + str(max_output))