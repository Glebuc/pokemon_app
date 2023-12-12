# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(697, 487)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"background-color: white;\n"
"}\n"
"QPushButton {\n"
"border: 1px solid white;\n"
"background-color: rgb(163, 9, 37);\n"
"padding: 5, 10;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"border: 1px solid white;\n"
"background-color: rgb(190, 21, 46) ;\n"
"padding: 5, 10;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnViewPokemon = QPushButton(self.frame)
        self.btnViewPokemon.setObjectName(u"btnViewPokemon")

        self.horizontalLayout_4.addWidget(self.btnViewPokemon)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_4.addWidget(self.frame)

        self.tablePokemon = QTableView(self.tab)
        self.tablePokemon.setObjectName(u"tablePokemon")
        self.tablePokemon.setStyleSheet(u"background-color: rgb(255, 56, 21);")

        self.verticalLayout_4.addWidget(self.tablePokemon)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frameSearchPokemon = QFrame(self.tab_2)
        self.frameSearchPokemon.setObjectName(u"frameSearchPokemon")
        self.frameSearchPokemon.setMaximumSize(QSize(300, 16777215))
        self.frameSearchPokemon.setStyleSheet(u"#frame {\n"
"background-color: #454641;\n"
"}\n"
"#label {\n"
"background-color: #454641;\n"
"}\n"
"#label_3 {\n"
"background-color: #454641;\n"
"}")
        self.frameSearchPokemon.setFrameShape(QFrame.StyledPanel)
        self.frameSearchPokemon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameSearchPokemon)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frameSearchPokemon)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.frameSearchPokemon)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;\n"
"font-size: 15px;")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignBottom)

        self.searchPokemon = QLineEdit(self.frameSearchPokemon)
        self.searchPokemon.setObjectName(u"searchPokemon")
        self.searchPokemon.setStyleSheet(u"border: 3px solid #eee;\n"
"background-color: #eee;")

        self.verticalLayout.addWidget(self.searchPokemon)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.btnSearchPokemon = QPushButton(self.frameSearchPokemon)
        self.btnSearchPokemon.setObjectName(u"btnSearchPokemon")
        self.btnSearchPokemon.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnSearchPokemon.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Pokemon/static/search-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSearchPokemon.setIcon(icon)

        self.verticalLayout.addWidget(self.btnSearchPokemon)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addWidget(self.frameSearchPokemon)

        self.frameViewPokemon = QFrame(self.tab_2)
        self.frameViewPokemon.setObjectName(u"frameViewPokemon")
        self.frameViewPokemon.setFrameShape(QFrame.StyledPanel)
        self.frameViewPokemon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameViewPokemon)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frameViewPokemon)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addWidget(self.frameViewPokemon)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnViewPokemon.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0441\u0435\u0445 \u043f\u043e\u043a\u0435\u043c\u043e\u043d\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"POKEDEX", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043a\u0435\u043c\u043e\u043d\u0430 \u0438\u043b\u0438 ID", None))
        self.searchPokemon.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pikachu", None))
        self.btnSearchPokemon.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438..", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0414\u0415\u0421\u042c \u041f\u041e\u041a\u0410 \u041d\u0418\u0427\u0415\u0413\u041e \u041d\u0415\u0422....", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u043a\u0435\u043c\u043e\u043d\u0430", None))
    # retranslateUi

