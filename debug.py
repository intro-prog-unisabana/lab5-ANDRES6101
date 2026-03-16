def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = int(input("Enter a number:\n"))
num2 = int(input("Enter a number:\n"))
num3 = int(input("Enter a number:\n"))

maximum = find_max(num1, num2, num3)

print("Maximum value:", maximum)



