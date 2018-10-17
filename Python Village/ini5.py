# Problem
#
# Given: A file containing at most 1000 lines.
#
# Return: A file containing all the even-numbered lines from the original file.
# Assume 1-based numbering of lines.

f = open('rosalind_ini5.txt', 'r')
lines = f.readlines()
output = []
for linenumber, line in enumerate(lines):
    if linenumber % 2:
        output.append(line)

outfile = open('rosalind_out.txt', 'w')
outfile.write(''.join(output))

f.close()
outfile.close()
