import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QLabel, QCheckBox, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap

# Classe Liste_pays qui reprend le bandeau déroulant du pays et le texte associé
class Liste_Pays(QWidget):
    #signaux

    paysChange = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()

        self.pays_actuel = ""
        
        # Ajout des informations des pays
        self.nom_pays = QLabel("Nom du pays")
        self.nom_pays.setStyleSheet("padding-left: 100px;padding-right: 100px;")
        self.nom_pays.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Création de la combobox des pays
        self.combo_total = QComboBox()
        
        # Ajout du select all
        self.selectall = QPushButton("Ajouter Pays")
        self.selectall.clicked.connect(self.changerCompRequete)
        
        # Ajout du deselect all
        self.deselectall = QPushButton("Reset Pays")
        self.deselectall.clicked.connect(self.resetPaysRequete)
        
        # Création des layout verticaux et horizontaux
        layout_ver = QVBoxLayout()
        layout_hor = QHBoxLayout()
        
        # Ajout des widgets pays
        layout_ver.addWidget(self.nom_pays)
        layout_ver.addWidget(self.combo_total)
        layout_hor.addWidget(self.selectall)
        layout_hor.addWidget(self.deselectall)
        layout_ver.addLayout(layout_hor)
        
        # Ajouter un espace extensible
        layout_ver.addStretch(1)
        
        # Setter du layout
        self.setLayout(layout_ver)

    def changerCompRequete(self):
        self.pays_actuel = self.combo_total.currentText()
        self.paysChange.emit(self.pays_actuel)

    #pour reset la liste des compagnie de la requete SQL pck sinon il faut fermer l'appli et c'est longo
    def resetPaysRequete(self):
        self.pays_requete = []
        print(self.pays_requete)
        
# Classe Liste_compagnies qui reprend le bandeau déroulant des compagnies et le texte associé
class Liste_Compagnies(QWidget):
    #signaux

    def __init__(self) -> None:
        super().__init__()

        self.compagnie_requete = []
        
        # Ajout des informations des compagnies
        self.nom_comp = QLabel("Nom de la compagnie")
        self.nom_comp.setStyleSheet("padding-left: 100px;padding-right: 100px;")
        self.nom_comp.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Création de la combobox des compagnies
        self.combo_total = QComboBox()

        # Ajout du select all
        self.selectall = QPushButton("Ajouter Compagnie")
        self.selectall.clicked.connect(self.ajoutCompRequete)
        
        # Ajout du deselect all
        self.deselectall = QPushButton("Reset Compagnie")
        self.deselectall.clicked.connect(self.resetCompRequete)
        
        # Création des layout verticaux et horizontaux
        layout_ver = QVBoxLayout()
        layout_hor = QHBoxLayout()
        
        layout_ver.addWidget(self.nom_comp)
        layout_ver.addWidget(self.combo_total)
        layout_hor.addWidget(self.selectall)
        layout_hor.addWidget(self.deselectall)
        layout_ver.addLayout(layout_hor)
        
        # Ajouter un espace extensible
        layout_ver.addStretch(1)
        
        # Setter du layout
        self.setLayout(layout_ver)

    def ajoutCompRequete(self):

        entrer = True
        for r in self.compagnie_requete:
            if r==self.combo_total.currentText():
                entrer = False
        
        if entrer==True:
            self.compagnie_requete.append(self.combo_total.currentText())
        print(self.compagnie_requete)


    #pour reset la liste des compagnie de la requete SQL pck sinon il faut fermer l'appli et c'est longo
    def resetCompRequete(self):
        self.compagnie_requete = []
        

# Classe Informations qui reprend le logo et les informations
class Informations(QWidget):
    def __init__(self):
        super().__init__()
        
        # Ajout des informations
        self.info = QLabel("Informations")
        self.info.setStyleSheet("padding-left: 100px;padding-right: 100px;")
        self.info.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Bandeau du nom de la compagnie et du champ d'écriture du nom
        self.nom_comp = QHBoxLayout()
        self.nom_comp_label = QLabel("Nom :   ")
        self.nom_comp_label.setStyleSheet("padding-right: 10px;padding-left: 10px;")
        self.nom_comp_champ = QLineEdit()
        self.nom_comp_champ.setFixedWidth(200)
        self.nom_comp_champ.setStyleSheet("margin-right: 10px;")
        self.nom_comp.addWidget(self.nom_comp_label)
        self.nom_comp.addWidget(self.nom_comp_champ)
        
        # Bandeau du pays et du champ d'écriture du pays
        self.pays_comp = QHBoxLayout()
        self.pays_comp_label = QLabel("Pays :    ")
        self.pays_comp_label.setStyleSheet("padding-right: 10px;padding-left: 10px;")
        self.pays_comp_champ = QLineEdit()
        self.pays_comp_champ.setFixedWidth(200)
        self.pays_comp_champ.setStyleSheet("margin-right: 10px;")
        self.pays_comp.addWidget(self.pays_comp_label)
        self.pays_comp.addWidget(self.pays_comp_champ)
        
        # Bandeau du Co2 et du champ d'ecriture du Co2
        self.co2_vol = QHBoxLayout()
        self.co2_vol_label = QLabel("Co2/vol :       ")
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
        self.nb_places_label = QLabel("Nb places :   ")
        self.nb_places_champ = QLineEdit()
        self.nb_places_champ.setFixedWidth(200)
        self.nb_places_champ.setStyleSheet("margin-right: 10px;")
        self.nb_places.addWidget(self.nb_places_label)
        self.nb_places.addWidget(self.nb_places_champ)
        
        # Création du layout vertical
        layout_ver = QVBoxLayout()        
        layout_ver.addWidget(self.info)
        layout_ver.addLayout(self.nom_comp)
        layout_ver.addLayout(self.pays_comp)
        layout_ver.addLayout(self.co2_vol)
        layout_ver.addLayout(self.nb_avions)
        layout_ver.addLayout(self.nb_places)
        
        # Ajouter un espace extensible
        layout_ver.addStretch(1)
        self.nom_comp.addStretch(1)
        self.pays_comp.addStretch(1)
        self.co2_vol.addStretch(1)
        self.nb_avions.addStretch(1)
        self.nb_places.addStretch(1)
        
        # Setter du layout
        self.setLayout(layout_ver)
    
class Image(QWidget):
    def __init__(self, image_path):
        super().__init__()

        # Création du layout vertical
        layout_ver = QHBoxLayout()

        # Chargement de l'image à l'aide du chemin fourni
        self.image = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(90,90)
        self.image.setPixmap(pixmap)
        layout_ver.addWidget(self.image)

        # Setter du layout
        self.setLayout(layout_ver)

class Footer(QWidget):
    #signaux

    def __init__(self):
        super().__init__()
        
        # Creation du layout vertical
        layout_ver = QHBoxLayout()       
         
        # Bouton requete
        self.precedent = QPushButton("Precedent")
        layout_ver.addWidget(self.precedent)

        # Bouton requete
        self.requete = QPushButton("Requete")
        layout_ver.addWidget(self.requete)
        
        # Bouton requete
        self.suivant = QPushButton("Suivant")
        layout_ver.addWidget(self.suivant)
                
        # Setter du layout
        self.setLayout(layout_ver)

class Graphique(QWidget):
    def __init__(self):
        super().__init__()
        self.histoire_comp = QVBoxLayout()
        self.histoire_comp_label = QLabel("Graphique de la requete : ")
        pixmap = QPixmap()
        self.histoire_comp_label.setPixmap(pixmap)

        self.histoire_comp.addWidget(self.histoire_comp_label)
        
        self.setLayout(self.histoire_comp)

    def updateGraphique(self, image_path):

        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(350,300)
        self.histoire_comp_label.setPixmap(pixmap)
        

class Interface1(QWidget):

    #signaux

    envoiCommande = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        # Caractéristique de la fenetre de l'interface
        self.resize(800, 400)
        self.setWindowTitle("Partie 1. :)")

        # Ajout de l'icone Oasix
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("./Logo.png")
        self.setWindowIcon(self.iconeFenetre)
        
        # Création des instances des classes Listes_Pays et Liste_Compagnies
        self.liste_pays = Liste_Pays()
        self.liste_compagnies = Liste_Compagnies()
        self.informations = Informations()
        self.footer = Footer()
        self.image = Image('Logo.png')
        self.graphique = Graphique()

        # Affichage de l'interface
        self.layout_vertical1 = QVBoxLayout()
        self.layout_horizontal1 = QHBoxLayout()
        self.layout_horizontal2 = QHBoxLayout()
        self.layout_horizontal3 = QHBoxLayout()
        
        # Ajout des widgets
        self.layout_horizontal1.addWidget(self.liste_pays)
        self.layout_horizontal1.addWidget(self.liste_compagnies)
        self.layout_vertical1.addLayout(self.layout_horizontal1)
        
        self.layout_horizontal2.addWidget(self.image)
        self.layout_horizontal2.addWidget(self.informations)
        self.layout_horizontal2.addWidget(self.graphique)
        self.layout_vertical1.addLayout(self.layout_horizontal2)
        
        self.layout_horizontal3.addWidget(self.footer)
        self.layout_vertical1.addLayout(self.layout_horizontal3)
        
        # Ajouter un espace extensible
        self.layout_vertical1.addStretch(1)
        
        self.setLayout(self.layout_vertical1)

        self.show()

class Interface2(QWidget):
    
    def __init__(self) -> None:

        super().__init__()
        
        # Caractéristique de la fenetre de l'interface
        self.resize(800, 400)
        self.setWindowTitle("PARTIE 2 !!!!")

        # Ajout de l'icone Oasix
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("./Logo.png")
        self.setWindowIcon(self.iconeFenetre)
        
        # Création des instances des classes Listes_Pays et Liste_Compagnies
        self.liste_pays = Liste_Pays()
        self.liste_compagnies = Liste_Compagnies()
        self.footer = Footer()
        self.image = Image('Logo.png')
        self.graphique = Graphique()

        # Affichage de l'interface
        self.layout_vertical1 = QVBoxLayout()
        self.layout_horizontal1 = QHBoxLayout()
        self.layout_horizontal2 = QHBoxLayout()
        self.layout_horizontal3 = QHBoxLayout()
        
        # Ajout des widgets
        self.layout_horizontal1.addWidget(self.liste_pays)
        self.layout_horizontal1.addWidget(self.liste_compagnies)
        self.layout_vertical1.addLayout(self.layout_horizontal1)
        
        self.layout_horizontal2.addWidget(self.image)
        self.layout_horizontal2.addWidget(self.graphique)
        self.layout_vertical1.addLayout(self.layout_horizontal2)
        
        self.layout_horizontal3.addWidget(self.footer)
        self.layout_vertical1.addLayout(self.layout_horizontal3)
        
        # Ajouter un espace extensible
        self.layout_vertical1.addStretch(1)
        
        self.setLayout(self.layout_vertical1)


class Total(QWidget):

    def __init__(self):
        super().__init__()

        self.interf_1 = Interface1()
        self.interf_2 = Interface2()

        self.interf_1.footer.suivant.clicked.connect(self.changeFenetre)
        self.interf_2.footer.suivant.clicked.connect(self.changeFenetre)

    def changeFenetre(self):
        if self.interf_2.isHidden() == True:
            self.interf_1.hide()
            self.interf_2.show()
        else:
            self.interf_2.hide()
            self.interf_1.show()

        


if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Total()
    sys.exit(app.exec())
