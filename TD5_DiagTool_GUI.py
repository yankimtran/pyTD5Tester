import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QGridLayout, QGroupBox
from PyQt5.QtCore import QTimer

SAMPLING_TIME = 2 #seconds

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.startTime = 0

        self.setWindowTitle("My TD5 Diagnostic Tool")
        #self.setGeometry(100, 100, 600, 400)


        self.mainLoop = QTimer()
        self.mainLoop.timeout.connect(self.mainLoopCallback)
        self.mainLoop.setInterval(SAMPLING_TIME*1000)

        # Création du widget de l'onglet principal
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs) #TODO: Que fait cette fonction?

        # Création des deux onglets
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Ajout des onglets au widget principal
        self.tabs.addTab(self.tab1, "Board Instruments")
        self.tabs.addTab(self.tab2, "Engine Faults")

        # Configuration des contenus des onglets
        self.setup_tab1()
        self.setup_tab2()

    def setup_tab1(self):
        layout = QGridLayout()
        ## Field 1
        Field_1_GridLayout = QGridLayout()
        Field_1_GridLayout.addWidget(QLabel("Field 1, champ 1"),0,0)
        Field_1_GridLayout.addWidget(QLabel("Field 1, champ 2"),1,0)

        Field_1= QGroupBox()
        Field_1.setTitle("Field 1")
        Field_1.setLayout(Field_1_GridLayout)

        ## Field 2
        Field_2_GridLayout = QGridLayout()
        Field_2_GridLayout.addWidget(QLabel("Field 2, champ 1"),0,0)
        Field_2_GridLayout.addWidget(QLabel("Field 2, champ 2"),1,0)

        Field_2= QGroupBox()
        Field_2.setTitle("Field 2")
        Field_2.setLayout(Field_2_GridLayout)

                ## Field 3
        Field_3_GridLayout = QGridLayout()
        Field_3_GridLayout.addWidget(QLabel("Field 3, champ 1"),0,0)
        Field_3_GridLayout.addWidget(QLabel("Field 3, champ 2"),1,0)

        Field_3= QGroupBox()
        Field_3.setTitle("Field 3")
        Field_3.setLayout(Field_3_GridLayout)

        ## Field 4
        Field_4_GridLayout = QGridLayout()
        Field_4_GridLayout.addWidget(QLabel("Field 4, champ 1"),0,0)
        Field_4_GridLayout.addWidget(QLabel("Field 4, champ 2"),1,0)

        Field_4= QGroupBox()
        Field_4.setTitle("Field 4")
        Field_4.setLayout(Field_4_GridLayout)

        ## Field 5
        Field_5_GridLayout = QGridLayout()
        Field_5_GridLayout.addWidget(QLabel("Field 5, champ 1"),0,0)
        Field_5_GridLayout.addWidget(QLabel("Field 5, champ 2"),1,0)

        Field_5= QGroupBox()
        Field_5.setTitle("Field 5")
        Field_5.setLayout(Field_5_GridLayout)

        ## Field 6
        Field_6_GridLayout = QGridLayout()
        Field_6_GridLayout.addWidget(QLabel("Field 6, champ 1"),0,0)
        Field_6_GridLayout.addWidget(QLabel("Field 6, champ 2"),1,0)

        Field_6= QGroupBox()
        Field_6.setTitle("Field 6")
        Field_6.setLayout(Field_6_GridLayout)

        ## Field 7
        Field_7_GridLayout = QGridLayout()
        Field_7_GridLayout.addWidget(QLabel("Field 7, champ 1"),0,0)
        Field_7_GridLayout.addWidget(QLabel("Field 7, champ 2"),1,0)

        Field_7= QGroupBox()
        Field_7.setTitle("Field 7")
        Field_7.setLayout(Field_7_GridLayout)

        ## Field 8
        Field_8_GridLayout = QGridLayout()
        Field_8_GridLayout.addWidget(QLabel("Field 8, champ 1"),0,0)
        Field_8_GridLayout.addWidget(QLabel("Field 8, champ 2"),1,0)

        Field_8= QGroupBox()
        Field_8.setTitle("Field 8")
        Field_8.setLayout(Field_8_GridLayout)

        ## Field 9
        Field_9_GridLayout = QGridLayout()
        Field_9_GridLayout.addWidget(QLabel("Field 9, champ 1"),0,0)
        Field_9_GridLayout.addWidget(QLabel("Field 9, champ 2"),1,0)

        Field_9= QGroupBox()
        Field_9.setTitle("Field 9")
        Field_9.setLayout(Field_9_GridLayout)
        
        layout.addWidget(Field_1,0,0)
        layout.addWidget(Field_2,1,0)
        layout.addWidget(Field_3,2,0)
        layout.addWidget(Field_4,0,1)
        layout.addWidget(Field_5,1,1)
        layout.addWidget(Field_6,2,1)
        layout.addWidget(Field_7,0,2)
        layout.addWidget(Field_8,1,2)
        layout.addWidget(Field_9,2,2)

        self.tab1.setLayout(layout)

    def setup_tab2(self):
        layout = QVBoxLayout()
        label = QLabel("Contenu de l'onglet 2")
        layout.addWidget(label)
        self.tab2.setLayout(layout)

    def mainLoopCallback(self):
        # TODO: implement this
        print("Main loop!") #TODO: delete this

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
