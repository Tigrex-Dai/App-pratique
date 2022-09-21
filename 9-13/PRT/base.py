# -*- coding: utf-8 -*-

import pandas as pd
import os
from pathlib import Path

# df = pd.read_excel('./resultat-prts-2014.xls')
dflist = []

# 文件夹中的文件计数函数
def file_count(local_path, type_dict):
    global all_file_num  # 声明全局变量
    file_list = os.listdir(local_path)  # 列出本地文件夹第一层目录的所有文件和目录
    for file_name in file_list:
        if os.path.isdir(os.path.join(local_path, file_name)):  # 判断是文件还是目录，是目录为真
            type_dict.setdefault("文件夹", 0)  # 如果字典key不存在，则添加并设置为初始值
            type_dict["文件夹"] += 1
            p_local_path = os.path.join(local_path, file_name)  # 拼接本地第一层子目录，递归时进入下一层
            file_count(p_local_path, type_dict)
        else:
            ext = os.path.splitext(file_name)[1]  # 获取到文件的后缀
            type_dict.setdefault(ext, 0)  # 如果字典key不存在，则添加并设置为初始值
            type_dict[ext] += 1
            all_file_num += 1  # 计算总文件数量
    return all_file_num

# if __name__ == '__main__':
#     local_path = './'  # 文件夹的路径
#     type_dict = dict()  # 定义一个保存文件类型及数量的空字典
#     all_file_num = 0  # 计算本地总文件数
#     file_count = file_count(local_path, type_dict)  # 运行函数,power by luotao
#
#     # 打印文件类型以及数量
#     for each_type in type_dict:
#         print(f"文件类型为【{each_type}】的数量有：{type_dict[each_type]} 个")
#     print(f"总文件数量为:{file_count}")

path = Path(Path.cwd())
for i in path.glob("*.xls*"):
    dflist.append(pd.read_excel(i, sheet_name=None))


temp1 = dflist[1]['Feuil1']
temp2 = dflist[1]['Feuil2']
del dflist[1]
dflist[1] = temp1
dflist.append(temp2)
print(dflist[1])