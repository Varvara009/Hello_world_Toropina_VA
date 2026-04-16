array = [64, -34, 25, 12, -22, 11, 90]
n = len(array)
sum = 0
t = 0

for i in range(0,n, 2):
    sum += array[i]
    t += 1
    print(array[i], i)
print(sum/t)
