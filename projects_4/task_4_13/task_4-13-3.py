n = int(input())
fact = 1
i = 1
for i in range (1, n + 1):
    fact = fact * i
    i = i + 1
print(fact)