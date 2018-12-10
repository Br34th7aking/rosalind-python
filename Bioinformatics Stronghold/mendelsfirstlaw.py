import sys

filename = sys.argv[1]

with open(filename, 'r') as infile: 
   data = infile.readline().rstrip()
data = data.split(' ')
values  = list(map(int, data))
k = values[0]
m = values[1]
n = values[2]

probability =( k * (k-1)/2 + (3/8) * m * (m-1) + k * n + k * m + m * n / 2) / ((k+m+n) * (k + m + n - 1) / 2)
print(probability) 


