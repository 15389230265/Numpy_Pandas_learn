# coding:utf-8

import numpy as np

# array：创建数组
# dtype：指定数据类型
# zeros：创建数据全为0
# ones：创建数据全为1
# empty：创建数据接近0
# arrange：按指定范围创建数据
# linspace：创建线段

a = np.array([2, 23, 4])
print(a)

a = np.array([2, 23, 4], dtype=np.int)
print(a.dtype)
a = np.array([2, 23, 4], dtype=np.int32)
print(a.dtype)
a = np.array([2, 23, 4], dtype=np.float)
print(a.dtype)
a = np.array([2, 23, 4], dtype=np.float32)
print(a.dtype)

a = np.array([[2, 23, 4],
             [2, 23, 4]])
print(a)

a = np.zeros((3, 4))
print(a)

a = np.ones((3, 4), dtype=np.int)
print(a)

a = np.empty((3, 4))
print(a)

a = np.arange(10, 20, 2)
print(a)

a = np.arange(12).reshape((3, 4))
print(a)

a = np.linspace(1, 10, 20)
print(a)

a = np.linspace(1, 10, 20).reshape((5, 4))
print(a)
