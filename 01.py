# Advent of Code 2019 - 01

# Init
modules=list()
fuel_1=0
temp_fuel=0
fuel_2=0

# input
with open('01.txt', 'r') as input:
	for line in input:
		modules.append(int(line[:-1]))

# fonction décrite dans description
def fuel_requirement(module):
	fuel = int(module/3)-2
	if fuel > 0:
		return fuel
	else:
		return 0

# partie 1
for module in modules:
	fuel_1 += fuel_requirement(module)

print(fuel_1)

# partie 2
for module in modules:
	temp_fuel = fuel_requirement(module)
	while temp_fuel != 0:
		fuel_2 += temp_fuel
		module = temp_fuel
		temp_fuel = fuel_requirement(module)


print(fuel_2)
