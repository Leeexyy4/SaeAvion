import sys
import typing
import psycopg2
from Controlleur_Arno import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QFileDialog, QRadioButton, QCheckBox
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6.QtGui import QIcon
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
        self.combo_total.addItem("Afghanistan")
        self.combo_total.addItem("Albania")
        self.combo_total.addItem("Algeria")
        self.combo_total.addItem("American Samao")
        self.combo_total.addItem("Angola")
        self.combo_total.addItem("Anguilla")
        self.combo_total.addItem("Antartica")
        self.combo_total.addItem("Antigua and Barbuda")
        self.combo_total.addItem("Argentina")
        self.combo_total.addItem("Armenia")
        self.combo_total.addItem("Aruba")
        self.combo_total.addItem("Ashmore and Cartier Islands")
        self.combo_total.addItem("Australia")
        self.combo_total.addItem("Austria")
        self.combo_total.addItem("Azerbaijan")
        self.combo_total.addItem("Bahamas")
        self.combo_total.addItem("Bahrain")
        self.combo_total.addItem("Baker Island")
        self.combo_total.addItem("Bangladesh")
        self.combo_total.addItem("Barbados")
        self.combo_total.addItem("Belarus")
        self.combo_total.addItem("Belgium")
        self.combo_total.addItem("Belize")
        self.combo_total.addItem("Benin")
        self.combo_total.addItem("Bermuda")
        self.combo_total.addItem("Bhutan")
        self.combo_total.addItem("Bolivia")
        self.combo_total.addItem("Bonaire, Saint Eustatius and Saba")
        self.combo_total.addItem("Bosnia and Herzegovina")
        self.combo_total.addItem("Botswana")
        self.combo_total.addItem("Bouvet Island")
        self.combo_total.addItem("Brazil")
        self.combo_total.addItem("British Indian Ocean Territory")
        self.combo_total.addItem("British Virgin Islands")
        self.combo_total.addItem("Brunei Darussalam")
        self.combo_total.addItem("Bulgaria")
        self.combo_total.addItem("Burkina Faso")
        self.combo_total.addItem("Burundi")
        self.combo_total.addItem("Cambodia")
        self.combo_total.addItem("Cameroon")
        self.combo_total.addItem("Canada")
        self.combo_total.addItem("Cape Verde")
        self.combo_total.addItem("Cayman Islands")
        self.combo_total.addItem("Central African Republic")
        self.combo_total.addItem("Chad")
        self.combo_total.addItem("Chile")
        self.combo_total.addItem("China")
        self.combo_total.addItem("Christmas Island")
        self.combo_total.addItem("Clipperton Island")
        self.combo_total.addItem("Cocos (Keeling) Islands")
        self.combo_total.addItem("Colombia")
        self.combo_total.addItem("Comoros")
        self.combo_total.addItem("Congo Republic")
        self.combo_total.addItem("Cook Islands")
        self.combo_total.addItem("Coral Sea Islands")
        self.combo_total.addItem("Costa Rica")
        self.combo_total.addItem("Cote d'Ivoire")
        self.combo_total.addItem("Croatia")
        self.combo_total.addItem("Cuba")
        self.combo_total.addItem("Cyprus")
        self.combo_total.addItem("Czech Republic")
        self.combo_total.addItem("Denmark")
        self.combo_total.addItem("Djibouti")
        self.combo_total.addItem("Dominica")
        self.combo_total.addItem("Dominican Republic")
        self.combo_total.addItem("DR Congo")
        self.combo_total.addItem("Ecuador")
        self.combo_total.addItem("Egypt")
        self.combo_total.addItem("El Salvador")
        self.combo_total.addItem("Equatorial Guinea")
        self.combo_total.addItem("Eritrea")
        self.combo_total.addItem("Estonia")
        self.combo_total.addItem("Eswatini")
        self.combo_total.addItem("Ethiopia")
        self.combo_total.addItem("Europa Island")
        self.combo_total.addItem("Faeroe Islands")
        self.combo_total.addItem("Falkland Islands")
        self.combo_total.addItem("Fiji")
        self.combo_total.addItem("Finland")
        self.combo_total.addItem("France")
        self.combo_total.addItem("French Guiana")
        self.combo_total.addItem("French Polynesia")
        self.combo_total.addItem("French Southern Territories")
        self.combo_total.addItem("Gabon")
        self.combo_total.addItem("Gambia")
        self.combo_total.addItem("Georgia")
        self.combo_total.addItem("Germany")
        self.combo_total.addItem("Ghana")
        self.combo_total.addItem("Gibraltar")
        self.combo_total.addItem("Glorioso Islands")
        self.combo_total.addItem("Greenland")
        self.combo_total.addItem("Grenada")
        self.combo_total.addItem("Guadeloupe")
        self.combo_total.addItem("Guam")
        self.combo_total.addItem("Guatemala")
        self.combo_total.addItem("Guernsey")
        self.combo_total.addItem("Guinea")
        self.combo_total.addItem("Guinea-Bissau")
        self.combo_total.addItem("Guyana")
        self.combo_total.addItem("Haiti")
        self.combo_total.addItem("Heard and McDonald Islands")
        self.combo_total.addItem("Honduras")
        self.combo_total.addItem("Hong Kong")
        self.combo_total.addItem("Howland Island")
        self.combo_total.addItem("Hungary")
        self.combo_total.addItem("Iceland")
        self.combo_total.addItem("India") # Il y en a deux 
        self.combo_total.addItem("Indonesia")
        self.combo_total.addItem("Iran")
        self.combo_total.addItem("Iraq")
        self.combo_total.addItem("Ireland")
        self.combo_total.addItem("Isle of Man")
        self.combo_total.addItem("Israel")
        self.combo_total.addItem("Italy")
        self.combo_total.addItem("Jamaica")
        self.combo_total.addItem("Jan Mayen")
        self.combo_total.addItem("Japan")
        self.combo_total.addItem("Jarvis Island")
        self.combo_total.addItem("Jersey")
        self.combo_total.addItem("Johnston Atoll")
        self.combo_total.addItem("Jordan")
        self.combo_total.addItem("Juan de Nova Island")
        self.combo_total.addItem("Kazakhstan")
        self.combo_total.addItem("Kenya")
        self.combo_total.addItem("Kingman Reef")
        self.combo_total.addItem("Kiribati")
        self.combo_total.addItem("Kuwait")
        self.combo_total.addItem("Kyrgyz Republic")
        self.combo_total.addItem("Laos")
        self.combo_total.addItem("Latvia")
        self.combo_total.addItem("Lebanon")
        self.combo_total.addItem("Lesotho")
        self.combo_total.addItem("Liberia")
        self.combo_total.addItem("Libya")
        self.combo_total.addItem("Lithuania")
        self.combo_total.addItem("Luxembourg")
        self.combo_total.addItem("Macao")
        self.combo_total.addItem("Macedonia")
        self.combo_total.addItem("Madagascar")
        self.combo_total.addItem("Malawi")
        self.combo_total.addItem("Malaysia")
        self.combo_total.addItem("Maldives")
        self.combo_total.addItem("Mali")
        self.combo_total.addItem("Malta")
        self.combo_total.addItem("Marshall Islands")
        self.combo_total.addItem("Martinique")
        self.combo_total.addItem("Mauritania")
        self.combo_total.addItem("Mauritius")
        self.combo_total.addItem("Mayotte")
        self.combo_total.addItem("Mexico")
        self.combo_total.addItem("Micronesia")
        self.combo_total.addItem("Midway Islands")
        self.combo_total.addItem("Moldova")
        self.combo_total.addItem("Monaco")
        self.combo_total.addItem("Mongolia")
        self.combo_total.addItem("Montenegro")
        self.combo_total.addItem("Montserrat")
        self.combo_total.addItem("Morocco")
        self.combo_total.addItem("Mozambique")
        self.combo_total.addItem("Myanmar")
        self.combo_total.addItem("Namibia")
        self.combo_total.addItem("Nauru")
        self.combo_total.addItem("Navassa Island")
        self.combo_total.addItem("Nepal")
        self.combo_total.addItem("Netherlands")
        self.combo_total.addItem("Netherlands Antilles")
        self.combo_total.addItem("New Caledonia")
        self.combo_total.addItem("New Zealand")
        self.combo_total.addItem("Nicaragua")
        self.combo_total.addItem("Niger")
        self.combo_total.addItem("Nigeria")
        self.combo_total.addItem("Niue")
        self.combo_total.addItem("Norfolk Island")
        self.combo_total.addItem("North Korea")
        self.combo_total.addItem("Northern Mariana Islands")
        self.combo_total.addItem("Norway")
        self.combo_total.addItem("Pakistan")
        self.combo_total.addItem("Palau")
        self.combo_total.addItem("Palestine") # Il y en a deux 
        

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
        
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("./Logo.png")
        self.setWindowIcon(self.iconeFenetre)
        
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