from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MARFA(object):
    def setupUi(self, MARFA):
        MARFA.setObjectName("MARFA")
        MARFA.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MARFA)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(340, 60, 93, 51))
        self.btn.setObjectName("btn")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 150, 511, 341))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        MARFA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MARFA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MARFA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MARFA)
        self.statusbar.setObjectName("statusbar")
        MARFA.setStatusBar(self.statusbar)

        self.retranslateUi(MARFA)
        QtCore.QMetaObject.connectSlotsByName(MARFA)

    def retranslateUi(self, MARFA):
        _translate = QtCore.QCoreApplication.translate
        MARFA.setWindowTitle(_translate("MARFA", "MARFA"))
        self.btn.setText(_translate("MARFA", "PushButton"))
        self.label.setText(_translate("MARFA", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MARFA = QtWidgets.QMainWindow()
    ui = Ui_MARFA()
    ui.setupUi(MARFA)
    MARFA.show()
    sys.exit(app.exec())
