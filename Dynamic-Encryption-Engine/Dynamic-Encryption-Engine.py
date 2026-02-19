from PyQt5 import QtCore, QtGui, QtWidgets 
import os
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 623)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 290, 971, 231))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 311, 34))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(399, 540, 571, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 971, 231))
        self.textEdit.setObjectName("textEdit")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(330, 10, 651, 26))
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setProperty("aa", "")
        self.horizontalSlider.setProperty("qq", QtGui.QColor(0, 0, 0))
        self.horizontalSlider.setObjectName("horizontalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 85, 127);")


		# self.lineEdit.setText(str(self.horizontalSlider.value()))
		# self.lineEdit.setText(str(self.horizontalSlider.value()))

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_clicked2)
        self.pushButton_3.clicked.connect(self.pushButton_clicked3)
        self.pushButton_4.clicked.connect(self.pushButton_clicked4)
        self.pushButton_5.clicked.connect(self.pushButton_clicked5)
        self.horizontalSlider.valueChanged.connect(self.update_textbox)






        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff0616;\">حرك الاسليدر لختيار رقم المعادلة التى ستقوم بالتشفير</span></p></body></html>"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "سيظهر هنا فك النص المشفر اذا كان الالمربع العلوى فيى نص مشفر وتريد  فكة والعكس يظهر النص المشفر اذا كان المربع العلىوى يحتوى على نص عادى وتريد تشفيرة"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.lineEdit.setText(_translate("MainWindow", str(self.horizontalSlider.value())))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "اكتب رقم من 1 الى 100,000 او حرك الاسليدر على اليمين"))
        self.pushButton.setText(_translate("MainWindow", "تشفير"))
        self.pushButton_2.setText(_translate("MainWindow", "فك"))
        self.pushButton_3.setText(_translate("MainWindow", "حفظ النص الاصلى"))
        self.pushButton_4.setText(_translate("MainWindow", "حفظ النص المشفر"))
        self.pushButton_5.setText(_translate("MainWindow", "افراغ الصناديق"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "اكتب النص الذى تريد تشفيره ثم اكتب رقم المعادلة التى ستقوم فى صندوق النص العلوى او حرك الاسليدر لختيار رقمبالتشفير من 1 الى مئة الف"))
        self.horizontalSlider.setToolTip(_translate("MainWindow", "حرك الصليدر لختيار رقم المعادلة التى ستقوم بالتشفير"))
        self.menu.setTitle(_translate("MainWindow", "حول"))
        self.action.setText(_translate("MainWindow", "حول التك"))




    def update_textbox(self, value):
        self.lineEdit.setText(str(value))
        CACHE_FILE = 'Hosin_508857.json'
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                        json1 = json.load(f)
            except json.JSONDecodeError:
                print(f"تحذير: ملف الكاش '{CACHE_FILE}' تالف. سيتم إنشاء كاش جديد.")
        str1 = self.textEdit.toPlainText() 
        result =""
        i2=0
        i3 = self.lineEdit.text()
        for i in str1:
            code = ord(i) + int(json1[i3][i2])
            i2 = i2 + 1
            if i2 == len(json1[i3]): i2 = 0     
            result += chr(code) 
        self.textEdit_2.setPlainText(result)



    def pushButton_clicked(self):
        CACHE_FILE = 'Hosin_508857.json'
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                        json1 = json.load(f)
            except json.JSONDecodeError:
                print(f"تحذير: ملف الكاش '{CACHE_FILE}' تالف. سيتم إنشاء كاش جديد.")
        str1 = self.textEdit.toPlainText() 
        result =""
        i2=0
        i3 = self.lineEdit.text()
        for i in str1:
            code = ord(i) + int(json1[i3][i2])
            i2 = i2 + 1
            if i2 == len(json1[i3]): i2 = 0     
            result += chr(code) 
        self.textEdit_2.setPlainText(result) 

    def pushButton_clicked2(self):
        CACHE_FILE = 'Hosin_508857.json'
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                        json1 = json.load(f)
            except json.JSONDecodeError:
                print(f"تحذير: ملف الكاش '{CACHE_FILE}' تالف. سيتم إنشاء كاش جديد.")
        str1 = self.textEdit_2.toPlainText() 
        result =""
        i2=0
        i3 = self.lineEdit.text()
        for i in str1:
            code = ord(i) - int(json1[i3][i2])
            i2 = i2 + 1
            if i2 == len(json1[i3]): i2 = 0     
            result += chr(code) 
        self.textEdit_2.setPlainText(result)  


    def pushButton_clicked3(self):
        str11 = self.textEdit.toPlainText() 
        with open("النص الاصلى.txt", 'w', encoding='utf-8') as f:
                f.write(str(str11))              

    def pushButton_clicked4(self):
        str11 = self.textEdit_2.toPlainText() 
        i3 = self.lineEdit.text()
        with open("النص المشفر_"+str(i3)+".txt", 'w', encoding='utf-8') as f:
                f.write(str(str11))
          



    def pushButton_clicked5(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")  






        









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
