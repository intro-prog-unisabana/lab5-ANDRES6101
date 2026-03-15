import os
import math

cwd = os.getcwd()
print("Current working directory:", cwd)

num = int(input("Enter an integer: "))
log_value = math.log2(num)
print("Log base 2 of", num, "is:", log_value)

floor_value = math.floor(log_value)
ceiling_value = math.ceil(log_value)

print("Floor:", floor_value)
print("Ceiling:", ceiling_value)