# -*- coding: utf-8 -*- #
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QVBoxLayout, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import numpy as np
import jieba
import pandas as pd
from gensim import corpora, models
import os
def test():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    df_a = pd.read_json('data/commet_all.json', lines=True, encoding='utf-8')
    df_a.isnull().sum()
    df_a.dropna(axis=0, inplace=True)
    df_a.drop_duplicates(inplace=True)
    df_groupby_score = df_a.groupby('cmt_star')
    df_groupby_score['cmt_id'].count()
    plt.figure(figsize=(10, 6), dpi=80)
    df_groupby_score['cmt_id'].count().plot(kind='bar')  # 先统计再画图
    df_a['cmt_star'].hist(bins=10, figsize=(10, 6))  # 画图时统计
    plt.title('评分人数分布情况')
    plt.ylabel('人数')
    plt.xlabel('评分')
    plt.show()

if __name__ == '__main__':
    test()
