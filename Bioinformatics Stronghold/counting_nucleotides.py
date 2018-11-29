# to count the number of nucleotides in a given string

import sys
# get the input
filename = sys.argv[1]

data = []
with open(filename, 'r') as infile:
    dnastring = infile.read().rstrip()

# use a dictionary with nucleotides as keys and do a linear scan of the string
nt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for c in dnastring:
    nt[c] += 1

for count in nt.values():
    print(count, end=' ')

print('\n')
