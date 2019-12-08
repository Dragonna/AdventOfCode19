# Advent of Code - 08
import numpy
# Init
layers=[]
layer=numpy.empty((6,25))
ctr=0
image=numpy.empty((6,25))

# input
with open('08.txt', 'r') as input:
	for numbers in input:
		for number in numbers:
			if '\n' in number:
				number = number[:-2]
			try:
				int(number)
				if ctr%(25*6)==0 and ctr!=0:
					layers.append(layer)
					layer=numpy.empty((6,25))
					ctr=0
				layer[int(ctr/25)][ctr%25]=number
				ctr+=1
			except:
				print(number)
				# end of file
		layers.append(layer)

# partie 1
zeros=[]
for layer in layers:
	zeros.append(numpy.count_nonzero(layer==0))

print(numpy.count_nonzero(layers[zeros.index(min(zeros))]==1) * numpy.count_nonzero(layers[zeros.index(min(zeros))]==2))

# partie 2
for layer in layers:
	for x in range(0,25):
		for y in range(0,6):
			if image[y][x]!=0 and image[y][x]!=1 and layer[y][x]!=2:
				image[y][x]=layer[y][x]
for y in range(0,6):
	line=''
	for x in range(0,25):
		line+=(str(int(image[y][x])))
	print(line)