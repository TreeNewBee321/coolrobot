# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSettings
from PyQt5.QtCore import QThread

from cqhttp import CQHttp
# import _thread
import time
import random
import requests
import json
import os
import sys
import urllib
import hashlib
import datetime
import pymysql
import backend
from itertools import groupby
from collections import defaultdict
# 引入时间调度器 apscheduler 的 BlockingScheduler
import lottery
from apscheduler.schedulers.blocking import BlockingScheduler

bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='',
             secret='')
# 实例化 BlockingScheduler
sched = BlockingScheduler()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(761, 484)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 721, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.proid = QtWidgets.QFrame(self.tab)
        self.proid.setGeometry(QtCore.QRect(30, 40, 621, 271))
        self.proid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.proid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.proid.setObjectName("proid")
        self.pro_id = QtWidgets.QLabel(self.proid)
        self.pro_id.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.pro_id.setObjectName("pro_id")
        self.lineEdit = QtWidgets.QLineEdit(self.proid)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.proid)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.proid)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 140, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.proid)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 100, 111, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.proid)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 240, 51, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox = QtWidgets.QCheckBox(self.proid)
        self.checkBox.setGeometry(QtCore.QRect(140, 240, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_9 = QtWidgets.QPushButton(self.proid)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 40, 91, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.proid)
        self.pushButton_10.setGeometry(QtCore.QRect(460, 40, 91, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_18 = QtWidgets.QLabel(self.proid)
        self.label_18.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.proid)
        self.label_19.setGeometry(QtCore.QRect(340, 10, 54, 12))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.proid)
        self.label_20.setGeometry(QtCore.QRect(340, 90, 101, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_13 = QtWidgets.QPushButton(self.proid)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 112, 91, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.listWidget_3 = QtWidgets.QListWidget(self.proid)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 100, 111, 121))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_28 = QtWidgets.QPushButton(self.proid)
        self.pushButton_28.setGeometry(QtCore.QRect(460, 110, 91, 31))
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 51, 20))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(30, 40, 271, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 10, 81, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 21, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 50, 81, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 21, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 90, 81, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(150, 10, 21, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 10, 81, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(150, 50, 21, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 50, 81, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(150, 90, 21, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 90, 81, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 120, 41, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 51, 16))
        self.label_10.setObjectName("label_10")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(30, 230, 271, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(60, 10, 51, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(60, 60, 51, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 60, 41, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(60, 110, 51, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 140, 41, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_48 = QtWidgets.QLabel(self.frame_2)
        self.label_48.setGeometry(QtCore.QRect(130, 10, 41, 16))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame_2)
        self.label_49.setGeometry(QtCore.QRect(130, 60, 41, 16))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.frame_2)
        self.label_50.setGeometry(QtCore.QRect(130, 110, 41, 16))
        self.label_50.setObjectName("label_50")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_37.setGeometry(QtCore.QRect(180, 10, 51, 20))
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_38.setGeometry(QtCore.QRect(180, 60, 51, 20))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_39.setGeometry(QtCore.QRect(180, 110, 51, 20))
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(340, 20, 61, 16))
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(340, 200, 61, 16))
        self.label_16.setObjectName("label_16")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(330, 40, 351, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 20, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 20, 51, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(90, 80, 181, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 80, 51, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_2.setGeometry(QtCore.QRect(190, 120, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setGeometry(QtCore.QRect(280, 120, 51, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setGeometry(QtCore.QRect(330, 230, 351, 171))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(200, 30, 113, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 60, 51, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_12.setGeometry(QtCore.QRect(240, 120, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_10.raise_()
        self.frame.raise_()
        self.label_3.raise_()
        self.frame_2.raise_()
        self.label_14.raise_()
        self.label_16.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(20, 30, 51, 21))
        self.label_21.setObjectName("label_21")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(90, 30, 221, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(20, 80, 51, 21))
        self.label_22.setObjectName("label_22")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(90, 80, 221, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(20, 130, 51, 21))
        self.label_44.setObjectName("label_44")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_33.setGeometry(QtCore.QRect(90, 130, 221, 20))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.label_45 = QtWidgets.QLabel(self.tab_3)
        self.label_45.setGeometry(QtCore.QRect(20, 180, 51, 21))
        self.label_45.setObjectName("label_45")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_34.setGeometry(QtCore.QRect(90, 180, 221, 20))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_46 = QtWidgets.QLabel(self.tab_3)
        self.label_46.setGeometry(QtCore.QRect(20, 230, 51, 21))
        self.label_46.setObjectName("label_46")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_35.setGeometry(QtCore.QRect(90, 230, 221, 20))
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.label_47 = QtWidgets.QLabel(self.tab_3)
        self.label_47.setGeometry(QtCore.QRect(20, 290, 51, 21))
        self.label_47.setObjectName("label_47")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_36.setGeometry(QtCore.QRect(90, 290, 221, 20))
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_27.setGeometry(QtCore.QRect(500, 322, 121, 31))
        self.pushButton_27.setObjectName("pushButton_27")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        # 持久化存储
        
        # 播报群号列表
        self.groupList = []
        # 官托id列表
        self.idList = []
        # 当前目录
        self.cwd = os.getcwd()
        # 多线程
        self.work = WorkThread()
        self.group =  GroupThread()
        # 保存概率设置
        self.pushButton_4.clicked.connect(self.readCardRate)
        # 填写项目id
        self.pushButton.clicked.connect(self.getProId)
        # 填写广播群号
        self.pushButton_3.clicked.connect(self.getGroupId)
        # 确认是否开始抽卡
        self.pushButton_6.clicked.connect(self.switchCard)
        # 设置资金档位
        self.pushButton_2.clicked.connect(self.setCardThreshold)
        # 设置播报文件夹
        self.pushButton_11.clicked.connect(self.setBroadCastDir)
        self.pushButton_5.clicked.connect(self.setNormalBroadCastDir)
        self.pushButton_7.clicked.connect(self.setHighRateBroadCastDir)
        # 添加官托摩点id
        self.pushButton_8.clicked.connect(self.setSpId)  
        # 保存官托id设置
        self.pushButton_12.clicked.connect(self.saveSpIdSettings)
        # 开始播报
        self.pushButton_9.clicked.connect(self.start)
        # 停止播报
        self.pushButton_10.clicked.connect(self.stop)
        # 开始群消息响应
        self.pushButton_13.clicked.connect(self.startDaemon)
        # 保存数据库设置
        self.pushButton_27.clicked.connect(self.saveDatabase)
        # 停止群消息相应
        self.pushButton_28.clicked.connect(self.stopDaemon)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.readConfig()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "黄球球机器人"))
        self.pro_id.setText(_translate("Form", "项目id"))
        self.pushButton.setText(_translate("Form", "保存"))
        self.pushButton_3.setText(_translate("Form", "添加群号"))
        self.pushButton_6.setText(_translate("Form", "保存"))
        self.checkBox.setText(_translate("Form", "抽卡开关"))
        self.pushButton_9.setText(_translate("Form", "开始播报"))
        self.pushButton_10.setText(_translate("Form", "停止播报"))
        self.label_18.setText(_translate("Form", "播报群号"))
        self.label_19.setText(_translate("Form", "播报开关"))
        self.label_20.setText(_translate("Form", "群状态监控开关"))
        self.pushButton_13.setText(_translate("Form", "开始监控"))
        self.pushButton_28.setText(_translate("Form", "停止监控"))
        self.label_2.setText(_translate("Form", "项目设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "摩点"))
        self.label_4.setText(_translate("Form", "N"))
        self.label_5.setText(_translate("Form", "R"))
        self.label_6.setText(_translate("Form", "SR"))
        self.label_7.setText(_translate("Form", "SP"))
        self.label_8.setText(_translate("Form", "SSR"))
        self.label_9.setText(_translate("Form", "UR"))
        self.pushButton_4.setText(_translate("Form", "保存"))
        self.label_3.setText(_translate("Form", "概率设置"))
        self.label_10.setText(_translate("Form", "档位设置"))
        self.label_11.setText(_translate("Form", "第一档"))
        self.label_12.setText(_translate("Form", "第二档"))
        self.label_13.setText(_translate("Form", "第三档"))
        self.pushButton_2.setText(_translate("Form", "保存"))
        self.label_48.setText(_translate("Form", "第四档"))
        self.label_49.setText(_translate("Form", "第五档"))
        self.label_50.setText(_translate("Form", "第六档"))
        self.label_14.setText(_translate("Form", "文件夹设置"))
        self.label_16.setText(_translate("Form", "官托设置"))
        self.label_15.setText(_translate("Form", "卡片文件夹"))
        self.pushButton_5.setText(_translate("Form", "浏览"))
        self.label_17.setText(_translate("Form", "高概率文件夹"))
        self.pushButton_7.setText(_translate("Form", "浏览"))
        self.checkBox_2.setText(_translate("Form", "高概率模式"))
        self.pushButton_11.setText(_translate("Form", "保存"))
        self.pushButton_8.setText(_translate("Form", "添加id"))
        self.pushButton_12.setText(_translate("Form", "保存设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "抽卡"))
        self.label_21.setText(_translate("Form", "host"))
        self.lineEdit_15.setText(_translate("Form", "localhost"))
        self.label_22.setText(_translate("Form", "port"))
        self.lineEdit_16.setText(_translate("Form", "3306"))
        self.label_44.setText(_translate("Form", "数据库名"))
        self.lineEdit_33.setText(_translate("Form", "htt"))
        self.label_45.setText(_translate("Form", "用户名"))
        self.lineEdit_34.setText(_translate("Form", "root"))
        self.label_46.setText(_translate("Form", "密码"))
        self.lineEdit_35.setText(_translate("Form", "password"))
        self.label_47.setText(_translate("Form", "charset"))
        self.lineEdit_36.setText(_translate("Form", "utf8"))
        self.pushButton_27.setText(_translate("Form", "保存数据库设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "数据库"))



    # 获取倍率
    def readCardRate(self):
        n_rate = self.lineEdit_4.text()
        r_rate = self.lineEdit_5.text()
        sr_rate = self.lineEdit_6.text()
        sp_rate = self.lineEdit_7.text()
        ssr_rate = self.lineEdit_8.text()
        ur_rate = self.lineEdit_9.text()
        if n_rate and r_rate and sr_rate and sp_rate and ssr_rate and ur_rate != "":
            # 抽卡
            lottery.getRate(int(n_rate),int(r_rate),int(sr_rate),int(sp_rate),int(ssr_rate),int(ur_rate))
            # 
        else:
            reply = QMessageBox.warning(QtWidgets.QMainWindow(), "warning", "倍率设置不可以为空！",QMessageBox.Ok)
    # 获取项目id
    def getProId(self):
        pro_id = self.lineEdit.text()
        if pro_id == "":
            reply = QMessageBox.warning(self, "warning", "项目id不可以为空！",QMessageBox.Ok)
        else:
            pro_ids = []
            pro_ids.append(int(pro_id))
            lottery.pro_id = int(pro_id)
            lottery.pro_ids = pro_ids
            print(lottery.pro_id)
            print(lottery.pro_ids)
    # 是否开启抽卡开关
    def switchCard(self):
        card_switch = int(self.checkBox.checkState())
        if card_switch == 2:
            lottery.cardswitch = True
        else:
            lottery.cardswitch = False
        print(lottery.cardswitch)
    # 设置资金档位
    def setCardThreshold(self):
        thresh = []
        if self.lineEdit_10.text() != "":
            thresh.append(float(self.lineEdit_10.text()))
        if self.lineEdit_11.text() != "":    
            thresh.append(float(self.lineEdit_11.text()))
        if self.lineEdit_12.text() != "":
            thresh.append(float(self.lineEdit_12.text()))
        if self.lineEdit_37.text() != "":
            thresh.append(float(self.lineEdit_37.text()))
        if self.lineEdit_38.text() != "":
            thresh.append(float(self.lineEdit_38.text()))
        if self.lineEdit_39.text() != "":
            thresh.append(float(self.lineEdit_39.text()))
        if len(thresh) == 6:
            reply = QMessageBox.warning(QtWidgets.QMainWindow(), "warning", "已保存资金档位设置",QMessageBox.Ok)
        else:
            reply = QMessageBox.warning(QtWidgets.QMainWindow(), "warning", "保存资金档位失败",QMessageBox.Ok)
        lottery.backerList = thresh
        print(lottery.backerList)

    # 设置播报文件夹 
    def setBroadCastDir(self):
        # 设置文件夹路径
        lottery.normalDir = self.lineEdit_2.text()
        lottery.highRateDir = self.lineEdit_13.text()
        normalTitle = self.lineEdit_2.text().split('/')
        highRateTitle = self.lineEdit_13.text().split('/')
        lottery.normalTitle = normalTitle[len(normalTitle)-1]
        lottery.highRateTitle = highRateTitle[len(highRateTitle)-1]
        # 设置高概率开关
        highrate_switch = int(self.checkBox_2.checkState())
        if  highrate_switch == 2:
            lottery.highrate_switch = True
        else:
            lottery.highrate_switch = False   
        print(lottery.highrate_switch)
        print(lottery.normalDir)     
        print(lottery.highRateDir)
    def setNormalBroadCastDir(self):
        normal_path = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QMainWindow(),  "选择普通文件夹",  self.cwd)
        self.lineEdit_2.setText(normal_path)
    def setHighRateBroadCastDir(self):
        highrate_path = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QMainWindow(),  "选择高概率文件夹",   self.cwd)       
        self.lineEdit_13.setText(highrate_path)  
    # 获取群号
    def getGroupId(self):
        if self.lineEdit_3.text() !="":
            self.groupList.append(int(self.lineEdit_3.text()))
        self.listWidget_3.addItem(self.lineEdit_3.text())
        self.lineEdit_3.clear()
        if len(self.groupList) == 0:
            reply = QMessageBox.warning(self, "warning", "播报群号不可以为空！",QMessageBox.Ok)
        else:
            lottery.group_id = self.groupList
            print(lottery.group_id)      
    # 设置官托摩点id
    def setSpId(self):
        self.idList.append(self.lineEdit_14.text())
        self.listWidget.addItem(self.lineEdit_14.text())
        self.lineEdit_14.clear()

    # 保存官托id设置
    def saveSpIdSettings(self):
        lottery.SpId = self.idList
        print(lottery.SpId)

    # 开启播报
    def start(self):
        self.writeConfig()        
        self.work.start()
    # 关闭播报
    def stop(self):
        # self.work.exit()
        self.work.terminate()
        # self.work.wait()
    # 开启群监控
    def startDaemon(self):
        backend.group_id = self.groupList
        if len(self.groupList) == 0:
            reply = QMessageBox.warning(self, "warning", "播报群号不可以为空！",QMessageBox.Ok)
        self.group.start()
    
    # 保存数据库
    def saveDatabase(self):
        lottery.host = self.lineEdit_15.text()
        port = self.lineEdit_16.text()
        lottery.port = int(port)
        lottery.user = self.lineEdit_34.text()
        lottery.password = self.lineEdit_35.text()
        lottery.database = self.lineEdit_33.text()
        lottery.charset = self.lineEdit_36.text()
        print(lottery.host,lottery.port,lottery.user,lottery.password,lottery.database,lottery.charset)
        reply = QMessageBox.warning(QtWidgets.QMainWindow(), "warning", "已保存数据库设置",QMessageBox.Ok)
    
    def stopDaemon(self):
        self.group.terminate()
    
    def writeConfig(self):
        settings = QSettings('./robot.ini',QSettings.IniFormat)
        #倍率
        settings.setValue('n_rate', self.lineEdit_4.text())
        settings.setValue('r_rate', self.lineEdit_5.text())
        settings.setValue('sr_rate', self.lineEdit_6.text())
        settings.setValue('sp_rate', self.lineEdit_7.text())
        settings.setValue('ssr_rate', self.lineEdit_8.text())
        settings.setValue('ur_rate', self.lineEdit_9.text())
        #项目id
        settings.setValue('pro_id', self.lineEdit.text())
        #播报群号
        settings.setValue('groupList', self.groupList)
        #官托id
        settings.setValue('idList', self.idList)
        #资金档位设置
        settings.setValue('class_1',self.lineEdit_10.text())
        settings.setValue('class_2',self.lineEdit_11.text())
        settings.setValue('class_3',self.lineEdit_12.text())
        settings.setValue('class_4',self.lineEdit_37.text())
        settings.setValue('class_5',self.lineEdit_38.text())
        settings.setValue('class_6',self.lineEdit_39.text())
        #文件夹设置
        settings.setValue('normal',self.lineEdit_2.text())
        settings.setValue('highrate',self.lineEdit_13.text())
        #数据库设置
        settings.setValue('host',self.lineEdit_15.text())
        settings.setValue('port',self.lineEdit_16.text())
        settings.setValue('user',self.lineEdit_34.text())
        settings.setValue('password',self.lineEdit_35.text())
        settings.setValue('db',self.lineEdit_33.text())
        settings.setValue('charset',self.lineEdit_36.text())
    
    def readConfig(self):
        settings = QSettings('./robot.ini',QSettings.IniFormat)
        # 倍率
        self.lineEdit_4.setText(settings.value('n_rate'))
        self.lineEdit_5.setText(settings.value('r_rate'))
        self.lineEdit_6.setText(settings.value('sr_rate'))
        self.lineEdit_7.setText(settings.value('sp_rate'))
        self.lineEdit_8.setText(settings.value('ssr_rate'))
        self.lineEdit_9.setText(settings.value('ur_rate'))
        self.readCardRate()
        # 项目id
        self.lineEdit.setText(settings.value('pro_id'))
        self.getProId()
        # 播报群号
        self.groupList = settings.value('groupList')
        for groupid in self.groupList:
            self.listWidget_3.addItem(str(groupid))
        self.getGroupId()
        # 资金档位设置
        self.lineEdit_10.setText(settings.value('class_1'))
        self.lineEdit_11.setText(settings.value('class_2'))
        self.lineEdit_12.setText(settings.value('class_3'))
        self.lineEdit_37.setText(settings.value('class_4'))
        self.lineEdit_38.setText(settings.value('class_5'))
        self.lineEdit_39.setText(settings.value('class_6'))  
        self.setCardThreshold()
        # 文件夹     
        self.lineEdit_2.setText(str(settings.value('normal')))
        self.lineEdit_13.setText(str(settings.value('highrate')))
        self.setBroadCastDir()
        # 数据库
        self.lineEdit_15.setText(settings.value('host'))
        self.lineEdit_16.setText(settings.value('port'))
        self.lineEdit_34.setText(settings.value('user'))
        self.lineEdit_35.setText(settings.value('password'))
        self.lineEdit_33.setText(settings.value('db'))
        self.lineEdit_36.setText(settings.value('charset'))
        self.saveDatabase()
# 抽卡线程
class WorkThread(QThread):
    # trigger = pyqtSignal()
    def __int__(self):
        super(WorkThread,self).__init__()
 
    def run(self):
        global sched
        if lottery.normalDir or lottery.highRateDir != "":
            sched.add_job(lottery.getOrders(lottery.pro_ids,lottery.group_id,lottery.cardswitch,lottery.backerList), 'interval', seconds=20)
            sched.start()           
        else:
            reply = QMessageBox.warning(QtWidgets.QMainWindow(), "warning", "卡片存放文件夹不可以为空！",QMessageBox.Ok)

# 群消息响应线程
class GroupThread(QThread):
    def __int__(self):
        super(GroupThread,self).__init__()
 
    def run(self):
        backend.threadStart()