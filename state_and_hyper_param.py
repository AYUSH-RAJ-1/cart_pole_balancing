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
        # now scale this value state(i) to put it inside the bound of the provided bound
        available_bins = N_BINS[i]
        # then find the ratio using which which we will put it inside the bin

        ratio = (state[i] - low)/(high - low)
        # scale this ratio by the avialable_bins

        scaled_ratio = available_bins * ratio
        bins.append(int(scaled_ratio))


print(int(5.6))
    

    

