# -*- coding: utf-8 -*-
"""Sample for Time Measuring
if you like to check how long a Script, 
or function will take for execution, 
you can just use this sample
"""

import time


# get the start time
st = time.time()

#########################
# main program
# put your code below, to check the execution time

# Sample One:
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i
print('Sum of first 1 million numbers is:', sum_x)

# Sample Two:
for i in range(6000):
    print('This will PRINT this message many times')
###########################

# get the end time
et = time.time()

# calculate and print the execution time
print('Execution time:', et - st, 'seconds')