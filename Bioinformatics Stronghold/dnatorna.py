# transcribing dna to rna
# replace every 'T' by a 'U'

# get the data
import sys
# get the input
filename = sys.argv[1]

data = []
with open(filename, 'r') as infile:
    dnastring = list(infile.read().rstrip())

for i in range(len(dnastring)):
    if dnastring[i] == 'T':
        dnastring[i] = 'U'

with open('outfile.txt', 'w') as outfile:
    outfile.write(''.join(dnastring))
