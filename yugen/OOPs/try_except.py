# print('Before')

# # a = 4 / 0

# try:
#     # a = 4 / 0
#     print(age)
# except NameError as e:
#     print("Name Error")
#     print(e)
# except ZeroDivisionError as e:
#     print('Division by 0 is not allow')
#     print(e)

# print('After')

class CheezeError(Exception):
    pass


def upper_func(string : str):
    if len(string) <= 0:
        raise CheezeError("String length should be > 0")
    return string.upper()


print(upper_func(""))

try:
    print(upper_func(""))
except Exception as e:
    print(e)
