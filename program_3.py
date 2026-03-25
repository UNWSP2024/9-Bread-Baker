# Name: Ariana Fafach
# Date: 3/25/2026
# Title: Program #3: Average Numbers


# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

def sum_numbers_from_file():
    ######################

    try:
        # Open numbers.txt:
        file = open('numbers.txt', 'r')

        # Initiaize total
        added_number = 0

        for number in file:
            # Convert the numbers to integers:
            number = int(number)
            # Add each number to the added_number variable:
            added_number += number

        # Close file:
        file.close()

    except:
        # Print the message if an IOError occurs:
        if IOError:
            print("IO Error occured. Make sure that the file 'numbers.txt' exists.")
        # Print the message if a ValueError occurs:
        if ValueError:
            print("Value error occured while running. Please try again.")

    ######################

    # Print the result:
    print(f"The sum of all the numbers in 'numbers.txt' is {added_number}.")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()