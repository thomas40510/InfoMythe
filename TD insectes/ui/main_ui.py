import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic

from ecosystem_ui import *
from ecosys import *
from animals import *


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # load UI
        self.ui = Ui_ecosystem()
        self.ui.setupUi(self)
        self.ui.btn_step.clicked.connect(self.step_simu)
        self.ui.btn_gen.clicked.connect(self.gen_simu)
        self.ui.btn_simu.clicked.connect(self.full_simu)
        self.timer = QtCore.QTimer()

        # draws background of UI sim board
        pixmap = QtGui.QPixmap('img/bg2.png')
        pal = QtGui.QPalette()
        pal.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))

        self.ui.wdgt_main.stackUnder(self)
        self.ui.wdgt_main.setAutoFillBackground(True)
        self.ui.wdgt_main.setPalette(pal)

        self.ui.wdgt_main.paintEvent = self.drawEcosys

        # init vars
        self.painter = QtGui.QPainter()
        self._ecosystem = None

        self.gen_simu()

    def paintEvent(self, e):
        qp = self.painter
        qp = QtGui.QPainter()
        qp.begin(self.ui.wdgt_main)
        self.drawEcosys(qp)
        qp.end()

    def drawEcosys(self, qp):
        qp = self.painter
        qp.begin(self.ui.wdgt_main)
        for ins in self._ecosystem:
            if ins.car() == 'F':
                qp.setPen(QtGui.QColor('green'))
                qp.drawText(ins.x, ins.y, "🐜")
                # qp.drawRect(ins.x, ins.y, 10, 5)
            else:
                qp.setPen(QtGui.QColor('red'))
                qp.drawText(ins.x, ins.y, "🦗")
                # qp.drawEllipse(ins.x, ins.y, 10, 5)
        qp.end()
        self.ui.wdgt_main.update()

    def step_simu(self):
        if self._ecosystem.nbtour > 0:
            self._ecosystem.unTour()
            # print(self._ecosystem)
            self._ecosystem.nbtour -= 1
            print(f'[i]: current step is {self._ecosystem.nbtour}')
            print(f'current timer is {self.timer.isActive()}')
        else:
            print('[i]: No steps remaining in current simulation.')
            self.timer.stop()
        self.drawEcosys(self.painter)
        self.ui.btn_step.setText(f"Step ({self._ecosystem.nbtour})")
        self.ui.wdgt_main.update()

    def gen_simu(self):
        w, h = self.ui.wdgt_main.width(), self.ui.wdgt_main.height()
        eco = Ecosystem(nbins=60, nbsim=150, width=w, height=h, nbNour=w//20)
        self._ecosystem = eco
        self.drawEcosys(self.painter)
        self.ui.wdgt_main.update()

    def full_simu(self):
        self.timer.startTimer(300)
        self.timer.timeout.connect(self.step_simu)

        while self._ecosystem.nbtour > 0:
            self.step_simu()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
