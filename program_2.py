# Name: Ariana Fafach
# Date: 3/25/2026
# Title: Program #2: Random Number File Writer


# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def write_random_numbers():

    # Get the number of random number to generate from user:
    number_of_numbers = int(input("Enter the number of random numbers you would like to write to the file. Enter a number between 0 and 1000:  "))
    
    # Only execute code if the user enters a number in the accepted range:
    if number_of_numbers > 0 and number_of_numbers < 1000:

        # Open random_numbers file in write mode:
        file = open("random_numbers.txt", 'w')

        for i in range(number_of_numbers):
            # Generate a random number in the range 0 to 500:
            random_number = random.randint(1,501)
            # Write each random number to the random_numbers file
            file.write(f'{random_number}\n')

        # Close file:
        file.close()

    # Print this message if the user enters a number that is too small or too large:
    else:
        print("Make sure your number is greater than 0 but less than 1000.")


if __name__ == '__main__':
    write_random_numbers()