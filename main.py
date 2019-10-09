import math

filename = ["5.wav","2019-05-14 1137.wav"]
filenameindex = 1

n = []
posl = 11
pos = 0
peaks = []
llindar = 1500
midindex = math.floor(posl/2)
differences = []
llpos = 0
llposl = 40
binary = []
binaryf = ""
hexf = ""
bitsUsed = 200
bf = [True]*8
bf[1] = False # Equals to 10111111

def mitjana(l):
	t = 0;
	for i in l:
		t += i
	return t/len(l)

def xor(byte1,byte2):
	if len(byte1) != len(byte2):
		return None
	print(byte1)
	print(byte2)
	print("////////////////////////")
	result = [False]*len(byte1)
	j = 0
	while j < len(byte1):
		result[j] = byte1[j] != byte2[j]
		j += 1
	return result

with open(filename[filenameindex],"rb") as f:
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
	i += 1
differences = differences[15:-5]

while len(differences) - llpos != llposl:
	a = differences[llpos:llpos+llposl]
	binary.append(a[0] < mitjana(a))
	#print(mitjana(a))
	llpos += 1
i = 0
while i < llposl-1:
	i += 1
	binary.append(a[i] < mitjana(a))

i = 0
b = True
while i < len(binary)-1:
	if binary[i] and binary[i+1] and b:
		b = False
	else:
		binaryf += "1" if binary[i] else "0"
		b = True
	i += 1

# Take out bits that we don't need
spos = binaryf.index("1011")
binaryf = binaryf[spos:spos+bitsUsed]

# Conversation from bin to hex
i = 0
accum = None
while i < len(binaryf):
	cbyte = binaryf[i:i+8]
	hexf += str(hex(int(cbyte,2)))[2:]
	if accum is not None:
		accum = xor(accum,[bit == "1" for bit in cbyte])
	else:
		accum = [bit == "1" for bit in cbyte]
	i += 8

if accum == bf:
	print(hexf)
else:
	print("An error has occurred while reading the file:")
	print(hexf)
	print(accum)