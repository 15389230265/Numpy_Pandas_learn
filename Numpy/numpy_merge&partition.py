# coding:utf-8

import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
print('A:{}\nB:{}\nvertical stack:{}\nhorizontal stack:{}\n'
      'concatenate\nvertical stack:{}\nhorizontal stack:{}\n'.format(
    A, B, np.vstack((A, B)), np.hstack((A, B), np.concatenate((A, B), axis=0), np.concatenate((A, B), axis=1)
))
