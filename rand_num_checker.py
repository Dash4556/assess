# -*- coding: utf-8 -*-
"""capgtech-bootcamp.ipynb

Automatically generated by Colaboratory.
"""

# --Assignement--
# Create and call a python function that :
# - stores a random integer A between 1 and 9
# - stores a random integer B between 1 and 9
# - multiplies A and B together as C
# - Prints A and C for every result until C = 4
# - If C = 4 , print ‘Success!’ and the results for A and B
# - Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV

import numpy as np
import random

def four_checker():
  A, B = random.randint(2, 8), random.randint(2, 8)
  C = A * B
  while C != 4:
    A, B = random.randint(2, 8), random.randint(2, 8)
    C = A * B
    print(A, C)
  print('Success! \nResults for A and B: ', A, 'and', B)

four_checker()
