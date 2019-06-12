import math

n = []
posl = 11
pos = 0
peaks = {}
midindex = math.floor(posl/2)

with open("5.wav","rb") as f:
	byte = f.read(44)
	while byte:
		byte = f.read(2)
		n.append(int.from_bytes(byte, "little", signed=True))
n = n[:-1]

# Find the maxium(s) and minimum(s) value(s)
while pos < len(n)-midindex:
	# Gettin the 11 numbers from pos
	a = n[pos:pos+posl]

	# Make array length divisible by posl
	while len(a)%posl != 0:
		a.append(0)

	# Get the middle value
	mid = a[midindex]

	# Get the max or min value & check if are equal
	if max(a) == mid or min(a) == mid:
		peaks[midindex+pos] = mid

	# Changing to the next position
	pos += 1
print(peaks)