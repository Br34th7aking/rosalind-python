# degree array
# Given a graph G, find the degree of each vertex in the graph
# abhijit raj

inputfile = open('rosalind_in.txt', 'r')
data = inputfile.readlines()

v,e = data[0].split()
v = int(v)
e = int(e)

count = [0] * (v+1)
for i in range(1, e+1):
    v1, v2 = data[i].split()
    count[int(v1)] += 1
    count[int(v2)] += 1
count = count[1: ] # to remove the first element, i.e. the 0 vertex
ans = ' '.join(str(item) for item in count)
outputfile = open('rosalind_out.txt', 'w')
outputfile.write(ans)
