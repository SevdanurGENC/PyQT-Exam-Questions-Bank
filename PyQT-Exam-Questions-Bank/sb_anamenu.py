import sys, os, xlrd, xlwt
from PyQt5 import QtWidgets, QtPrintSupport, QtGui
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.QtWidgets import * 
from Ui_SB_AnaMenu import Ui_SB_AnaMenu
from Ui_SB_YeniSoruEkle import Ui_SB_YeniSoruEkle
from Ui_SB_SoruSec import Ui_SB_SoruSec  


class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_SB_AnaMenu()
        self.ui.setupUi(self)

        self.ui.actionYeni_Soru_Ekle.triggered.connect(self.YeniSoruEklePenceresiniCagir)
        self.ui.actionSoru_Sec.triggered.connect(self.SoruSecPenceresiniCagir) 
 
    def YeniSoruEklePenceresiniCagir(self): 
        self.yeniSoruEkle = YeniSoruEkle()
        self.yeniSoruEkle.show() 

    def SoruSecPenceresiniCagir(self): 
        self.soruSec = SoruSec()
        self.soruSec.show()  

class YeniSoruEkle(QtWidgets.QMainWindow):

    def __init__(self):
        super(YeniSoruEkle, self).__init__()
        self.yeniSoruEkle = Ui_SB_YeniSoruEkle()
        self.yeniSoruEkle.setupUi(self)

        self.yeniSoruEkle.tableWidget.setColumnCount(7)  
        self.yeniSoruEkle.tableWidget.setHorizontalHeaderLabels(['Soru', '1. Secenek', '2. Secenek', '3. Secenek', '4. Secenek', '5. Secenek', 'Cevap'])

        self.yeniSoruEkle.pushButton.clicked.connect(self.SorulariListeyeAktar)
        self.yeniSoruEkle.pushButton_2.clicked.connect(self.SoruBankasinaKaydet)

    def SorulariListeyeAktar(self):
 
        SoruyuAl = self.yeniSoruEkle.textEdit.toPlainText()
        birinciSecenek = self.yeniSoruEkle.lineEdit.text()
        ikinciSecenek = self.yeniSoruEkle.lineEdit_2.text()
        ucuncuSecenek = self.yeniSoruEkle.lineEdit_3.text()
        dorduncuSecenek = self.yeniSoruEkle.lineEdit_4.text()
        besinciSecenek = self.yeniSoruEkle.lineEdit_5.text()

        dogruSecenekRB = ''
        dogruSecenek = ''
        birinciRB = self.yeniSoruEkle.radioButton.isChecked()
        ikinciRB = self.yeniSoruEkle.radioButton_2.isChecked()
        ucuncuRB = self.yeniSoruEkle.radioButton_3.isChecked()
        dorduncuRB = self.yeniSoruEkle.radioButton_4.isChecked()
        besinciRB = self.yeniSoruEkle.radioButton_5.isChecked() 

        if birinciRB == True:   
            dogruSecenekRB = 'A'
            dogruSecenek = birinciSecenek
        if ikinciRB == True:   
            dogruSecenekRB = 'B'
            dogruSecenek = ikinciSecenek
        if ucuncuRB == True:   
            dogruSecenekRB = 'C'
            dogruSecenek = ucuncuSecenek
        if dorduncuRB == True:   
            dogruSecenekRB = 'D'
            dogruSecenek = dorduncuSecenek
        if besinciRB == True:   
            dogruSecenekRB = 'E'
            dogruSecenek = besinciSecenek  

        lastrow = self.yeniSoruEkle.tableWidget.rowCount()
        self.yeniSoruEkle.tableWidget.insertRow(lastrow) 

        self.yeniSoruEkle.tableWidget.setItem(lastrow,0, QTableWidgetItem(SoruyuAl))  #Soru
        self.yeniSoruEkle.tableWidget.setItem(lastrow,1, QTableWidgetItem(birinciSecenek))  #BirinciSecenek
        self.yeniSoruEkle.tableWidget.setItem(lastrow,2, QTableWidgetItem(ikinciSecenek))   #IkinciSecenek
        self.yeniSoruEkle.tableWidget.setItem(lastrow,3, QTableWidgetItem(ucuncuSecenek))    #UcuncuSecenek
        self.yeniSoruEkle.tableWidget.setItem(lastrow,4, QTableWidgetItem(dorduncuSecenek))   #DorduncuSecenek
        self.yeniSoruEkle.tableWidget.setItem(lastrow,5, QTableWidgetItem(besinciSecenek))   #BesinciSecenek
        self.yeniSoruEkle.tableWidget.setItem(lastrow,6, QTableWidgetItem(dogruSecenekRB))   #DogruSecenekRB
 
 
    def SoruBankasinaKaydet(self):
        self.ExcelDosyaKaydet()
        nb_row = self.yeniSoruEkle.tableWidget.rowCount()
        nb_col = self.yeniSoruEkle.tableWidget.columnCount()

        for row in range (nb_row):
            for col in range(nb_col):
                print(row, col, self.yeniSoruEkle.tableWidget.item(row, col).text()) 

    def ExcelDosyaKaydet(self):
        global path_openfile_name 
        Name = QFileDialog.getSaveFileName(self, "Save file", "./", "xls(*.xls)") 
        path_openfile_name = Name[0] 
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet")
        self.SayfayiExceleEkle(sheet)
        wbk.save(Name[0])

    def SayfayiExceleEkle(self, sheet):
        horizontalHeader = ['Soru', '1. Secenek', '2. Secenek', '3. Secenek', '4. Secenek', '5. Secenek', 'Cevap']
        for currentColumn in range(7):
            sheet.write(0, currentColumn, horizontalHeader[currentColumn])

        for currentRow in range(self.yeniSoruEkle.tableWidget.rowCount()):
            for currentColumn in range(self.yeniSoruEkle.tableWidget.columnCount()):
                listdata = str(self.yeniSoruEkle.tableWidget.item(currentRow, currentColumn).text())
                sheet.write(currentRow + 1, currentColumn, listdata)  
 
class SoruSec(QtWidgets.QMainWindow):

    def __init__(self):
        super(SoruSec, self).__init__()
        self.soruSec = Ui_SB_SoruSec()
        self.soruSec.setupUi(self) 
        
        self.soruSec.tableWidget.setColumnCount(7)  
        self.soruSec.tableWidget.setHorizontalHeaderLabels(['Soru', '1. Secenek', '2. Secenek', '3. Secenek', '4. Secenek', '5. Secenek', 'Cevap'])
   
        self.soruSec.pushButton_2.clicked.connect(self.ExcelDosyaAc)  
        self.soruSec.tableWidget.cellClicked.connect(self.seciliOlaniYazdir)
        self.soruSec.pushButton.clicked.connect(self.pdfOnizlemeAl) 
 
    def ExcelDosyaAc(self):    
        excel_file, _ = QFileDialog.getOpenFileName(self, "Select Excel file to import","","Excel (*.xls *.xlsx)") 
        
        workbook = xlrd.open_workbook(excel_file)
        worksheet = workbook.sheet_by_name("sheet")
        worksheet = workbook.sheet_by_index(0)

        total_rows = worksheet.nrows
        total_column = worksheet.ncols  

        for x in range(1,total_rows):            
            lastrow = self.soruSec.tableWidget.rowCount()
            self.soruSec.tableWidget.insertRow(lastrow)
            for y in range(total_column):
                self.soruSec.tableWidget.setItem(lastrow, y, QTableWidgetItem(worksheet.cell(x,y).value) ) 
 
    def seciliOlaniYazdir(self):  
        liste = []
        for i in range(7):
            liste.append(self.soruSec.tableWidget.item(self.soruSec.tableWidget.currentRow(), i).text())  
        print(liste)  

    def pdfOnizlemeAl(self):  
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.pdfYazdirmaIslemi)
        dialog.exec_()
        self.pdfYazdirEkrani()
    
    def pdfYazdirEkrani(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.pdfYazdirmaIslemi(dialog.printer())

    def pdfYazdirmaIslemi(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        table = cursor.insertTable(
            self.soruSec.tableWidget.rowCount(), self.soruSec.tableWidget.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.soruSec.tableWidget.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer) 

def app():
    app = QtWidgets.QApplication(sys.argv) 
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()



