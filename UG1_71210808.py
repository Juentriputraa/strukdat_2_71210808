import timeit
from matplotlib import pyplot as plt

#iteratif
def prima1(n): 
    x = 1 
    y = 1 
    for y in range(1,n):
        if ((y+1) % 5 == 0):
            print(end="")
        z = y
        y = y+x
        x = z
    
for y in range(1,101):
    start = timeit.default_timer()
    prima1(y)  
    end = timeit.default_timer()
    print("n=",y,"iteratif ->", end-start,"second")
print()

#rekursif
def prima(n):
    if n <= 1:
        return n
    else:
        return (prima(n-1)+prima(n-2))

for y in range(1,101):
    start = timeit.default_timer()
    prima(y)  
    end = timeit.default_timer()
    print("n=",y,"rekursif ->", end-start,"second")

