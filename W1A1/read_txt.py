import pandas as pd
import numpy as np
file = open('hello.txt').read()
print('------------------')
print('OK! Let\'s try some thing!')
print('yes!')
print('------------------')
print(file)
print('------------------')

from some_utils import *

test_str='have'
print(f"Whether {test_str} in str: ",exam_if_str_this_in(file, test_str))

test_str='day'
print(f"Whether {test_str} in str: ",exam_if_str_this_in(file, test_str))
print("The count of alphabets: ",cal_alpha_length_of_str(file))
