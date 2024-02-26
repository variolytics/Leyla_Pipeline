import sys
import csv
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QFileDialog,
    QAction,
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd


class ScatterPlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Scatter Plot")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.plot_button = QPushButton("Plot Scatter")
        self.plot_button.clicked.connect(self.plot_scatter)
        self.layout.addWidget(self.plot_button)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Add a toolbar for zoom, pan, and home
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout.addWidget(self.toolbar)

        # Add keyboard shortcuts for zoom and pan
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.triggered.connect(self.zoom_in)
        self.addAction(zoom_in_action)
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.triggered.connect(self.zoom_out)
        self.addAction(zoom_out_action)
        pan_action = QAction("Pan", self)
        pan_action.triggered.connect(self.pan)
        self.addAction(pan_action)
        home_action = QAction("Home", self)
        home_action.triggered.connect(self.home)
        self.addAction(home_action)

        # Set keyboard shortcuts
        zoom_in_action.setShortcut(Qt.CTRL + Qt.Key_Plus)
        zoom_out_action.setShortcut(Qt.CTRL + Qt.Key_Minus)
        pan_action.setShortcut(Qt.CTRL + Qt.Key_P)
        home_action.setShortcut(Qt.CTRL + Qt.Key_H)

    def zoom_in(self):
        self.toolbar.zoom()

    def zoom_out(self):
        self.toolbar.zoom(-1)

    def pan(self):
        self.toolbar.pan()

    def home(self):
        self.toolbar.home()

    def plot_scatter(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("CSV files (*.csv)")
        file_dialog.setViewMode(QFileDialog.Detail)
        filename, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV files (*.csv)")

        if filename:
            cols = ['Time', '2.0', '12.0', '8.0', '13.0', '15.0', '19.0', '22.0', '29.0', '30.0', '32.0', '34.0', '40.0', '84.0']
            data = pd.read_csv(filename, sep=';', decimal=',', usecols=cols)
            if data.empty:
                print("Error: Empty DataFrame")
                return
            
            data.set_index('Time', inplace=True)
            data.reset_index(inplace=True)

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.scatter(data.index, data["15.0"])
            ax.set_xlabel("Index")
            ax.set_ylabel("15.0")
            self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScatterPlotWindow()
    window.show()
    sys.exit(app.exec_())
