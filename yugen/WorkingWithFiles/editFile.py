# Read
file = open('cheese.txt','r')
lines = file.readlines()
file.close()

# Edit
# lines = ['Hello\n','My name is Nick']

# lines.insert(0, 'I like cheese\n')
# lines[1] = "Hello Friend\n"

lines[-1] = lines[-1] + '\n'
lines.append('Goodbye!')



# Write
file = open('cheese.txt', 'w')
file.writelines(lines)
file.close()

# -----------------------------------
# Challenge: Write a numbers on every lines by multiply by 2

# Read
with open('numbers.txt', 'r') as file:
    lines = file.readlines()
    print(type(lines))


# Edit
lines = list(map(lambda x: str(int(x)*2) + '\n', lines))


# Write
with open('numbers.txt', 'w') as file:
    lines = file.writelines(lines)