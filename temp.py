# -*- coding: utf-8 -*-
"""

"""

'''
1. 先把两个表(old1,old2)合并, 
2. 然后取出重复的数据, 保留一条
3. 保存到新表new1
4. 吧old1表和new1表合并
5. 然后取出重复的数据并删除，得到差集，就是在old2中但不在old1中的数据
6. 吧old2表和new1表合并
7. 然后取出重复的数据并删除，得到差集，就是在old1中但不在old2中的数据
'''


import pandas as pd


# openexcel
data1 = pd.read_excel('C:\\Users\\JZ\\.spyder-py3\\1.xlsx')
df1 = data1['Server Name'] # 读取列名为Server Name的内容
#print(df1)

data2 = pd.read_excel('C:\\Users\\JZ\\.spyder-py3\\2.xlsx')
df2 = data2['Host'] # 读取列名为Host的内容
#print(df2)


# 1.merge_excel
res = pd.concat([df1, df2], axis=0, ignore_index=True)
#print(res)


# 2,3.get_compilation
#compilation_del = res.drop_duplicates(keep=False)
compilation = res.drop_duplicates()
compilation.to_excel('C:\\Users\\JZ\\.spyder-py3\\res.xlsx')
#print(compilation_del)
#print(compilation)

# 4.merge ITAM and compilation
notin_df1_file = pd.concat([df1, compilation], axis=0, ignore_index=True)
#print(notin_df1_file)

# 5.get subtraction
inventory_notin_itam = notin_df1_file.drop_duplicates(keep=False)
#print(inventory_notin_itam)
inventory_notin_itam.to_excel('C:\\Users\\JZ\\.spyder-py3\\inventory_notin_itam.xlsx')

# 6.merge inventory and compilation
notin_df2_file = pd.concat([df2, compilation],axis=0, ignore_index=True)
#print(notin_df2_file)

# 7.get subtraction
itam_notin_inventory = notin_df2_file.drop_duplicates(keep=False)
#print(itam_notin_inventory)
itam_notin_inventory.to_excel('C:\\Users\\JZ\\.spyder-py3\\itam_notin_inventory.xlsx')







