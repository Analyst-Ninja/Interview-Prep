# Creates the file only when file does not exist - x
# file = open('cheese.txt', 'x')
# file.write('X marks the spot.')

# Overwrite (create even if the file not exists) - w
file = open('cheese.txt', 'w')
file.write('For the W!\n')

# Append
file = open('cheese.txt', 'a')
file.write('for a the A!\n')

# -------------------------------------------
# Challenge: Create a file named as the arguents given from CLI

import sys

file = open(f'{sys.argv[1]}.txt', 'w')
file.close()