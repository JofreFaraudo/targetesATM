import math

n = []
posl = 11
pos = 0
maximums = []

with open("5.wav","rb") as f:
	byte = f.read(44)
	while byte:
		byte = f.read(2)
		n.append(int.from_bytes(byte, "little", signed=True))
n = n[:-1]

# Find the maxium(s) value(s)
while pos < len(n):
	# Gettin the 11 numbers from pos
	a = n[pos:pos+posl]

	# Make array length divisible by posl
	while len(a)%posl != 0:
		a.append(0)

	# Get the middle value
	mid = a[math.floor(posl/2)]

	# Get the max value & check if are equal
	if max(a) == mid:
		maximums.append(mid)

	# Changing to the next position
	pos += 1
print(maximums)