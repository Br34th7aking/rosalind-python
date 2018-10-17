# Problem
#
# Given: Two positive integers a and b (a<b<10000).
#
# Return: The sum of all odd integers from a through b, inclusively.

numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])

i = a
sum = 0
if not i % 2:
    i += 1
while i <= b:
    sum += i
    i += 2
print(sum)
