# coding:utf-8

import numpy as np

array = np.array([[1, 2, 3],
                  [2, 3, 4]])
print(array)
# ndim：维度
# shape：行数和列数
# size：元素个数
print('number of dim:{}\nshape:{}\nsize:{}\n'.format(array.ndim, array.shape, array.size))
