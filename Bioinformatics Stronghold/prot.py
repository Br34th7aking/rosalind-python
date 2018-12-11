# solution to the problem 'translating rna to protein' 
import sys

filename = sys.argv[1]

with open(filename, 'r') as infile: 
	data = infile.readline().rstrip()

# build a dictionary containing rna codons 
codon = { 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 
'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 
'UAG': 'STOP', 'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W', 
'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 
'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
'CGU': 'R', 'CGC': 'R', 'CGA':  'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 
'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 
'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 
'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 
'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}


# from the string select substrings of length 3 and identify the 
# code from the table
protein = ""
i = 0
while i <len(data) - 3:

	code = data[i:i+3]
	if code != 'UAA' or code != 'UAG' or code != 'UGA':
		# add it to the protein string 
		protein += codon[code]
	else: 
		break
	i += 3

print(protein)

