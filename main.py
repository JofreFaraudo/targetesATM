import math

n = []
posl = 11
pos = 0
peaks = []
llindar = 1500
midindex = math.floor(posl/2)
differences = []

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
	if (max(a) == mid or min(a) == mid) and abs(mid) > llindar:
		peaks.append(midindex+pos)

	# Changing to the next position
	pos += 1

i = 0
while i < len(peaks)-1:
	differences.append(abs(peaks[i]-peaks[i+1]))
	print(peaks[i])
	i += 1