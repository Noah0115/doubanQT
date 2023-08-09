# -*- coding: utf-8 -*- #
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableView, QVBoxLayout, QWidget, QPushButton, QGridLayout, \
    QGroupBox, QLabel
import view
class Demo(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = view.Ui_MainWindow()
        self.ui.setupUi(self)
        self.label = QLabel(self.ui.label)
        self.label.setGeometry(0, 0, 780, 470)
        self.init_ui()
    def init_ui(self):
        self.ui.btn1.clicked.connect(self.ciyun)
        self.ui.btn2.clicked.connect(self.goodbadsquard)
        self.ui.btn3.clicked.connect(self.pingjirenshubingzhuangtu)
        self.ui.btn4.clicked.connect(self.pingjirenshuzhifangtu)
        self.ui.btn5.clicked.connect(self.diananxingshuliangfenbu)
        self.ui.btn6.clicked.connect(self.pianduanhaopingrenshufenbuzhifangtu)
        self.ui.btn7.clicked.connect(self.pianduanhaopingrenshufenbubingzhuangtu)
        self.ui.btn8.clicked.connect(self.pingxingjirenshufenbubingzhuangtu)
        self.ui.btn9.clicked.connect(self.pinglunnianfenzhifangtu)
        self.ui.btn10.clicked.connect(self.doubanpingfenfenbuzhifnagtu)

    def ciyun(self):
        # 从文件读取词云图片并显示
        pixmap = QPixmap('关键词词云.png').scaled(780,470)

        self.label.setPixmap(pixmap)
    def goodbadsquard(self):
        # 从文件读取直方图图片并显示
        pixmap = QPixmap('好坏评级人数分布直方图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def pingjirenshubingzhuangtu(self):
        pixmap = QPixmap('好坏评级人数分布饼状图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def pingjirenshuzhifangtu(self):
        pixmap = QPixmap('每个评分人数分布图直方图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def diananxingshuliangfenbu(self):
        pixmap = QPixmap('点赞星数量分布饼状图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def pianduanhaopingrenshufenbuzhifangtu(self):
        pixmap = QPixmap('片段好评人数分布直方图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def pianduanhaopingrenshufenbubingzhuangtu(self):
        pixmap = QPixmap('片段好评人数分布饼状图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def pingxingjirenshufenbubingzhuangtu(self):
        pixmap = QPixmap('评星级人数分布饼状图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def pinglunnianfenzhifangtu(self):
        pixmap = QPixmap('评论年份分布直方图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
    def doubanpingfenfenbuzhifnagtu(self):
        pixmap = QPixmap('豆瓣评分人数分布直方图.png').scaled(780,470)
        self.label.setPixmap(pixmap)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())