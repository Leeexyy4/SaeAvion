import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QLabel, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


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
        
class Image():
    pass

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

        # Affichage de l'interface
        self.affichage = QHBoxLayout()
        self.affichage.addWidget(self.listes_pays)
        self.affichage.addWidget(self.liste_compagnies)
                        
        self.setLayout(self.affichage)

        self.show()


if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Interface()
    sys.exit(app.exec())
