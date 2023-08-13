# Script to sort lines by two different keys
# Written by Murshid Saqlain
# Each line of the text file contains the name of a card
# The names have a specific formatting, with which we will sort the names
# First 3 letters specify the TYPE of the card (TEQ, PHY, STR, INT, AGL)
# The next two letters specify the RARITY of the card (UR and LR)
# Knowing this information and that the format is always the same,
# we can easily create keys with list indices and use the sorted() function

# Filepath where the file to be sorted is
file_path = '../data/sorting/dbz_cards.txt'

# Read the lines from the file and store them in a list
lines = []
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove trailing newline characters from each line
lines = [line.strip() for line in lines]


# Function to create custom sorting keys
def custom_sort_key(item):

    prefix = item[:3]  # Get the first 3 characters
    rarity = item[4:6]  # Get the next 2 characters (after the space)

    return (prefix, rarity)


# Sort the lines based on the keys we defined above
sorted_lines = sorted(lines, key=custom_sort_key)

# Specify the file path where we want to write the file
# if it will be a new file, otherwise use previous filepath
file_path = '../data/sorting/dbz_cards_sorted.txt'

# Open the file in write mode and write the sorted lines
with open(file_path, 'w') as file:
    for line in sorted_lines:
        file.write(line + '\n')

# Print confirmation
print("File updated with sorted lines.")
