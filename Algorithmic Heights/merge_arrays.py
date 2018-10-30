# Given two sorted arrays, merge them into a new array
# Abhijit Raj

def merge(A, B):
    ''' takes in two sorted arrays A and B
    returns a sorted array C that contains all the elements of A and B
    '''
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    C = []
    while i < n and j < m:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i == n and j < m:
        C.extend(B[j:])
    if j == m and i < n:
        C.extend(A[i:])

    return C

inputfile = open('rosalind_in.txt', 'r')
data = inputfile.readlines()
n = data[0]
A = list(map(int, data[1].rstrip().split()))
m = data[2]
B = list(map(int, data[3].rstrip().split()))

result = merge(A, B)

outputfile = open('rosalind_out', 'w')
outputfile.write(' '.join(list(map(str,result))))

inputfile.close()
outputfile.close()
