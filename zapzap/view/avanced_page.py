from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/avanced_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Avanced(object):
    def setupUi(self, Avanced):
        Avanced.setObjectName("Avanced")
        Avanced.resize(476, 146)
        Avanced.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Avanced)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Avanced)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=Avanced)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.hideBarUsers = QtWidgets.QCheckBox(parent=Avanced)
        self.hideBarUsers.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.hideBarUsers.setObjectName("hideBarUsers")
        self.gridLayout.addWidget(self.hideBarUsers, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Avanced)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Avanced)
        QtCore.QMetaObject.connectSlotsByName(Avanced)

    def retranslateUi(self, Avanced):
        
        self.label.setText(_("Avanced Mode"))
        self.label_2.setText(_("Hide setting bar with only one user"))
        self.hideBarUsers.setText(_("Off"))
        self.label_3.setText(_("To access the settings use the menu in the tray or the shortcut Ctrl+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Avanced = QtWidgets.QWidget()
    ui = Ui_Avanced()
    ui.setupUi(Avanced)
    Avanced.show()
    sys.exit(app.exec())