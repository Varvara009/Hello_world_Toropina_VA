array = [64, -34, 25, 12, -22, 11, 90]
n = len(array)
sum = 0

for i in range(0,n, 2):
    sum += array[i]
    print(array[i])
print(sum)
