a = int(input("Enter a number: "))
c = 0
for i in range(0, a+1):
    b = i**2
    if b < a+1:
        c += b
    else:
        break
print(c)