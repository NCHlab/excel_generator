# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_menu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(444, 346)
        MainWindow.setMinimumSize(QSize(400, 330))
        self.quickcreate_ACTION = QAction(MainWindow)
        self.quickcreate_ACTION.setObjectName(u"quickcreate_ACTION")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.exit_ACTION = QAction(MainWindow)
        self.exit_ACTION.setObjectName(u"exit_ACTION")
        self.clearfields_ACTION = QAction(MainWindow)
        self.clearfields_ACTION.setObjectName(u"clearfields_ACTION")
        self.create_ACTION = QAction(MainWindow)
        self.create_ACTION.setObjectName(u"create_ACTION")
        self.create_ACTION.setShortcutVisibleInContextMenu(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_frm = QFrame(self.centralwidget)
        self.main_frm.setObjectName(u"main_frm")
        self.main_frm.setFrameShape(QFrame.StyledPanel)
        self.main_frm.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sheetname_LBL = QLabel(self.main_frm)
        self.sheetname_LBL.setObjectName(u"sheetname_LBL")
        self.sheetname_LBL.setMinimumSize(QSize(77, 0))

        self.horizontalLayout_2.addWidget(self.sheetname_LBL)

        self.sheetname_LE = QLineEdit(self.main_frm)
        self.sheetname_LE.setObjectName(u"sheetname_LE")
        self.sheetname_LE.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.sheetname_LE)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.filepath_LBL = QLabel(self.main_frm)
        self.filepath_LBL.setObjectName(u"filepath_LBL")
        self.filepath_LBL.setMinimumSize(QSize(77, 0))

        self.horizontalLayout_3.addWidget(self.filepath_LBL)

        self.filepath_LE = QLineEdit(self.main_frm)
        self.filepath_LE.setObjectName(u"filepath_LE")
        self.filepath_LE.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.filepath_LE)

        self.filepath_TB = QToolButton(self.main_frm)
        self.filepath_TB.setObjectName(u"filepath_TB")

        self.horizontalLayout_3.addWidget(self.filepath_TB)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cols_LBL = QLabel(self.main_frm)
        self.cols_LBL.setObjectName(u"cols_LBL")
        self.cols_LBL.setMinimumSize(QSize(77, 0))
        self.cols_LBL.setMaximumSize(QSize(77, 16777215))

        self.horizontalLayout_5.addWidget(self.cols_LBL)

        self.cols_CB = QComboBox(self.main_frm)
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.addItem("")
        self.cols_CB.setObjectName(u"cols_CB")
        self.cols_CB.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_5.addWidget(self.cols_CB)

        self.checkBox = QCheckBox(self.main_frm)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filename_LBL = QLabel(self.main_frm)
        self.filename_LBL.setObjectName(u"filename_LBL")
        self.filename_LBL.setMinimumSize(QSize(77, 0))

        self.horizontalLayout.addWidget(self.filename_LBL)

        self.filename_LE = QLineEdit(self.main_frm)
        self.filename_LE.setObjectName(u"filename_LE")
        self.filename_LE.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.filename_LE)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rows_LBL = QLabel(self.main_frm)
        self.rows_LBL.setObjectName(u"rows_LBL")
        self.rows_LBL.setMinimumSize(QSize(77, 0))
        self.rows_LBL.setMaximumSize(QSize(77, 16777215))

        self.horizontalLayout_4.addWidget(self.rows_LBL)

        self.rows_CB = QComboBox(self.main_frm)
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.addItem("")
        self.rows_CB.setObjectName(u"rows_CB")
        self.rows_CB.setMinimumSize(QSize(74, 0))
        self.rows_CB.setMaximumSize(QSize(74, 16777215))

        self.horizontalLayout_4.addWidget(self.rows_CB)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.accenttype_LBL = QLabel(self.main_frm)
        self.accenttype_LBL.setObjectName(u"accenttype_LBL")
        self.accenttype_LBL.setMinimumSize(QSize(75, 0))
        self.accenttype_LBL.setMaximumSize(QSize(77, 16777215))

        self.horizontalLayout_6.addWidget(self.accenttype_LBL)

        self.accenttype_CB = QComboBox(self.main_frm)
        self.accenttype_CB.addItem("")
        self.accenttype_CB.addItem("")
        self.accenttype_CB.addItem("")
        self.accenttype_CB.addItem("")
        self.accenttype_CB.addItem("")
        self.accenttype_CB.addItem("")
        self.accenttype_CB.setObjectName(u"accenttype_CB")
        self.accenttype_CB.setEnabled(True)
        self.accenttype_CB.setMaximumSize(QSize(75, 16777215))
        self.accenttype_CB.setLayoutDirection(Qt.LeftToRight)
        self.accenttype_CB.setInsertPolicy(QComboBox.InsertAtBottom)

        self.horizontalLayout_6.addWidget(self.accenttype_CB)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.create_PB = QPushButton(self.main_frm)
        self.create_PB.setObjectName(u"create_PB")

        self.horizontalLayout_7.addWidget(self.create_PB)

        self.quickcreate_PB = QPushButton(self.main_frm)
        self.quickcreate_PB.setObjectName(u"quickcreate_PB")

        self.horizontalLayout_7.addWidget(self.quickcreate_PB)

        self.cancel_PB = QPushButton(self.main_frm)
        self.cancel_PB.setObjectName(u"cancel_PB")

        self.horizontalLayout_7.addWidget(self.cancel_PB)


        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.headers_LBL = QLabel(self.main_frm)
        self.headers_LBL.setObjectName(u"headers_LBL")
        self.headers_LBL.setMinimumSize(QSize(77, 0))

        self.horizontalLayout_8.addWidget(self.headers_LBL)

        self.headers_LE = QLineEdit(self.main_frm)
        self.headers_LE.setObjectName(u"headers_LE")
        self.headers_LE.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_8.addWidget(self.headers_LE)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.main_frm, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 444, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.create_ACTION)
        self.menuFile.addAction(self.quickcreate_ACTION)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_ACTION)
        self.menuEdit.addAction(self.clearfields_ACTION)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.quickcreate_ACTION.setText(QCoreApplication.translate("MainWindow", u"Quick Create", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.exit_ACTION.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.clearfields_ACTION.setText(QCoreApplication.translate("MainWindow", u"Clear Fields", None))
        self.create_ACTION.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.sheetname_LBL.setText(QCoreApplication.translate("MainWindow", u"Sheet Name", None))
        self.sheetname_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sheet1", None))
        self.filepath_LBL.setText(QCoreApplication.translate("MainWindow", u"File Path", None))
        self.filepath_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select filepath....", None))
        self.filepath_TB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.cols_LBL.setText(QCoreApplication.translate("MainWindow", u"Columns", None))
        self.cols_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.cols_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.cols_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.cols_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.cols_CB.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.cols_CB.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.cols_CB.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.cols_CB.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.cols_CB.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.cols_CB.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Force Column", None))
        self.filename_LBL.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.filename_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter filename....", None))
        self.rows_LBL.setText(QCoreApplication.translate("MainWindow", u"Rows", None))
        self.rows_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.rows_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.rows_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.rows_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.rows_CB.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.rows_CB.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.rows_CB.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.rows_CB.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.rows_CB.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.rows_CB.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.accenttype_LBL.setText(QCoreApplication.translate("MainWindow", u"Accent Type", None))
        self.accenttype_CB.setItemText(0, QCoreApplication.translate("MainWindow", u"Accent1", None))
        self.accenttype_CB.setItemText(1, QCoreApplication.translate("MainWindow", u"Accent2", None))
        self.accenttype_CB.setItemText(2, QCoreApplication.translate("MainWindow", u"Accent3", None))
        self.accenttype_CB.setItemText(3, QCoreApplication.translate("MainWindow", u"Accent4", None))
        self.accenttype_CB.setItemText(4, QCoreApplication.translate("MainWindow", u"Accent5", None))
        self.accenttype_CB.setItemText(5, QCoreApplication.translate("MainWindow", u"Accent6", None))

        self.create_PB.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.quickcreate_PB.setText(QCoreApplication.translate("MainWindow", u"Quick Create", None))
        self.cancel_PB.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.headers_LBL.setText(QCoreApplication.translate("MainWindow", u"Headers", None))
        self.headers_LE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"header1, header2, header3, header4....", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

