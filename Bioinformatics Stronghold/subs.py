# find all the occurrences of a motif in a given dna string 

# store the length of the motif in a variable and then scan through the dna string to see 
# if the substring is equal to the motif. 
# if yes, store this index in a list 


import sys 

filename = sys.argv[1]

with open(filename, 'r') as infile: 
	data = infile.readlines()

dna = data[0].rstrip()
motif = data[1].rstrip()
len_motif = len(motif)

indexes = []
for i in range(len(dna) - len_motif):
	test_str = dna[i:i+len_motif]
#	print(test_str, motif)
	if test_str == motif: 
		indexes.append(i+1)


for i in indexes: 
	print(i, end=' ')

