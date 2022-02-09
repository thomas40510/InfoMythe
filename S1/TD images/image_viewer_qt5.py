#!/usr/bin/python3

"""IHM de visualisation d'images.

.. codeauthor:: R. Moitié, S. Moyne pour le passage à Qt5
"""

import sys
import numpy as np

from PyQt5 import QtGui, QtCore, QtWidgets

import image_process
import image_process_opt

import cProfile
import pstats


class ImageViewer(QtWidgets.QMainWindow):
    """Classe principale : crée la fenêtre.
    """

    def __init__(self):
        super(ImageViewer, self).__init__()
        self.pixmap = None
        self.initial_pixmap = None
        self.init_ui()

    def init_ui(self):
        """Construction de la fenêtre.
        """
        self.resize(640, 480)
        self.setWindowTitle(u"Exemples d'utilisation d'images")
        self.image_1 = 'lena.jpg'

        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.vertical_layout = QtWidgets.QVBoxLayout()

        # QLabel
        self.label = QtWidgets.QLabel(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                            QtWidgets.QSizePolicy.Preferred)
        self.label.setSizePolicy(size_policy)
        self.pixmap = QtGui.QPixmap(self.image_1)
        self.initial_pixmap = self.pixmap.copy()

        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.vertical_layout.addWidget(self.label)
        self.horizontal_layout.addLayout(self.vertical_layout)

        self.setCentralWidget(self.centralwidget)

        # Menu
        exit_action = QtWidgets.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        open_action = QtWidgets.QAction(QtGui.QIcon('open.png'), '&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open image')
        open_action.triggered.connect(self.open_image)

        self.opt_action = QtWidgets.QAction('Enable', self, checkable=True)
        self.opt_action.setStatusTip('Enable optimization')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)
        filter_menu = menubar.addMenu('&Tools')

        init_action = QtWidgets.QAction('init', self)
        init_action.triggered.connect(self.init_image)
        filter_menu.addAction(init_action)

        opt_menu = menubar.addMenu('&Optimization')
        opt_menu.addAction(self.opt_action)

        self.mapper = QtCore.QSignalMapper(self)
        for item in ['copy', 'negative', 'h_flip', 'v_flip', 'red', 'green',
                     'blue', 'rotate_colors', 'blur', 'zoom', 'black_and_white',
                     'edge', 'contrast']:
            action = QtWidgets.QAction(item, self)
            self.mapper.setMapping(action, item)
            action.triggered.connect(self.mapper.map)
            filter_menu.addAction(action)
        self.mapper.mapped['QString'].connect(self.generic_filter)

    def open_image(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        self.pixmap = QtGui.QPixmap(fname[0])
        self.initial_pixmap = self.pixmap.copy()
        self.label.setPixmap(QtGui.QPixmap(self.pixmap))
        self.label.setGeometry(self.pixmap.rect())
        self.centralwidget.setGeometry(self.pixmap.rect())

    def init_image(self):
        self.pixmap = self.initial_pixmap
        self.label.setPixmap(QtGui.QPixmap(self.pixmap))

    def generic_prof_filter(self, item):
        cProfile.runctx(
            "self.generic_filter(item)", globals(), locals(), "Profile.prof")
        s = pstats.Stats("Profile.prof")
        s.strip_dirs().sort_stats("time").print_stats()

    def generic_filter(self, operation):
        """Applique la fonction operation à l'image.

        Parameters
        ----------
        operation : fonction
            Fonction à appliquer.
        """
        # transforme un pixmap en image
        qi = self.pixmap.toImage()
        # create the object
        img = self.image_to_array(qi)

        # appelle la fonction de calcul
        if self.opt_action.isChecked():
            new_img = eval('image_process_opt.{0}(img)'.format(operation))
        else:
            new_img = eval('image_process.{0}(img)'.format(operation))
        new_img[:, :, 3] = 255  # alpha layer
        qi2 = self.array_to_image(new_img)

        # mise à jour du pixmap
        self.pixmap = self.pixmap.fromImage(qi2)
        self.label.setPixmap(QtGui.QPixmap(self.pixmap))

    def image_to_array(self, image):
        """Conversion d'une image en numpy array.

        Parameters
        ----------
        img : QImage
            Image source.

        Returns
        -------
        numpy.array
        """
        ptr = image.constBits()
        ptr.setsize(image.byteCount())
        return np.array(ptr, dtype=np.uint8).reshape(image.height(),
                                                     image.width(), 4)

    def array_to_image(self, arr):
        """Conversion d'un nupy array en image.

        Parameters
        ----------
        arr : numpy.array
            Image source.

        Returns
        -------
        img : QImage
        """
        img = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0],
                           QtGui.QImage.Format_ARGB32)
        return img


if __name__ == "__main__":
    # Pour une exécution sous la console IPython
    # ajouter le test suivant en décommentant
    # les 3 lignes suivantes
    # APP = QtCore.QCoreApplication.instance()
    # if APP is None:
    #    APP = QtWidgets.QApplication(sys.argv)
    APP = QtWidgets.QApplication(sys.argv)
    UI = ImageViewer()
    UI.show()
    sys.exit(APP.exec_())
