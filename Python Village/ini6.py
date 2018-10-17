# Problem
#
# Given: A string s of length at most 10000 letters.
#
# Return: The number of occurrences of each word in s, where words are separated by spaces.
# Words are case-sensitive, and the lines in the output can be in any order.

inputfile = open('rosalind_ini6.txt', 'r')
line = inputfile.readline()
words = str(line).split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

outfile = open('rosalind_out6.txt', 'w')
output = []
for word in word_freq:
    line = ' '.join([word, str(word_freq[word])])
    output.append(line)

outfile.write('\n'.join(output))
outfile.close()
