import locale
import os
import logtool.log as log
import json
import ctypes
import sys
import mainwindow
from PySide6 import QtCore, QtWidgets, QtGui, QtMultimediaWidgets, QtMultimedia

# 获取系统语言
syslang = locale.getdefaultlocale()[0]
log.logINFO("your system default language is " + syslang)

# 加载本地化文件
i18n_file = open("i18n/" + syslang + ".json", "r")
i18n_file_r = i18n_file.read()
i18n_file.close()
translate = json.loads(i18n_file_r)
translate_this = translate["FastGALRunner.py"]

# 实例化class
app = QtWidgets.QApplication([])
mw = mainwindow.Ui_MainWindow()

# 判断所需文件是否都存在
if os.path.exists("config.json") == False:
    mw.msg_critical(translate_this["ConfigNotExistsErrorDialogText"])
    exit()
if os.path.exists("res") == False:
    mw.msg_critical(translate_this["ResourcesNotExistsErrorDialogText"])
    exit()
if os.path.exists("scripts") == False:
    mw.msg_critical(translate_this["ScriptsNotExistsErrorDialogText"])
    exit()

# 初始化ui与显示
mw.setupUi(mw)
mw.setupStart()
mw.show()

# 开始运行app
sys.exit(app.exec())
