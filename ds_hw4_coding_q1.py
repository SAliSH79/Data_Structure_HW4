# -*- coding: utf-8 -*-
"""DS_HW4_Coding_Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fD_iWylrwl7iu1r2xhD3rz4mLpHp9_3D

## Data Structure Spring 2023
### SeyedAli SeyedHosseini 9731306
HW4_CODE 1 Practical Implementation
"""

import numpy as np
if int(T) > 1e5 :
  print("Wrong Test Number")
n, m, s, t = 4, 3, 2, 3 #2nd person, 1st person, #relations for BigMouth, friends numbers
T = n #Test size
A = np.array([[2, 3], [3, 4],[4,1 ]]) #Relations between bigMouth dudes and friends and its only between 2 friends not More

if n + m > 1e5 :
  print("Numbers are exceeded")

row = A.shape[0]
col = A.shape[1]

d = 0 #days counter
if A[0][0] != s:
    print("Wrong information")
for i in range(row) :
    if A[i][1] != s:
      d += 1
      continue
    if A[i][1] == s:
      print("Days it took for the secret to become outof Bag :",d)
if A[row - 1][col - 1] != s :
     print("-1")