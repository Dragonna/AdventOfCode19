# Advent of Code - 06

# Init
galaxy=dict()
curr_sats=["COM"]
next_sats=[]
loop=1

# input
with open('06.txt', 'r') as input:
	for line in input:
		if '\n' in line:
			galaxy[line.split(")")[1][:-1]] = [[line.split(")")[0]],[]]
		else:
			galaxy[line.split(")")[1][:-1]] = [[line.split(")")[0]],[]]	

while loop == 1:
	for curr_sat in curr_sats:
		for key in galaxy.keys():
			if curr_sat in galaxy.get(key)[0]: #if direct link with it
				if galaxy.get(curr_sat) is not None:
					for direct in galaxy.get(curr_sat)[0]:
						galaxy[key][1].append(direct)
					for indirect in galaxy.get(curr_sat)[1]:
						galaxy[key][1].append(indirect)
				#print(galaxy)
				next_sats.append(key)
	if len(next_sats)==0:
		loop = 0
	curr_sats=next_sats.copy()
	next_sats=[]

compte=0
for key in galaxy.keys():
	compte+=len(galaxy.get(key)[0])+len(galaxy.get(key)[1])
print(compte)

YOUpath=[]
SANpath=[]
YOUpath.append(galaxy.get("YOU")[0])
SANpath.append(galaxy.get("SAN")[0])
# ce bout pourrait être bcp mieux, mais j'ai sommeil et ça fonctionne mdr XD
for x in galaxy.get("YOU")[1]:
	YOUpath.append(x)
for x in galaxy.get("SAN")[1]:
	SANpath.append(x)
for y in YOUpath:
	if y in SANpath:
		print(YOUpath.index(y)+SANpath.index(y))
		break

