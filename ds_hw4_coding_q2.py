# -*- coding: utf-8 -*-
"""DS_HW4_Coding_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ICfVqfMnbUDI8LX7_-blBRRoPaPwpx2t
"""

import intervals as I

n = 3
x1 = I.open(-I.inf,3)
x2 = I.open(3,7)
x3 = I.closedopen(7,I.inf)

p = x1 & x2
p.is_empty()
if p:
   u2 =  x2.union(x3)
else :
   u2 = x1 | x2
print("The result of Union is",x1 ,"U", u2)