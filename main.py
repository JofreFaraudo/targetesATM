#import numpy as np
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
#print(n)
while pos < len(n):
	a = n[pos:pos+posl]
	print(a)
	mid = a[math.floor(posl/2)]
	print(mid)
	print(max(a))
	if max(a) == mid:
		print("yes")
		maximums.append(mid)
	pos += 1
print(maximums)