# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_obj(object):
    def setupUi(self, obj):
        obj.setObjectName("obj")
        obj.resize(400, 184)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        obj.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(obj)
        self.gridLayout.setObjectName("gridLayout")
        self.hint = QtWidgets.QLabel(obj)
        self.hint.setText("")
        self.hint.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hint.setObjectName("hint")
        self.gridLayout.addWidget(self.hint, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(obj)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(obj)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(obj)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(obj)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 3, 2, 1)

        self.retranslateUi(obj)
        self.buttonBox.accepted.connect(obj.accept)
        self.buttonBox.rejected.connect(obj.reject)
        self.lineEdit.returnPressed.connect(self.textBrowser.update)
        QtCore.QMetaObject.connectSlotsByName(obj)

    def retranslateUi(self, obj):
        _translate = QtCore.QCoreApplication.translate
        obj.setWindowTitle(_translate("obj", "dirty_box"))
        self.label.setText(_translate("obj", "ENTER YOUR NAME  :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    obj = QtWidgets.QDialog()
    ui = Ui_obj()
    ui.setupUi(obj)
    obj.show()
    sys.exit(app.exec_())

