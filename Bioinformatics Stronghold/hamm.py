# hamming distance between two strings 
# both strings s and t are of equal length 

import sys 

filename = sys.argv[1]

with open(filename, 'r') as infile: 
	data = infile.readlines()


s = data[0].rstrip()
t = data[1].rstrip()

hamm = 0

for i in range(len(s)):
	if s[i] != t[i]:
		hamm += 1

print(hamm)
