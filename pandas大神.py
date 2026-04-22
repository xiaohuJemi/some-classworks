import pandas as pd
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 28],
    '城市': ['北京', '上海', '广州']
})
df.loc[0, '年龄'] = 26
df['是否成年'] = df['年龄'] >= 18
df1 = df.drop(0, axis = 0)
#print(df1)
#print(df1.mean(axis = 0, numeric_only = True))

