# solution to the question fib.py
import sys 

filename = sys.argv[1]

with open(filename, 'r') as infile: 
    data = infile.readline().split(' ')

n = int(data[0])
k = int(data[1])

# the formula for the recurrence is F(n) = F(n-1) + k * F(n-2)

first = 1 
second = 1 

if n == 1: 
    print(first)

if n == 2: 
    print(second)

third = 0
for i in range(2, n):
    third = second + k * first 
    first = second 
    second = third 

print(third) 
