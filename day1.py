# Count the number of times depth increased from its previous value 

input_lst = [i for i in open("aoc_day1_data.txt").read().split()]

input_lst = [int(i) for i in input_lst]

def count_depth_increase(input):
    '''
    For a given list of inputs, counts the number of times each 
        value is greater than the previous value
    Inputs:
        input: (list): list of values 
    Returns (int): Number of times value increases 
    '''

    depth_increase_counter = 0

    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            depth_increase_counter += 1

    return depth_increase_counter
     
