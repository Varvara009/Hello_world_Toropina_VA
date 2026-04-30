n = int(input("Введите длину массива:"))
maxi = None
for i in range(n):
    x = float(input("Введите содержимое массива:"))
    if maxi is None or x > maxi :
        maxi = x
print("Наибольшее число: ", maxi)    
    
