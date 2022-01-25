# Problem Set 2, Question 12

import numpy as np 
import time


def eliminate(A, b):
    ''' 
    Performs elimination on a square matrix 

    Inputs:
      A: square matrix 
      b: RHS of the system of equations 

    Returns: tuple containing the upper triangular matrix and solution matrix 
    '''
    
    # create augmented matrix M
    M = np.concatenate((A, b.reshape(len(A), 1)), axis = 1)
 
    # create solution matrix 
    sm = np.zeros((len(M), 1))

    # conduct elimination
    for i in range(len(M)):
        for j in range(i+1, len(M)):
            multiplier = M[j][i] / M[i][i]

            for k in range(len(M) + 1):
                M[j][k] = M[j][k] - multiplier * M[i][k]
    
    # conduct back substitution
    sm[len(M)-1] = M[len(M)-1][len(M)] / M[len(M)-1][len(M)-1]
     
    for i in range(len(M)-2, -1, -1):
        sm[i] = M[i][len(M)]
                
        for j in range(i+1,len(M)):
            sm[i] = sm[i] - M[i][j] * sm[j]
        
        sm[i] = sm[i] / M[i][i]

    return (M, sm.reshape(1, len(A)))


def part_a():


    # From page 46 

    A = np.array([[1, -2], [3, 2]])
    b = np.array([1, 11])

    elim_answer = eliminate(A, b)
    print('Output of equations on page 46 using eliminate')
    print(elim_answer)

    linalg_answer = np.linalg.solve(A, b)
    print('Output of equations on page 46 using linalg.solve')
    print(linalg_answer)

    # From page 50 
    A = np.array([[2, 4, -2], [4, 9, -3], [-2, -3, 7]])
    b = np.array([2, 8, 10])

    elim_answer = eliminate(A, b)
    print('Output of equations on page 50 using eliminate')
    print(elim_answer)

    linalg_answer = np.linalg.solve(A, b)
    print('Output of equations on page 50 using linalg.solve')
    print(linalg_answer)


def compare_speed():
    '''
    Compare speed of eliminate with np.linalg.solve
    
    Inputs:
      n (int): length of matrix
      
    Returns: nothing. Prints the average time for each run 
    '''
    
    n_lst = [100, 200, 400, 800]    
        
    elim_time_lst_rv = []
    linalg_time_lst_rv = []
    
    for n in n_lst:
        elim_time_lst = []
        linalg_time_lst = []
        for _ in range(10):
            R = np.random.randn(n, n)
            w = np.ones(n)

            start_time_elim = time.time()
            rv = eliminate(R, w)
            end_time_elim = time.time()
            elim_time = end_time_elim - start_time_elim
            elim_time_lst.append(elim_time)

            start_time_linalg = time.time()
            np.linalg.solve(R, w)
            end_time_linalg = time.time()
            linalg_time = end_time_linalg - start_time_linalg
            linalg_time_lst.append(linalg_time)
        
        elim_avg_k_time = np.mean(elim_time_lst)
        elim_time_lst_rv.append(elim_avg_k_time)
        
        linalg_avg_k_time = np.mean(linalg_time_lst)
        linalg_time_lst_rv.append(linalg_avg_k_time)
            
    
    print('ELIMINATE')
    for i, avg_time in enumerate(elim_time_lst_rv):
        print(f'Solving Rx = w with n = 100.2^{i} using eliminate takes approximately {avg_time} milliseconds.')
        
    print('')   
    print('NP.LINALG.SOLVE')
    
    for i, avg_time in enumerate(linalg_time_lst_rv):
        print(f'Using linalg.solve, it takes approximately {avg_time} milliseconds')
        
    print('')