# debugging.py

# Function to get user input
def get_daily_steps():

    steps = input("Enter your daily steps for 7 days separated by spaces: ")
    step_list = steps.split()
    step_list = [int(s) for s in step_list]
    return step_list

# Function to calculate total steps
def total_steps(nums):
    return sum(nums)

# Function to calculate average daily steps
def average_steps(total, days=7):

    return total // days

# Function to get maximum steps
def max_steps(nums):
    
 return max(nums)


# Function to get minimum steps
def min_steps(nums):

 return min(nums)

# Fuction to check if each day meets the goal
def goal_check(nums, goal=10000):

    result = []
    for s in nums:
        result.append(s >= goal)
    return result

# -----------------------
# Main program
# -----------------------

step_list = get_daily_steps()

total = total_steps(step_list)
average = average_steps(total)
highest = max_steps(step_list)
lowest = min_steps(step_list)
goal_met = goal_check(step_list)

print("Total steps:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goal_met)