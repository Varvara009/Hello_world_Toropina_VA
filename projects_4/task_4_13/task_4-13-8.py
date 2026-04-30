array = [64, -34, 25, 12, -22, 11, 90]
n = len(array)
sum = 0

for i in range(n):
    if array[i] > 0:
        sum += 1
print(sum)
