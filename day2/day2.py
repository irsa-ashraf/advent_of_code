

data = open('day2_data.txt').read().split('\n')

directions = [tuple(direction.split()) for direction in data]
directions = directions[: -1]

# PART A
def calculate_depth_and_horizontal(direction_data):
    '''
    Calculates the final depth and horizontal position 
    Inputs:
        direction_data: (list) list of tuples 
    Returns (tuple): tuple with final horizontal and depth values 
    '''

    horizontal = 0
    depth = 0 

    for direction, value in direction_data:
        if direction == 'forward':
            horizontal += int(value)
        elif direction == "down":
            depth += int(value)
        elif direction == "up":
            depth -= int(value)

    return (horizontal, depth)



# PART B
def calculate_depth_and_horizontal_with_aim(direction_data):
    '''
    '''

    horizontal = 0
    depth = 0
    aim = 0 

    for direction, value in direction_data:
        if direction == 'forward':
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == 'down':
            aim += int(value) 
        elif direction == 'up':
            aim -= int(value)

    return (horizontal, depth)





