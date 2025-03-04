# Requires 3.10 or above

direction = input("Which direction: ").lower().strip()

match direction:
    case 'north':
        print('Up')
    case 'south':
        print('Down')
    case 'east':
        print('Right')
    case 'west':
        print('Left')
    case _:
        print('Not a valid direction')

