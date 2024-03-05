import sys

from PyQt5 import QtCore, QtGui, QtWidgets
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
from PyQt5.QtGui import QIcon

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar



class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName("winMain")
        winMain.resize(928, 722)
        winMain.setFixedSize(winMain.size()) 
        self.centralwidget = QtWidgets.QWidget(winMain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tbwMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tbwMain.setEnabled(True)
        self.tbwMain.setIconSize(QtCore.QSize(50, 50))
        self.tbwMain.setObjectName("tbwMain")
        self.wDataScreening = QtWidgets.QWidget()
        self.wDataScreening.setEnabled(True)
        self.wDataScreening.setObjectName("wDataScreening")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.wDataScreening)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.wDataScreening)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 884, 574))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(711, 500, 171, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ScreeningFile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ScreeningFile.setObjectName("ScreeningFile")
        self.horizontalLayout_3.addWidget(self.ScreeningFile)
        # Increase the font and button size of the ScreeningFile button
        button_font = QtGui.QFont()
        button_font.setPointSize(12)  # Adjust the font size as needed
        button_font.setBold(True)  # Make the font bold
        self.ScreeningFile.setFont(button_font)

        # Set size policy for the button
        self.ScreeningFile.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed
        )
        # Increase the size of the push button
        self.ScreeningFile.setFixedSize(150, 40)  # Adjust the width and height as needed
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 871, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Plot_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Plot_label.setObjectName("Plot_label")
        self.verticalLayout_4.addWidget(self.Plot_label)
        # Set font size for the "Data Preview" label
        font = QtGui.QFont()
        font.setPointSize(12)  # Adjust the font size as needed
        font.setBold(True)  # Make the font bold
        self.Plot_label.setFont(font)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.gridLayout_8.addLayout(self.verticalLayout_2, 0, 0, 1, 2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_engineering.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wDataScreening, icon, "")
        
        self.wFiltering = QtWidgets.QWidget()
        self.wFiltering.setEnabled(True)
        self.wFiltering.setObjectName("wFiltering")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wFiltering)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 891, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        # Add a label above the QListWidget
        self.labelAboveListWidget = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelAboveListWidget.setObjectName("labelAboveListWidget")
        self.labelAboveListWidget.setText("Selected Files:")
        # Set font size for the label (adjust as needed)
        label_font = QtGui.QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        self.labelAboveListWidget.setFont(label_font)

        # Set size policy for the label
        self.labelAboveListWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )

        self.verticalLayout.addWidget(self.labelAboveListWidget)
       
        self.SelectedFile_listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.SelectedFile_listWidget.setObjectName("listWidget")
        # Set size policy for the QListWidget
        self.SelectedFile_listWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addWidget(self.SelectedFile_listWidget)
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.seletFile_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.seletFile_label.setObjectName("seletFile_label")
        self.horizontalLayout.addWidget(self.seletFile_label)
        seletFile_label_font = QtGui.QFont()
        seletFile_label_font.setPointSize(12)
        seletFile_label_font.setBold(True)
        self.seletFile_label.setFont(seletFile_label_font)

        # Set size policy for the label
        self.seletFile_label.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )
        self.addButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addButton.setEnabled(True)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        addButton_font = QtGui.QFont()
        addButton_font.setPointSize(12)
        addButton_font.setBold(True)
        self.addButton.setFont(addButton_font)

        # Set size policy for the label
        self.addButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )
        self.removeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        removeButton_font = QtGui.QFont()
        removeButton_font.setPointSize(12)
        removeButton_font.setBold(True)
        self.removeButton.setFont(removeButton_font)

        # Set size policy for the label
        self.removeButton.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        
        # Add a label above the second QListWidget
        self.labelAboveListWidget2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelAboveListWidget2.setObjectName("labelAboveListWidget2")
        self.labelAboveListWidget2.setText("Filtered Files:")
        # Set font size for the label (adjust as needed)
        label_font = QtGui.QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        self.labelAboveListWidget2.setFont(label_font)

        # Set size policy for the label
        self.labelAboveListWidget2.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Fixed
        )

        self.verticalLayout.addWidget(self.labelAboveListWidget2)
       
        # Add a second QListWidget for filtered files
        self.FilteredFile_listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.FilteredFile_listWidget.setObjectName("FilteredFile_listWidget")
        # Set size policy for the second QListWidget
        self.FilteredFile_listWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addWidget(self.FilteredFile_listWidget)
        
        # Create a horizontal layout for the Filter button
        self.horizontalLayoutFilter = QtWidgets.QHBoxLayout()
        self.horizontalLayoutFilter.setObjectName("horizontalLayoutFilter")
        spacerItemFilter = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutFilter.addItem(spacerItemFilter)
        
        # Add the Filter button to the horizontal layout
        self.filterButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.filterButton.setObjectName("filterButton")
        self.filterButton.setText("Filter")
        filterButton_font = QtGui.QFont()
        filterButton_font.setPointSize(12)
        filterButton_font.setBold(True)
        self.filterButton.setFont(filterButton_font)
        
        # Set size policy for the Filter button
        self.filterButton.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed,  # Use Fixed size policy to prevent expanding
            QtWidgets.QSizePolicy.Fixed
        )
        
        # Add the Filter button to the horizontal layout
        self.horizontalLayoutFilter.addWidget(self.filterButton)
        
        # Add the horizontal layout to the main vertical layout
        self.verticalLayout.addLayout(self.horizontalLayoutFilter)
        
        
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_diagnosis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wFiltering, icon1, "")
        self.wSetting = QtWidgets.QWidget()
        self.wSetting.setObjectName("wSetting")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.wSetting)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 911, 561))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wSetting, icon2, "")
        self.wHelp = QtWidgets.QWidget()
        self.wHelp.setObjectName("wHelp")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.wHelp)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tbwHelp = QtWidgets.QTabWidget(self.wHelp)
        self.tbwHelp.setTabPosition(QtWidgets.QTabWidget.South)
        self.tbwHelp.setObjectName("tbwHelp")
        self.wVideo = QtWidgets.QWidget()
        self.wVideo.setObjectName("wVideo")
        self.tbwHelp.addTab(self.wVideo, "")
        self.wManual = QtWidgets.QWidget()
        self.wManual.setObjectName("wManual")
        self.tbwHelp.addTab(self.wManual, "")
        self.gridLayout_6.addWidget(self.tbwHelp, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mainTab/icons/main_help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbwMain.addTab(self.wHelp, icon3, "")
        self.gridLayout.addWidget(self.tbwMain, 0, 1, 1, 1)
        winMain.setCentralWidget(self.centralwidget)
        self.mbMain = QtWidgets.QMenuBar(winMain)
        self.mbMain.setGeometry(QtCore.QRect(0, 0, 928, 22))
        self.mbMain.setObjectName("mbMain")
        winMain.setMenuBar(self.mbMain)
        self.stbStatusbar = QtWidgets.QStatusBar(winMain)
        self.stbStatusbar.setObjectName("stbStatusbar")
        winMain.setStatusBar(self.stbStatusbar)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # Increase the size of the canvas
        self.canvas.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_4.addWidget(self.canvas)
        # Add a toolbar for zoom, pan, and home
        self.toolbar = NavigationToolbar(self.canvas)
        self.verticalLayout_4.addWidget(self.toolbar)
        
        # Set font size and minimum width for the tabs
        tab_style = "QTabBar::tab { font-size: 11pt; min-width: 150px; }"
        self.tbwMain.setStyleSheet(tab_style)  
        
        self.retranslateUi(winMain)
        self.tbwMain.setCurrentIndex(0)
        self.tbwHelp.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        _translate = QtCore.QCoreApplication.translate
        winMain.setWindowTitle(_translate("winMain", "Preprocessing Tool"))
        # Create a bold font
        bold_font_Tab = QtGui.QFont()
        bold_font_Tab.setBold(True)
        self.ScreeningFile.setText(_translate("winMain", "Select File"))
        self.removeButton.setText(_translate("winMain", "Remove"))
        self.addButton.setText(_translate("winMain", "Add"))
        self.seletFile_label.setText(_translate("winMain","Add/Remove files:"))
        self.Plot_label.setText(_translate("winMain", "Data Preview:"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wDataScreening), _translate("winMain", "Screening"))
        self.tbwMain.setTabToolTip(self.tbwMain.indexOf(self.wDataScreening), _translate("winMain", "DataScreening"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wFiltering), _translate("winMain", "Filtering"))
        self.tbwMain.setTabToolTip(self.tbwMain.indexOf(self.wFiltering), _translate("winMain", "Filtering"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wSetting), _translate("winMain", "Setting"))
        self.tbwMain.setTabToolTip(self.tbwMain.indexOf(self.wSetting), _translate("winMain", "Setting"))
        self.tbwHelp.setTabText(self.tbwHelp.indexOf(self.wVideo), _translate("winMain", "Video"))
        self.tbwHelp.setTabText(self.tbwHelp.indexOf(self.wManual), _translate("winMain", "Manual"))
        self.tbwMain.setTabText(self.tbwMain.indexOf(self.wHelp), _translate("winMain", "Help"))
        self.tbwMain.tabBar().setFont(bold_font_Tab)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    winMain = QtWidgets.QMainWindow()
    ui = Ui_winMain()
    ui.setupUi(winMain)
    winMain.show()
    sys.exit(app.exec_())
