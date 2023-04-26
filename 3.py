a = int(input("Enter the number of elements: "))
numbers = []
for i in range(a):
    b = int(input("Enter a number: "))
    numbers.append(b)
    
seperator = lambda nums: {"even": [n for n in nums if n % 2 == 0], "odd": [n for n in nums if n % 2 != 0]}

print(seperator(numbers))