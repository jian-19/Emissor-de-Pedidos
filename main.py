
import sys
from layout1 import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtGui import QPixmap

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_cancelar.clicked.connect(self.cancelar)
    def somar(self):
        quantidade = 0
        if self.line_qnt.text() == 1:
            quantidade = quantidade+1
        if self.line_qnt.text() == 2:
            quantidade = quantidade+2
        if self.line_qnt.text() == 3:
            quantidade = quantidade+3
        if self.line_qnt.text() == 4:
            quantidade = quantidade+4
        if self.line_qnt.text() == 5:
            quantidade = quantidade+5
        if self.line_qnt.text() == 6:
            quantidade = quantidade+6
        if self.line_qnt.text() == 7:
            quantidade = quantidade+7
        if self.line_qnt.text() == 8:
            quantidade = quantidade+8
        if self.line_qnt.text() == 9:
            quantidade = quantidade+9
        if self.line_qnt.text() == 10:
            quantidade = quantidade+10
    def imprimir(self):
        pedido = "pedido"+str(self.input_name.text())
        pedido = pedido+".txt"
        arq = open(pedido,"w")
        arq.write("----Inffo Informatica----")
        arq.write("\nRua: Quintino Bocaiuva, 160")
        arq.write("\nCNPJ:")
        arq.write("\n-----------------------\n\n")
        arq.write("<<<<Dados do Pedido>>>>\n\n")
        arq.write("\nData: "+str(self.line_data.text()))
        #arq.write("\nPedido: "+str(entry_pedido.get()))
        arq.write("\nCliente: "+str(self.input_name.text()))
        arq.write("\nTelefone: "+str(self.input_telefone.text()))
        arq.write("\nEndereço: "+str(self.input_endereco.text()))
        arq.write("\nDescrição: "+str(self.line_descricao.text()))
        arq.write("\nQuantidade: "+str(self.line_qnt.text()))
        arq.write("\nValor da Recarga: "+str(self.line_valor.text())+" R$")
        arq.write("\nValor da Entrega: "+str(self.line_entrega.text())+" R$")
        arq.write("\nValor Total: "+str(n10))
        arq.write("\n\n\n______________________________")
        arq.write("\n          Assinatura")
        arq.write("\n\n \n\n")
        arq.close()

        n1 = self.line_data.text()
        n2 = self.input_name.text()
        n3 = self.input_telefone.text()
        n4 = self.input_endereco.text()
        n5 = self.line_descricao.text()
        n6 = self.line_qnt.text()
        n7 = self.line_valor.text()
        n8 = self.line_entrega.text()
        n9 = self.line_qnt.text()
        n10 = self.somar
        #n11 = n10()

        imprimir(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

        prt = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(prt)

        if dialog.exec_( ) == QPrintDialog.Accepted:
            self.edt.print_(prt)
        
        pt = QPrinter(QPrinter.HighResolution)
        prev = QPrintPreviewDialog(pt, self)
        prev.paintRequested.connect(self.preview)
        prev.exec_( )

    def print(self):
        prt = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(prt)

        if dialog.exec_( ) == QPrintDialog.Accepted:
            self.edt.print_(prt)

    def view(self):
        pt = QPrinter(QPrinter.HighResolution)
        prev = QPrintPreviewDialog(pt, self)
        prev.paintRequested.connect(self.preview)
        prev.exec_( )

    def preview(self, pt):
        self.edt.print_(pt)
    def cancelar(self):
        pass    
   

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()