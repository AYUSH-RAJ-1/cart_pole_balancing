import gymnasium as gym
import numpy as np 
from collections import deque
import matplotlib.pyplot as plt
import math

ALPHA = 0.1

GAMMA = 0.99 # close to one is better for farsighted behaviour

# then we have decay rate of exploration and we start with one

EPSILON_START = 1.0
EPSILON_MIN = 0.01
EPSILON_DECAY = 0.997 # applied after every episode

N_EPISODE = 4000
MAX_STEP = 500

# discretization and finding bound for our cartpole

STATE_BOUNDS = [
    (-2.4,2.4),# displacement from center
    (-3.0,3.0),
    (-0.25,0.25),
    (-3.5, 3.5)
]

N_BINS = [6, 6, 12, 12]
# when we recive an state we have 4 values which are continuos and each belongs to some bins, like the value -2.4 for displacment will be placed in bin 0 of that state so we have to map the value accrodingly
def discretize(state):
    bins = []
    # map the continuos values to the discrete states that we define using bins

    # our idea is to make descrete values of thoose functions so that we can discretize them properly

    # write a function for that

    for i in range(len(state)):

        low,high = STATE_BOUNDS[i]
        value = state[i]

        if value < low:
            value = low
        elif value > high:
            value = high
        
        # now scale this value state(i) to put it inside the bound of the provided bound
        available_bins = N_BINS[i]
        # then find the ratio using which which we will put it inside the bin

        ratio = (value - low)/(high - low)
        # scale this ratio by the avialable_bins

        if ratio == 1:
            bins.append(available_bins-1)

        else:
            scaled_ratio = available_bins * ratio
            bins.append(int(scaled_ratio))
    return bins


# check this function using init

if __name__ == "__main__":

    state = [2,3,0,3]
    created_bins = discretize(state)
    print(created_bins)

    # in the last push the the values where not clipped and also we can use some predefine cases to test if the function actually works
    # we can use assert in the line which will stop our code if obvious codes are not working
    # today only this part we will do in this repo

    # test cases for which we know the answer
    state_1 = [2.4,3.0,0.25,3.5] # answer will be - [5,5,11,11]
    print('test_Case_1 [5, 5, 11, 11]',discretize(state_1))
    state_2 = [-2.4,-3.0,-0.25,-3.5]# answer will be - [0, 0, 0, 0]
    print("test_case_2 [0, 0, 0, 0]",discretize(state_2))
    state_3 = [2.3,2.9,0.24,3.4] # check of previous error [5, 5, 11, 11]
    print("test_case_ 3 [5, 5, 11, 11]",discretize(state_3))
    # found the problem now debug it
    # fixed now make clip the values in range using max and min
    # test case for max and min
    state_4 = [-2.5,-3.1,-0.26,3.5] # [0, 0, 0, 11]
    print("out_of_bound_test_case [0, 0, 0, 11]",discretize(state_4))

    
    

    

