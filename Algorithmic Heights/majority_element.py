# Majority Element
# Abhijit Raj

inputfile = open('rosalind_maj.txt', 'r')
data = inputfile.readlines()
k, n = data[0].split()
k = int(k)
n = int(n)

outputfile = open('rosalind_out.txt', 'w')
for i in range(1,k+1):
    arr = data[i].split()
    arr.sort()
    count = {}
    for e in range(len(arr)):
        arr[e] = int(arr[e])
        if arr[e] in count:
            count[arr[e]] += 1
        else:
            count[arr[e]] = 1

    mid = int(n/2)


    if count[arr[mid]] > mid:
        outputfile.write(str(arr[mid]) + ' ')
    else:
        outputfile.write(str(-1) + ' ')

inputfile.close()
outputfile.close()
