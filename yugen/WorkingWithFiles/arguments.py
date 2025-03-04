import sys

for arg in sys.argv:
    print(arg)

# --------------------------------
# Challenge : Get the product of the all the arguments 


prod = 1
del(sys.argv[0])
for i in range(len(sys.argv)):
    try:
        prod*=float(sys.argv[i])
    except Exception as e:
        print(e)
        print('Only Numbers can be provided')
        sys.exit(1)

print(prod)