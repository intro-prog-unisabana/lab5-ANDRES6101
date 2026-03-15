# FREEZE CODE BEGIN
def greet(name):
    """
    Return a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting in the format "Hello, <name>!".
    """
    return f"Hello, {name}!"


def flip(input_string):
    """
    Reverse the characters in the given string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return input_string[::-1]


def count_letters(input_string, letter):
    """
    Count how many times a specific letter appears in a string.

    Args:
        input_string (str): The string to search.
        letter (str): The letter to count (should be a single character).

    Returns:
        int: The number of occurrences of the letter in the string.
    """
    count = 0
    for char in input_string:
        if char == letter:
            count += 1
    return count

if __name__ == "__main__":
  print("This file is being run directly.")
# FREEZE CODE END
from utils import flip, count_letters
mensaje = input("Please type your message\n")
mensaje_invertido = flip(mensaje)

cantidad_a = count_letters(mensaje, 'a')
mensaje_codificado = mensaje_invertido + str(cantidad_a)

print("Your encoded message is:", mensaje_codificado)
