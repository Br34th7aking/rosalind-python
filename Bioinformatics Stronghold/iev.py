# Solution to the problem 'Calculating Expected Offspring'

# From the given data in the problem statement, it is clear that the first three cases will have all the offsprings with 
# the dominant phenotype
# the 4th case will have 3/4 offspring with dominant type
# the 5th case will have 1/2 offspring with the dominant phenotype 
# the last case will have no offspring with the dominant phenotype 


# so the formula becomes 1 * 2 * (num1 + num2 + num3) + 3/4 * 2 * (num4) + 1/2 * 2  * num5 + 0
# we multiply by 2 because each couple is producing two offspring.  


import sys 

filename = sys.argv[1]

with open(filename, 'r') as infile: 
	data = infile.readlines()

numbers = list(map(int, data[0].rstrip().split(' ')))

expectation = 2 * (numbers[0] + numbers[1] + numbers[2]) + 3/4 * 2 * numbers[3] + 1/2 * 2 * numbers[4]


print(expectation)
