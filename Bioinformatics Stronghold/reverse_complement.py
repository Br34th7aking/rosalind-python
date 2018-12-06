import sys

filename = sys.argv[1]

with open(filename, 'r') as infile: 
    data = infile.readline().rstrip()

reverse = data[::-1] # reverses the string 

complement = ''

replace = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
revchar = ''

for char in reverse: 
    complement+= replace[char]

with open('outfile.txt', 'w') as outfile: 
    outfile.write(complement) 


