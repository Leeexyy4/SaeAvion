import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QLabel, QCheckBox, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Classe Liste_pays qui reprend le bandeau déroulant du pays et le texte associé
class Listes_Pays(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        # Ajout des informations des pays
        self.nom_pays = QLabel("Nom du pays")
        self.nom_pays.setStyleSheet("padding-left: 100px;padding-right: 100px;")
        self.nom_pays.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Création de la combobox des pays
        self.combo_total = QComboBox()
        self.combo_total.addItem("Afghanistan")
        self.combo_total.addItem("Albania")
        self.combo_total.addItem("Algeria")
        self.combo_total.addItem("American Samao")
        
        # Ajout du select all
        self.selectall = QCheckBox("Select All")
        
        # Ajout du deselect all
        self.deselectall = QCheckBox("Deselect All")
        
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
        
# Classe Liste_compagnies qui reprend le bandeau déroulant des compagnies et le texte associé
class Liste_Compagnies(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        # Ajout des informations des compagnies
        self.nom_comp = QLabel("Nom de la compagnie")
        self.nom_comp.setStyleSheet("padding-left: 100px;padding-right: 100px;")
        self.nom_comp.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Création de la combobox des compagnies
        self.combo_total = QComboBox()
        self.combo_total.addItem("1-2-go")
        self.combo_total.addItem("12 North")
        self.combo_total.addItem("135 Airways")
        self.combo_total.addItem("1Time Airline")

        # Ajout du select all
        self.selectall = QCheckBox("Select All")
        
        # Ajout du deselect all
        self.deselectall = QCheckBox("Deselect All")
        
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
        
        # Widget textedit Histoire compagnie : 
        self.histoire_comp = QVBoxLayout()
        self.histoire_comp_label = QLabel("Histoire compagnie : ")
        self.histoire_comp_champ = QTextEdit()
        self.histoire_comp_champ.setStyleSheet("margin-bottom: 30px;")
        self.histoire_comp_champ.setMaximumSize(265,200)
        self.histoire_comp.addWidget(self.histoire_comp_label)
        self.histoire_comp.addWidget(self.histoire_comp_champ)
        
        # Création des layout verticaux et horizontaux
        layout_ver = QVBoxLayout()        
        layout_ver.addWidget(self.info)
        layout_ver.addLayout(self.nom_comp)
        layout_ver.addLayout(self.pays_comp)
        layout_ver.addLayout(self.co2_vol)
        layout_ver.addLayout(self.nb_avions)
        layout_ver.addLayout(self.nb_places)
        layout_ver.addLayout(self.histoire_comp)
        
        # Ajouter un espace extensible
        layout_ver.addStretch(1)
        self.nom_comp.addStretch(1)
        self.pays_comp.addStretch(1)
        self.co2_vol.addStretch(1)
        self.nb_avions.addStretch(1)
        self.nb_places.addStretch(1)
        
        # Setter du layout
        self.setLayout(layout_ver)
    

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        
        # Caractéristique de la fenetre de l'interface
        self.resize(800, 600)

        # Ajout de l'icone Oasix
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("./Logo.png")
        self.setWindowIcon(self.iconeFenetre)
        
        # Création des instances des classes Listes_Pays et Liste_Compagnies
        self.listes_pays = Listes_Pays()
        self.liste_compagnies = Liste_Compagnies()
        self.informations = Informations()

        # Affichage de l'interface
        self.layout_principal = QVBoxLayout()
        
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.listes_pays)
        self.layout_horizontal.addWidget(self.liste_compagnies)
        
        self.layout_principal.addLayout(self.layout_horizontal)
        self.layout_principal.addWidget(self.informations)
        
        # Ajouter un espace extensible
        self.layout_principal.addStretch(1)
        
        self.setLayout(self.layout_principal)

        self.show()


if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Interface()
    sys.exit(app.exec())