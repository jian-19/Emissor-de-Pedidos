# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(440, 740)
        MainWindow.setMinimumSize(QtCore.QSize(440, 740))
        MainWindow.setMaximumSize(QtCore.QSize(440, 740))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:/programação/cartucho/imagens/29313 (1).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(1105, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 10, 281, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("c:/programação/cartucho/imagens/inffo.png"))
        self.logo.setObjectName("logo")
        self.informacoes = QtWidgets.QLabel(self.centralwidget)
        self.informacoes.setGeometry(QtCore.QRect(10, 670, 421, 31))
        self.informacoes.setObjectName("informacoes")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 200, 301, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.input_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_name.setObjectName("input_name")
        self.horizontalLayout.addWidget(self.input_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_telefone = QtWidgets.QLabel(self.layoutWidget)
        self.label_telefone.setObjectName("label_telefone")
        self.horizontalLayout_2.addWidget(self.label_telefone)
        self.input_telefone = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_telefone.setObjectName("input_telefone")
        self.horizontalLayout_2.addWidget(self.input_telefone)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_endereco = QtWidgets.QLabel(self.layoutWidget)
        self.label_endereco.setObjectName("label_endereco")
        self.horizontalLayout_3.addWidget(self.label_endereco)
        self.input_endereco = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_endereco.setObjectName("input_endereco")
        self.horizontalLayout_3.addWidget(self.input_endereco)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_qnt = QtWidgets.QLineEdit(self.centralwidget)
        self.line_qnt.setGeometry(QtCore.QRect(30, 370, 41, 20))
        self.line_qnt.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.line_qnt.setObjectName("line_qnt")
        self.line_descricao = QtWidgets.QLineEdit(self.centralwidget)
        self.line_descricao.setGeometry(QtCore.QRect(80, 370, 150, 20))
        self.line_descricao.setObjectName("line_descricao")
        self.label_qnt = QtWidgets.QLabel(self.centralwidget)
        self.label_qnt.setGeometry(QtCore.QRect(30, 350, 41, 16))
        self.label_qnt.setObjectName("label_qnt")
        self.label_descricao = QtWidgets.QLabel(self.centralwidget)
        self.label_descricao.setGeometry(QtCore.QRect(90, 350, 131, 16))
        self.label_descricao.setObjectName("label_descricao")
        self.label_unidade = QtWidgets.QLabel(self.centralwidget)
        self.label_unidade.setGeometry(QtCore.QRect(240, 350, 41, 16))
        self.label_unidade.setObjectName("label_unidade")
        self.label_valor = QtWidgets.QLabel(self.centralwidget)
        self.label_valor.setGeometry(QtCore.QRect(290, 350, 61, 16))
        self.label_valor.setObjectName("label_valor")
        self.line_unidade = QtWidgets.QLineEdit(self.centralwidget)
        self.line_unidade.setGeometry(QtCore.QRect(240, 370, 41, 20))
        self.line_unidade.setObjectName("line_unidade")
        self.line_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.line_valor.setGeometry(QtCore.QRect(290, 370, 61, 20))
        self.line_valor.setObjectName("line_valor")
        self.line_entrega = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entrega.setGeometry(QtCore.QRect(360, 370, 41, 20))
        self.line_entrega.setObjectName("line_entrega")
        self.line_qnt_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_qnt_2.setGeometry(QtCore.QRect(30, 400, 41, 20))
        self.line_qnt_2.setObjectName("line_qnt_2")
        self.line_descricao_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_descricao_2.setGeometry(QtCore.QRect(80, 400, 151, 20))
        self.line_descricao_2.setObjectName("line_descricao_2")
        self.line_unidade_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_unidade_2.setGeometry(QtCore.QRect(240, 400, 41, 20))
        self.line_unidade_2.setObjectName("line_unidade_2")
        self.line_valor2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_valor2.setGeometry(QtCore.QRect(290, 400, 61, 20))
        self.line_valor2.setObjectName("line_valor2")
        self.line_entrega2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entrega2.setGeometry(QtCore.QRect(360, 400, 41, 20))
        self.line_entrega2.setObjectName("line_entrega2")
        self.line_qnt_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_qnt_3.setGeometry(QtCore.QRect(30, 430, 41, 20))
        self.line_qnt_3.setObjectName("line_qnt_3")
        self.line_descricao_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_descricao_3.setGeometry(QtCore.QRect(80, 430, 151, 20))
        self.line_descricao_3.setObjectName("line_descricao_3")
        self.line_unidade_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_unidade_3.setGeometry(QtCore.QRect(240, 430, 41, 20))
        self.line_unidade_3.setObjectName("line_unidade_3")
        self.line_valor_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_valor_3.setGeometry(QtCore.QRect(290, 430, 61, 20))
        self.line_valor_3.setObjectName("line_valor_3")
        self.line_entrega_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entrega_3.setGeometry(QtCore.QRect(360, 430, 41, 20))
        self.line_entrega_3.setObjectName("line_entrega_3")
        self.line_qnt_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_qnt_4.setGeometry(QtCore.QRect(30, 460, 41, 20))
        self.line_qnt_4.setObjectName("line_qnt_4")
        self.line_descricao_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_descricao_4.setGeometry(QtCore.QRect(80, 460, 151, 20))
        self.line_descricao_4.setObjectName("line_descricao_4")
        self.line_unidade_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_unidade_4.setGeometry(QtCore.QRect(240, 460, 41, 20))
        self.line_unidade_4.setObjectName("line_unidade_4")
        self.line_valor_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_valor_4.setGeometry(QtCore.QRect(290, 460, 61, 20))
        self.line_valor_4.setObjectName("line_valor_4")
        self.line_entrega_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entrega_4.setGeometry(QtCore.QRect(360, 460, 41, 20))
        self.line_entrega_4.setObjectName("line_entrega_4")
        self.line_qnt_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_qnt_5.setGeometry(QtCore.QRect(30, 490, 41, 20))
        self.line_qnt_5.setObjectName("line_qnt_5")
        self.line_descricao_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_descricao_5.setGeometry(QtCore.QRect(80, 490, 151, 20))
        self.line_descricao_5.setObjectName("line_descricao_5")
        self.line_unidade_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_unidade_5.setGeometry(QtCore.QRect(240, 490, 41, 20))
        self.line_unidade_5.setObjectName("line_unidade_5")
        self.line_valor_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_valor_5.setGeometry(QtCore.QRect(290, 490, 61, 20))
        self.line_valor_5.setObjectName("line_valor_5")
        self.line_entrega_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entrega_6.setGeometry(QtCore.QRect(361, 490, 41, 20))
        self.line_entrega_6.setObjectName("line_entrega_6")
        self.informacoes_1 = QtWidgets.QLabel(self.centralwidget)
        self.informacoes_1.setGeometry(QtCore.QRect(10, 680, 401, 41))
        self.informacoes_1.setObjectName("informacoes_1")
        self.informacoes_2 = QtWidgets.QLabel(self.centralwidget)
        self.informacoes_2.setGeometry(QtCore.QRect(10, 700, 401, 31))
        self.informacoes_2.setObjectName("informacoes_2")
        self.line_qnt_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_qnt_6.setGeometry(QtCore.QRect(30, 520, 41, 20))
        self.line_qnt_6.setObjectName("line_qnt_6")
        self.line_descricao_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_descricao_6.setGeometry(QtCore.QRect(80, 520, 151, 20))
        self.line_descricao_6.setObjectName("line_descricao_6")
        self.label_valor_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_valor_2.setGeometry(QtCore.QRect(360, 350, 40, 16))
        self.label_valor_2.setObjectName("label_valor_2")
        self.line_unidade_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_unidade_6.setGeometry(QtCore.QRect(240, 520, 41, 20))
        self.line_unidade_6.setObjectName("line_unidade_6")
        self.line_valor_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_valor_9.setGeometry(QtCore.QRect(290, 520, 61, 20))
        self.line_valor_9.setObjectName("line_valor_9")
        self.line_entrega_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_entrega_5.setGeometry(QtCore.QRect(360, 520, 41, 20))
        self.line_entrega_5.setObjectName("line_entrega_5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(260, 550, 141, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_valortotal = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_valortotal.setObjectName("label_valortotal")
        self.horizontalLayout_5.addWidget(self.label_valortotal)
        self.line_valor_total = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.line_valor_total.setObjectName("line_valor_total")
        self.horizontalLayout_5.addWidget(self.line_valor_total)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(140, 590, 148, 72))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_imprimir = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_imprimir.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_imprimir.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_imprimir.setFont(font)
        self.btn_imprimir.setAutoFillBackground(False)
        self.btn_imprimir.setStyleSheet("")
        self.btn_imprimir.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:/programação/cartucho/imagens/imprimir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_imprimir.setIcon(icon1)
        self.btn_imprimir.setIconSize(QtCore.QSize(60, 60))
        self.btn_imprimir.setObjectName("btn_imprimir")
        self.horizontalLayout_4.addWidget(self.btn_imprimir)
        self.btn_cancelar = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_cancelar.setMinimumSize(QtCore.QSize(70, 70))
        self.btn_cancelar.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:/programação/cartucho/imagens/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancelar.setIcon(icon2)
        self.btn_cancelar.setIconSize(QtCore.QSize(50, 50))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_4.addWidget(self.btn_cancelar)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 170, 101, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_name_2 = QtWidgets.QLabel(self.widget)
        self.label_name_2.setObjectName("label_name_2")
        self.horizontalLayout_6.addWidget(self.label_name_2)
        self.line_data = QtWidgets.QLineEdit(self.widget)
        self.line_data.setObjectName("line_data")
        self.horizontalLayout_6.addWidget(self.line_data)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emissor de Pedidos de Cartuchos"))
        self.informacoes.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Quintino Bocaiuva 160 </span></p></body></html>"))
        self.label_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">  Nome  </span></p></body></html>"))
        self.label_telefone.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Telefone</span></p></body></html>"))
        self.label_endereco.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Endereço</span></p></body></html>"))
        self.label_qnt.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Qnt</span></p></body></html>"))
        self.label_descricao.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Descriçao</span></p></body></html>"))
        self.label_unidade.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">V.Uni</span></p></body></html>"))
        self.label_valor.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Valor</span></p></body></html>"))
        self.informacoes_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">049 3567-3350</span></p></body></html>"))
        self.informacoes_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Caçador-SC </span></p></body></html>"))
        self.label_valor_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ent</span></p></body></html>"))
        self.label_valortotal.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Valor Total</span></p></body></html>"))
        self.label_name_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Data</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
