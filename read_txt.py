import pandas as pd
import numpy as np
file = open('hello.txt').read()
print('------------------')
print('OK! Let\'s try some thing!')
<<<<<<< HEAD
print('yes!')
=======


>>>>>>> parent of 1248ee7... add try something
print('------------------')
print(file)
print('------------------')

from exam_if_str_in import exam_if_str_this_in
from calculate_alpha_length import cal_alpha_length_of_str

test_str='have'
print(f"Whether {test_str} in str: ",exam_if_str_this_in(file, test_str))
print("The count of alphabets: ",cal_alpha_length_of_str(file))