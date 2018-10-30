# Given an unsorted array, sort it using merge sort
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

def merge_sort(A):
    mid = int(len(A)/2)
    if mid == 0:
        return A
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

inputfile = open('rosalind_in.txt', 'r')
data = inputfile.readlines()
n = int(data[0])
A = list(map(int, data[1].rstrip().split()))


result = merge_sort(A)

outputfile = open('rosalind_out', 'w')
outputfile.write(' '.join(list(map(str,result))))

inputfile.close()
outputfile.close()
