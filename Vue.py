import sys
import typing
import psycopg2
from Controlleur_Arno import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QFileDialog, QRadioButton, QCheckBox
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets


class Infos_Pays(QVBoxLayout) :
    #signaux

    envoiCommande = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        
        # Pour sélectionner les pays
        self.table_pays = []

        # Bandeau d'informartions des compagnies
        self.nom_col3 = QLabel("Infos Compagnie")
        self.nom_col3.setStyleSheet("padding-left: 100px;padding-right: 100px;")
        self.nom_col3.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Bandeau du nom de la compagnie et du champ d'écriture du nom
        self.nom_comp = QHBoxLayout()
        self.nom_comp_label = QLabel("Nom : ")
        self.nom_comp_label.setStyleSheet("padding-right: 10px;padding-left: 10px;")
        self.nom_comp_champ = QLineEdit()
        self.nom_comp_champ.setFixedWidth(200)
        self.nom_comp_champ.setStyleSheet("margin-right: 10px;")
        self.nom_comp.addWidget(self.nom_comp_label)
        self.nom_comp.addWidget(self.nom_comp_champ)
        
        # Bandeau du pays et du champ d'écriture du pays
        self.pays_comp = QHBoxLayout()
        self.pays_comp_label = QLabel("Pays : ")
        self.pays_comp_label.setStyleSheet("padding-right: 10px;padding-left: 10px;")
        self.pays_comp_champ = QLineEdit()
        self.pays_comp_champ.setFixedWidth(200)
        self.pays_comp_champ.setStyleSheet("margin-right: 10px;")
        self.pays_comp.addWidget(self.pays_comp_label)
        self.pays_comp.addWidget(self.pays_comp_champ)
        
        # Bandeau du Co2 et du champ d'ecriture du Co2
        self.co2_vol = QHBoxLayout()
        self.co2_vol_label = QLabel("Co2/vol : ")
        self.co2_vol_champ = QLineEdit()
        self.co2_vol_champ.setFixedWidth(200)
        self.co2_vol_champ.setStyleSheet("margin-right: 10px;")
        self.co2_vol.addWidget(self.co2_vol_label)
        self.co2_vol.addWidget(self.co2_vol_champ)
        
        # Bandeau du Nbr d'avions/j et du champ d'ecriture du Nbr d'avions par jours
        self.nb_avions = QHBoxLayout()
        self.nb_avions_label = QLabel("Nb avions/j : ")
        self.nb_avions_champ = QLineEdit()
        self.nb_avions_champ.setFixedWidth(200)
        self.nb_avions_champ.setStyleSheet("margin-right: 10px;")
        self.nb_avions.addWidget(self.nb_avions_label)
        self.nb_avions.addWidget(self.nb_avions_champ)
        
        # Bandeau du Nb de places et du champ d'ecriture du Nb de places
        self.nb_places = QHBoxLayout()
        self.nb_places_label = QLabel("Nb places : ")
        self.nb_places_champ = QLineEdit()
        self.nb_places_champ.setFixedWidth(200)
        self.nb_places_champ.setStyleSheet("margin-right: 10px;")
        self.nb_places.addWidget(self.nb_places_label)
        self.nb_places.addWidget(self.nb_places_champ)
        
        # Widget textedit Histoire compagnie : 
        self.histoire_comp = QVBoxLayout()
        self.histoire_comp_label = QLabel("Histoire compagnie : ")
        self.histoire_comp_champ = QTextEdit()
        self.histoire_comp_champ.setStyleSheet("margin-bottom: 30px;")
        self.requete = QPushButton("Requete")
        self.requete.clicked.connect(self.send)

        self.histoire_comp.addWidget(self.requete)
        self.histoire_comp.addWidget(self.histoire_comp_label)
        self.histoire_comp.addWidget(self.histoire_comp_champ)
        
        
        self.addWidget(self.nom_col3)
        self.addLayout(self.nom_comp)
        self.addLayout(self.pays_comp)
        self.addLayout(self.co2_vol)
        self.addLayout(self.nb_avions)
        self.addLayout(self.nb_places)
        self.addLayout(self.histoire_comp)

    def send(self):
        self.requete_sql = "SELECT latitude, longitude FROM aeroport WHERE type LIKE 'airport' AND pays_id=(SELECT pays_id FROM pays WHERE pays_nom ILIKE "+ self.table_pays[0]+ ")"
        self.envoiCommande.emit(self.requete_sql)

class Listes_Pays(QWidget):
    
    def __init__(self) -> None:
        super().__init__()

        self.combo_total = QComboBox()
        self.combo_total.addItem("Arabie Saoudite")
        self.combo_total.addItem("Kirguistan")
        self.combo_total.addItem("France")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.combo_total)
        

class Interface(QWidget):

    #signaux


    def __init__(self):
        super().__init__()
        
        # Colonne Compagnie
        self.compagnie = QVBoxLayout()
        self.nom_col1 = QLabel("Compagnie")
        self.nom_col1.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.nom_col1.setStyleSheet("padding-left: 25px;padding-right: 25px;")
        # self.nom_col1.setStyleSheet("background-color: rgb(235, 235, 235);position: relative; padding-top: 10px; padding-right: 2px; padding-bottom: 10px; padding-left: 2px;font-size: 20px;")
        self.nom_comp1 = QCheckBox("France", self)
        self.nom_comp1.clicked.connect(lambda: self.changeTableSQL(self.nom_comp1))
        # self.nom_comp1.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp2 = QCheckBox("Spain", self)
        self.nom_comp2.clicked.connect(lambda: self.changeTableSQL(self.nom_comp2))
        # self.nom_comp2.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp3 = QCheckBox("Etats-Unis", self)
        self.nom_comp3.clicked.connect(lambda: self.changeTableSQL(self.nom_comp3))
        # self.nom_comp3.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp4 = QCheckBox("NomComp", self)
        # self.nom_comp4.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp5 = QCheckBox("NomComp", self)
        # self.nom_comp5.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp6 = QCheckBox("NomComp", self)
        # self.nom_comp6.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp7 = QCheckBox("NomComp", self)
        # self.nom_comp7.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.nom_comp8 = QCheckBox("NomComp", self)
        # self.nom_comp8.setStyleSheet("background-color: rgb(200, 200, 200);padding: 20px;")
        self.compagnie_select_all = QPushButton("select all")
        self.compagnie_select_all.clicked.connect(self.check)
        self.compagnie_deselect_all = QPushButton("deselect all")
        self.compagnie_deselect_all.clicked.connect(self.uncheck)

        self.compagnie.addWidget(self.nom_col1)
        self.compagnie.addWidget(self.nom_comp1, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp2, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp3, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp4, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp5, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp6, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp7, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.nom_comp8, alignment=Qt.AlignmentFlag.AlignTop)
        self.compagnie.addWidget(self.compagnie_select_all)
        self.compagnie.addWidget(self.compagnie_deselect_all)




        # Colonne Pays
        self.pays = QVBoxLayout()

        self.nom_col2 = QLabel("Pays")
        self.nom_col2.setStyleSheet("padding-left: 25px;padding-right: 25px;")
        # self.nom_col2.setStyleSheet("background-color: rgb(235, 235, 235);position: relative; padding-top: 10px; padding-right: 2px; padding-bottom: 10px; padding-left: 2px;font-size: 20px;")
        
        self.nom_pays1 = QCheckBox("NomPays", self)
        #place les QCheckBox nom_pays1 un peu plus haut
        self.nom_pays1.setStyleSheet("padding-top: 10px;")
        self.nom_pays2 = QCheckBox("NomPays", self)
        self.nom_pays3 = QCheckBox("NomPays", self)
        self.nom_pays4 = QCheckBox("NomPays", self)
        self.pays_select_all = QPushButton("select all")
        self.pays_deselect_all = QPushButton("deselect all")
        
        self.pays.addWidget(self.nom_col2)
        self.nom_col2.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.pays.addWidget(self.nom_pays1, alignment=Qt.AlignmentFlag.AlignTop)
        self.pays.addWidget(self.nom_pays2, alignment=Qt.AlignmentFlag.AlignTop)
        self.pays.addWidget(self.nom_pays3, alignment=Qt.AlignmentFlag.AlignTop)
        self.pays.addWidget(self.nom_pays4, alignment=Qt.AlignmentFlag.AlignTop)
        self.pays.addWidget(self.pays_select_all)
        self.pays.addWidget(self.pays_deselect_all)
        
        self.infos_pays = Infos_Pays()
        self.combobox = Listes_Pays()
        
        
        # Colonne Graphique
        self.graphique = QVBoxLayout()
        self.nom_col4 = QLabel("Graphique")
        self.nom_col4.setStyleSheet("padding-left: 150px;padding-right: 150px;")
        self.nom_col4.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.attend = QTextEdit()
        self.graphique.addWidget(self.nom_col4)
        self.graphique.addWidget(self.attend)
        
        
        
        
        self.affichage = QHBoxLayout()
        self.affichage.addLayout(self.combobox.layout)
        self.affichage.addLayout(self.compagnie)
        self.affichage.addLayout(self.pays)
        self.affichage.addLayout(self.infos_pays)
        self.affichage.addLayout(self.graphique)
        self.setLayout(self.affichage)
        
        self.show()
        
    def check(self):
        self.nom_comp1.setChecked(True)
        self.nom_comp2.setChecked(True)
        self.nom_comp3.setChecked(True)
        self.nom_comp4.setChecked(True)
        self.nom_comp5.setChecked(True)
        self.nom_comp6.setChecked(True)
        self.nom_comp7.setChecked(True)
        self.nom_comp8.setChecked(True)
        
    def uncheck(self):
        self.nom_comp1.setChecked(False)
        self.nom_comp2.setChecked(False)
        self.nom_comp3.setChecked(False)
        self.nom_comp4.setChecked(False)
        self.nom_comp5.setChecked(False)
        self.nom_comp6.setChecked(False)
        self.nom_comp7.setChecked(False)
        self.nom_comp8.setChecked(False)

    def changeTableSQL(self, boite:QCheckBox):
        if boite.isChecked():

            self.infos_pays.table_pays.append("'"+boite.text()+ "'")
        else:
            self.infos_pays.table_pays.remove("'"+boite.text()+ "'")
        print(self.infos_pays.table_pays)



        
                   
if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Interface()
    sys.exit(app.exec())