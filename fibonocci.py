def fibonocci(n):
    if n <= 1:
        return 1
    else :
        return n-1 + fibonocci(n-2)

a = int(input("Enter the number of elements: "))

for i in range(a):
    print(fibonocci(i), end=" ")