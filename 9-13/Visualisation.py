# -*- coding: utf-8 -*-

import pandas as pd
import os
from pathlib import Path
import numpy as np
import re
from pyecharts.charts import Bar
import pandas as pd
from pyecharts import options as opts
import pandas_alive as pal


def initdf():
    df = pd.read_csv('./ProjetsComplet.csv', sep=',')

    # print(df.loc[:, 'MontantAccordé'][0])
    for index, row in df.iterrows():
        mt = row['MontantAccordé']
        if mt == '*':
            mt = 0
        # if type(mt) == str:
        #     print(mt)
        #     mt = re.sub('[^A-Za-z0-9]+', '', mt)
        #     mt = int(mt)
        df.loc[index, 'MontantAccordé'] = mt
        df = df
    df.loc[len(df.loc[:, 'MontantAccordé']) - 3, 'MontantAccordé'] = 838426
    df.loc[len(df.loc[:, 'MontantAccordé']) - 2, 'MontantAccordé'] = 324700
    df.loc[len(df.loc[:, 'MontantAccordé']) - 1, 'MontantAccordé'] = 224389


df = pd.read_csv('./ProjetsComplet.csv', sep=',')

#print(df.loc[:, 'MontantAccordé'][0])
for index, row in df.iterrows():
    mt = row['MontantAccordé']
    if mt == '*':
        mt = 0
    # if type(mt) == str:
    #     print(mt)
    #     mt = re.sub('[^A-Za-z0-9]+', '', mt)
    #     mt = int(mt)
    df.loc[index, 'MontantAccordé'] = mt
    df = df
df.loc[len(df.loc[:, 'MontantAccordé'])-3, 'MontantAccordé'] = 838426
df.loc[len(df.loc[:, 'MontantAccordé'])-2, 'MontantAccordé'] = 324700
df.loc[len(df.loc[:, 'MontantAccordé'])-1, 'MontantAccordé'] = 224389
df['MontantAccordé'] = df['MontantAccordé'].astype('float')

nometa = 'Nom de l\'établissement'

dfeta = df
for index, row in dfeta.iterrows():
    etab = row[nometa]
    if type(etab)==float:
        dfeta.drop(index=index, inplace=True)
    elif etab.find('CHU')+etab.find('CHRU') == -2:
        dfeta.drop(index=index, inplace=True)
    dfeta = dfeta

initdf()
dfeta = dfeta.drop(['Unnamed: 0','Finess', 'NomInvestigateur', 'PrénomInvestigateur', 'TitreProjet', 'NuméroProjet', 'Acronyme'], axis=1)
temp2 = dfeta.groupby(['Année', nometa]).sum
listeta = list(set(dfeta[nometa].tolist()))
#print(listeta)
semi1 = []

for j in range(2013, 2022):
    # lcount = 0
    templist = []
    templist.append(j)
    for i in listeta:
        count = 0
        for index, row in dfeta.iterrows():
            reta = row[nometa]
            rann = row['Année']
            rmon = row['MontantAccordé']
            if reta==i and rann==j:
                count += rmon
        # print(lcount)
        templist.append(count)
        # templist[lcount] = count
        # lcount += 1
    semi1.append(templist)
    # for k in range(len(templist)):
    #     semi[i][k] = templist[k]
    # semi[i] = semi[i].astype('float')

listeta.insert(0,'Année')
final = pd.DataFrame(semi1, columns=listeta)
# dfann = pd.DataFrame({'Année':[2013,2014,2015,2016,2017,2018,2019,2020,2021]})
# final = pd.concat([semi2,dfann])



#
# # 柱状图创建
bars = Bar(init_opts=opts.InitOpts(theme='dark'))
#
# # 添加值
bars.add_xaxis(list(final['Année'])),
# bars.add_yaxis("纯点", list(temp3[nometa]), stack="stack2"),
for g in listeta:
    bars.add_yaxis(g, list(final[g]), stack='stack1')


# # 配置
# bars.set_global_opts(
#
#     # 图表标题
#     title_opts=opts.TitleOpts(
#         # 标题
#         title="eta",
#         # 标题位置
#         pos_left="left",
#         # 标题字体大小设置为 20
#         title_textstyle_opts=opts.TextStyleOpts(font_size=20)
#     ),
#
#     # 图例设置
#     legend_opts=opts.LegendOpts(
#         # 显示图例，就是各个指标的切换按钮
#         is_show=True,
#         # 图例设置为单选模式(multiple 多选)
#         selected_mode='multiple',
#         # 图例的位置
#         # pos_top='5%', pos_right='50%',
#         # 图例的布局朝向，水平(vertical 垂直)
#         orient='horizontal',
#         # 图例形状
#         legend_icon='circle'
#     ),
#
#     # 工具箱设置
#     toolbox_opts=opts.ToolboxOpts(
#         # 是否显示工具栏组件
#         is_show=True,
#         # 布局朝向('vertical')
#         orient='vertical',
#         # 离上边距的距离
#         pos_top='10%',
#         # 离左边距的距离
#         pos_left='91%',
#
#         # 配置各个工具箱
#         feature=opts.ToolBoxFeatureOpts(
#
#             # 保存工具
#             opts.ToolBoxFeatureSaveAsImageOpts(
#                 # 是否显示
#                 is_show=True,
#                 # 提示语
#                 title="save",
#             ),
#
#             # 还原工具
#             opts.ToolBoxFeatureRestoreOpts(
#                 # 是否显示该工具
#                 is_show=True,
#                 # 提示语
#                 title="undo",
#             ),
#
#             # 数据视图工具
#             opts.ToolBoxFeatureDataViewOpts(
#                 # 是否显示该工具
#                 is_show=True,
#                 # 提示语
#                 title="data",
#                 # 是否不可编辑
#                 is_read_only=False,
#             ),
#
#             # 缩放工具配置项，直角坐标系适用
#             opts.ToolBoxFeatureDataZoomOpts(
#                 # 是否显示该工具。
#                 is_show=True,
#                 # 提示语
#                 zoom_title="zoom",
#                 # 提示语
#                 back_title="undo",
#             ),
#
#             # 图表类型切换，适用于直角坐标系
#             opts.ToolBoxFeatureMagicTypeOpts(
#                 # 是否显示该工具
#                 is_show=True,
#                 # 启用的动态类型('stack','line','bar','tiled')
#                 type_=['stack', 'bar', 'tiled'],
#                 # 折线标题文本
#                 # line_title="折线图",
#                 # 柱状标题文本
#                 bar_title="barplot",
#                 # 堆积标题文本
#                 stack_title="stack",
#                 # 平铺标题文
#                 tiled_title="tiled",
#             ),
#
#             # 工具箱选框组件配置项
#             opts.ToolBoxFeatureBrushOpts(
#                 # 选择显示哪些选框
#                 type_=[]
#             ),
#         )
#     ),
# )
# bars.render('bar.html')


final.plot_animated(filename='./perpendicular-example.gif',perpendicular_bar_func='mean')
