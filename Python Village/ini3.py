input_str = input()
positions = input().split()
a,b,c,d = int(positions[0]), int(positions[1]), int(positions[2]),int(positions[3])

print(input_str[a: b+1], end = " ")
print(input_str[c: d+1])
