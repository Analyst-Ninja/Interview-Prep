# file = open('cheese.txt', 'r')

# file.read()
# file.read()
# file.read()

# lines = file.readlines()
# print(lines)

# -------------------------------------
# Challenge:
# Create a file numbers.txt that has a few lines of numbers.
# Multiply all the numbers together and print the result.

file = open('numbers.txt', 'a')

numList1 = '1,2,3,4,5,6,7\n'
numList2 = '1,2,3,4,5,6,2\n'
numList3 = '1,2,3,4,5,6,4\n'
file.write(numList1)
file.write(numList2)
file.write(numList3)

file.close()

file = open('numbers.txt', 'r')
lines = file.readlines()

from functools import reduce
nums = []
# all_numbers = reduce(lambda nums, num : nums + num.strip().split(","), lines)

numList = list(map(lambda x:x.strip().split(","), lines))

all_prod = 1
for nums in numList:
    prod=reduce(lambda p, x: p*int(x), nums, 1)
    all_prod *= prod
print(all_prod)