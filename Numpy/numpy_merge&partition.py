# coding:utf-8

import numpy as np

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]
print('A:{}\nB:{}\nvertical stack:{}\nhorizontal stack:{}\nconcatenate\nvertical stack:{}\nhorizontal stack:{}\n'.format(
    A, B, np.vstack((A, B)), np.hstack((A, B)), np.concatenate((A, B, B, A), axis=0), np.concatenate((A, B, B, A), axis=1)
))

A = np.arange(12).reshape((3, 4))
print('A:{}\nvertical split:{}\nhorizontal split:{}\nnot equal split:{}\n'.format(
    A, np.split(A, 2, axis=1), np.split(A, 3, axis=0), np.array_split(A, 3, axis=1)
))
