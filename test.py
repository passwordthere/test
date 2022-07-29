from test_path import *
import os
from shutil import move, copytree


# 题1
# a_list = [A, B, C, D, E, F, G, H, I, J, ]

# for i in a_list:
#     try:
#         os.mkdir(i)
#     except FileExistsError as e:
#         print(e)

# 题2
# for i in range(1, 11):
#     try:
#         os.mkdir(str(i))
#     except FileExistsError as e:
#         print(e)

# j = 1
# for i in range(1, 1001):
#     open('file%s' % i, 'w')
#     move('file%s' % i, str(j))
#     if (int(i) % 100 == 0):
#         j += 1
        
# 题3
a_list = [A, B, C, D, E, F, G, H, I, J, ]

k = 1
for i in a_list:
    for j in range(k, 11):
        copytree(str(j), i + str(j))
    k += 1
    for l in range(1, k-1):
        copytree(str(l), i + str(l))
        