import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_MARFA(object):
    def setupUi(self, MARFA):
        MARFA.setObjectName("MARFA")
        MARFA.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MARFA)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(340, 60, 93, 51))
        self.btn.setObjectName("btn")
        self.btn.clicked.connect(self.add_circle)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 150, 600, 600))
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

        self.pixmap = QtGui.QPixmap(self.label.size())
        self.pixmap.fill(QtGui.QColor("black"))  # Correct way to specify black
        self.label.setPixmap(self.pixmap)

        self.retranslateUi(MARFA)
        QtCore.QMetaObject.connectSlotsByName(MARFA)

    def add_circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter = QtGui.QPainter(self.pixmap)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(*[randint(0, 255) for i in range(3)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.label.setPixmap(self.pixmap)  # Update the label

    def retranslateUi(self, MARFA):
        _translate = QtCore.QCoreApplication.translate
        MARFA.setWindowTitle(_translate("MARFA", "MARFA"))
        self.btn.setText(_translate("MARFA", "Add Circle"))
        self.label.setText(_translate("MARFA", ""))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MARFA = QtWidgets.QMainWindow()
    ui = Ui_MARFA()
    ui.setupUi(MARFA)  # Call setupUi here
    MARFA.show()
    sys.exit(app.exec())