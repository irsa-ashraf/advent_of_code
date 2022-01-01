# Count the number of times depth increased from its previous value 

input_lst = [int(i) for i in open("aoc_day1_data.txt").read().split()]


# PART A 
def count_increase(depth_lst):
    '''
    For a given list of inputs, counts the number of times each 
        value is greater than the previous value
    Inputs:
        depth_lst: (list): list of values 
    Returns (int): Number of times value increases 
    '''

    depth_increase_counter = 0

    for i in range(1, len(depth_lst)):
        if depth_lst[i] > depth_lst[i - 1]:
            depth_increase_counter += 1

    return depth_increase_counter
     
# PART B 
def count_window_increase(depth_lst, window_size):
    '''
    Counts number of windows whose sum is greater than the previous
        window sum
    Inputs:
        depth_lst (list): list of values 
        window_size (int): size of window 

    Returns (int): number of times the window sum increases 
    '''

    window_increase_counter = 0

    for i in range(len(depth_lst) - window_size):
        current_window_sum = sum(depth_lst[i: i + window_size])
        previous_window_sum = sum(depth_lst[i - 1: i - 1 + window_size])
        if current_window_sum > previous_window_sum:
            window_increase_counter += 1

    return window_increase_counter

        