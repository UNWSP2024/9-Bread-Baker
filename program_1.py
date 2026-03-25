# Name: Ariana Fafach
# Date: 3/25/2026
# Title: Program #1: Item Counter


# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    # Add your code here #

    # Initialize number_of_names variable:
    number_of_names = 0

    # For loop add 1 to number_of_names for every name in names.txt:
    names = open("names.txt", 'r')
    for name in names:
        number_of_names += 1
    
    # Close names.txt file:
    names.close()

    ######################
    # Print the result:
    print(f"There are {number_of_names} names stored in names.txt.")



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()