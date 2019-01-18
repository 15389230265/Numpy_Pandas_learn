# coding:utf-8

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print('a:{}\nb:{}\na+b:{}\na-b:{}\na*b:{}\nb^2:{}\n10*sin(a):{}\nb<3:{}\n'.format(
    a, b, a+b, a-b, a*b, b**2, 10*np.sin(a), b < 3
))

a = np.array([[1, 1],
              [0, 1]])
b = np.arange(4).reshape((2, 2))

print('a:{}\nb:{}\na*b:{}\nab:{}\n'.format(
    a, b, a*b, a.dot(b)
))

a = np.random.random((2, 4))
print('a:{}\nsum:{}\nmin:{}\nmax:{}\n'.format(
    a, np.sum(a, axis=1), np.min(a, axis=0), np.max(a, axis=1)
))

A = np.arange(2, 14).reshape((3, 4))
print('A:{}\nargmin:{}\nargmax:{}\nmean:{}\nmedian:{}\ncumsum:{}\ndiff:{}\nnonzero:{}\n'.format(
    A, np.argmin(A), np.argmax(A), np.mean(A), np.median(A), np.cumsum(A), np.diff(A), np.nonzero(A)
))

A = np.arange(14, 2, -1).reshape((3, 4))
print('A:{}\nsort:{}\ntranspose:{}\nclip:{}'.format(
    A, np.sort(A), np.transpose(A), np.clip(A, 5, 9)
))
