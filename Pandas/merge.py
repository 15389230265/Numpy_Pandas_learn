import pandas as pd
import numpy as np

# # concatenating
# #定义资料集
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
#
# res = pd.concat([df1, df2, df3], axis=0)
# print(res)
#
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)
#
# # join, ['inner', 'outer']
# #定义资料集
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
# res = pd.concat([df1, df2], join='outer')
# print(res)
# res = pd.concat([df1, df2], join='inner', ignore_index=True)
# print(res)
#
# # join_axes
# res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
# print(res)
#
# # append
# #定义资料集
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
# s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
#
# #将df2合并到df1的下面，以及重置index，并打印出结果
# res = df1.append(df2, ignore_index=True)
# print(res)
# #合并多个df，将df2与df3合并至df1的下面，以及重置index，并打印出结果
# res = df1.append([df2, df3], ignore_index=True)
# print(res)
# #合并series，将s1合并至df1，以及重置index，并打印出结果
# res = df1.append(s1, ignore_index=True)
# print(res)

# merging two df by key/keys.
#定义资料集并打印出
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on='key')
print(res)

# consider two keys
#定义资料集并打印出
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
# how = ['left', 'right', 'inner', 'outer']
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print(res)

# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_col')
print(res)

# merge by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boys', '_girls'], how='outer')
print(res)
