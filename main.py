import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox
from Validator import INN
from Validator import OGRN
f = open("file.txt", 'a')


class MAINWINDOW(QWidget):
    def __init__(self):
        super().__init__()
        self.initgui()
        self.button.clicked.connect(self.check)

    def initgui(self):
        self.button = QPushButton('Проверить')
        self.leinn = QLineEdit()
        self.leogrn = QLineEdit()
        self.cname = QLineEdit()
        self.cname.setPlaceholderText('ООП "DOCValidator"')
        self.leogrn.setInputMask('x' * 13)
        self.leogrn.setPlaceholderText("13-ти значный ОГРН")
        self.leinn.setInputMask('x' * 10)
        self.leinn.setPlaceholderText("10-ти значный ИНН")
        labelcname = QLabel('  Название\nорганизации')
        labelogrn = QLabel('ОГРН')
        labelinn = QLabel('ИНН')
        cnamehbox = QHBoxLayout()
        cnamehbox.addWidget(labelcname)
        cnamehbox.addWidget(self.cname)
        ogrnhbox = QHBoxLayout()
        ogrnhbox.addWidget(labelogrn)
        ogrnhbox.addWidget(self.leogrn)
        innhbox = QHBoxLayout()
        innhbox.addWidget(labelinn)
        innhbox.addWidget(self.leinn)
        buttonhbox = QHBoxLayout()
        buttonhbox.addWidget(self.button)
        vboxlayout = QVBoxLayout()
        vboxlayout.addLayout(cnamehbox)
        vboxlayout.addLayout(innhbox)
        vboxlayout.addLayout(ogrnhbox)
        vboxlayout.addLayout(buttonhbox)
        self.setLayout(vboxlayout)

    def check(self):
        cname = self.cname.text()
        inn = self.leinn.text()
        ok_inn = INN.is_valid(inn)
        ogrn = self.leogrn.text()
        ok_ogrn = OGRN.is_valid(ogrn)
        if ok_inn and ok_ogrn:
            QMessageBox.information(self, 'Результат', 'Валидация пройдена!\nВсе данные введены в документ>', QMessageBox.Ok)
            f.write('\n•••' + cname + '|ИНН: ' + inn + '|ОГРН: ' + ogrn + '|•••')
            f.close()
        elif not ok_inn and not ok_ogrn:
            QMessageBox.information(self, 'Результат', 'Валидация не пройдена!\nДанные ОГРН и ИНН не существуют',
                                    QMessageBox.Ok)
        elif ok_inn:
            QMessageBox.information(self, 'Результат', 'Валидация не пройдена!\nДанный ОГРН не существует',
                                    QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Результат', 'Валидация не пройдена!\nДанный ИНН не существует',
                                    QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MAINWINDOW()
    w.resize(400, 150)
    w.move(300, 300)
    w.setWindowTitle('DOCVALIDATOR')
    w.show()
    sys.exit(app.exec_())
