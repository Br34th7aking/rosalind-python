# get the input from the file

data = []
with open('rosalind_in.txt', 'r') as inputfile:
    data = inputfile.readlines()
# store the neighbors of each node in a dictionary
num_nodes = int(data[0].split(' ')[0])

neighbors = {}
for i in range(1, num_nodes +1):
    neighbors[str(i)] = []
for line in data[1:]:
    line = line.rstrip()
    nodes = line.split(' ')
    if nodes[0] not in neighbors.keys():
        neighbors[nodes[0]] = [nodes[1]]
        if nodes[1] not in neighbors.keys():
            neighbors[nodes[1]] = [nodes[0]]
        else:
            neighbors[nodes[1]].append(nodes[0])
    else:
        neighbors[nodes[0]].append(nodes[1])
        if nodes[1] not in neighbors.keys():
            neighbors[nodes[1]] = [nodes[0]]
        else:
            neighbors[nodes[1]].append(nodes[0])
# for every node count the degrees of the neighbors and add them

sum = {}
for node in neighbors.keys():
    sum[node] = 0
    for i in neighbors[node]:
        sum[node] += len(neighbors[i])
ans = []
for val in sum:
    ans.append(sum[val])

for i in range(len(ans)):
    ans[i] = str(ans[i])
# print the output to the output file
with open ('rosalind_out.txt', 'w') as outputfile:
    outputfile.write(' '.join(ans))
