import pandas as pd
df = pd.DataFrame({
    '部门': ['技术', '技术', '市场', '市场', '技术', '市场'],
    '姓名': ['张三', '李四', '王五', '赵六', '钱七', '孙八'],
    '年龄': [25, 30, 28, 35, 29, 32],
    '工资': [10000, 15000, 12000, 18000, 13000, 14000],
    '性别': ['男', '男', '女', '女', '男', '男']
})

print(df.groupby('部门').mean(numeric_only = True))
print(df)
x = df.groupby('部门').agg({'年龄': ['mean', 'min', 'max', 'count'],
                        '工资': ['mean', 'sum']})
print(x)
