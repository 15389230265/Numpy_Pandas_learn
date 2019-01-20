import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)

dates = pd.date_range('20190101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'
                    })
print('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    df2, df2.dtypes, df2.index, df2.columns, df2.values, df2.describe(), df2.T, df2.sort_index(axis=1, ascending=False), df2.sort_values(by='B')))
