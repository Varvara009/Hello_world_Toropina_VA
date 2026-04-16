n = int(input())
maxi= None
for i in range(n):
    x = float(input())
    if maxi is None or x > maxi :
        maxi = x
print(maxi)    
    
