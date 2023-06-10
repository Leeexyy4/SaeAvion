import sys
import typing
import requete
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QLabel, QRadioButton, QLineEdit, QTextEdit, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QPalette

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
        
    #pour reset la liste des compagnie de la requete SQL pck sinon il faut fermer l'appli et c'est longo
    def resetAeroRequete(self):
        if self.deselectall.isChecked() == True:
            self.aero_requete = []

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
        


class Liste_Options(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.option_choisie = "compagnie"

        self.combo_option = QComboBox()
        self.combo_option.addItem("Pollution par compagnie")
        self.combo_option.addItem("Pollution par pays (départs)")
        self.combo_option.addItem("Pollution par pays (arrivées))")

        self.combo_option.currentTextChanged.connect(self.ajouteOption)


        #cette option est celle par défaut
        self.option_graphiqueplus = QRadioButton("10 plus polluant.e.s")
        self.option_graphiqueplus.setChecked(True)


        self.option_graphiquemoins = QRadioButton("10 moins polluant.e.s")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.combo_option)
        self.layout.addWidget(self.option_graphiqueplus)
        self.layout.addWidget(self.option_graphiquemoins)
        self.setLayout(self.layout)

    def ajouteOption(self):
        if self.combo_option.currentIndex() ==0:
            self.option_choisie = "compagnie"
        elif self.combo_option.currentIndex() ==1:
            self.option_choisie = "pays_dep"
        elif self.combo_option.currentIndex() ==2:
            self.option_choisie = "pays_arr"



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

    def UpdateInfos(self, nom_comp, nom_pays, co2_par_vol, nbavions_par_jour, nb_places):
        self.nom_comp_champ.setText(nom_comp)
        self.pays_comp_champ.setText(nom_pays)
        self.co2_vol_champ.setText(str(co2_par_vol))
        self.nb_avions_champ.setText(str(nbavions_par_jour))
        self.nb_places_champ.setText(str(nb_places))

    
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

    def updateGraphique(self, image_path:str, size:tuple):

        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(size[0],size[1])
        self.histoire_comp_label.setPixmap(pixmap)
        

class Interface1(QWidget):

    #signaux

    envoiCommande = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        # Caractéristique de la fenetre de l'interface
        self.resize(800, 400)
        self.setWindowTitle("Interface 1 : Emplacement des aéroports d'arrivée des compagnies")
        self.setStyleSheet('Interface1{background:#D4F6FF}')

        # Ajout de l'icone Oasix
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("images/Logo.png")
        self.setWindowIcon(self.iconeFenetre)
        
        # Création des instances des classes Listes_Pays et Liste_Compagnies
        self.liste_pays = Liste_Pays()
        self.liste_compagnies = Liste_Compagnies()
        self.informations = Informations()
        self.footer = Footer()
        self.image = Image('images/Logo.png')
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


class Interface2(QWidget):
    # signal
    requeteChanged : pyqtSignal = pyqtSignal(dict)
    nextClicked = pyqtSignal()
    previousClicked = pyqtSignal()
    
    def __init__(self) -> None:

        super().__init__()
        
        # Caractéristique de la fenetre de l'interface
        self.resize(800, 400)
        self.setWindowTitle("Requêtes qui pourraient vous interesser...")
        self.setStyleSheet('Interface2{background:#FFC1C1}')

        # Widgets
        self.requete = QLineEdit()
        self.graph = QLabel()
        self.analyse = QTextEdit("Analyse du graphique par notre équipe")
        self.explication = QTextEdit("Explication des données du graphiques")
        self.footer = Footer()
        
        # Read only text
        self.requete.setReadOnly(True)
        self.analyse.setReadOnly(True)
        self.explication.setReadOnly(True)

        # Buttons
        self.precedent = QPushButton("<< précédent")
        self.suivant = QPushButton("suivant >>")
        

        # signaux
        self.requete.editingFinished.connect(self.changeRequete)
        self.analyse.textChanged.connect(self.changeRequete)
        self.explication.textChanged.connect(self.changeRequete)

        self.precedent.clicked.connect(self.requetePrecedente)
        self.suivant.clicked.connect(self.requeteSuivante)
        
        layout = QVBoxLayout(); self.setLayout(layout)
        nom_requete = QHBoxLayout()
        graphi = QHBoxLayout()
        analyse_expli = QHBoxLayout()

        nom_requete.addWidget(self.precedent, 1)
        nom_requete.addWidget(self.requete,6)
        analyse_expli.addWidget(self.analyse, 1)
        analyse_expli.addWidget(self.explication, 1)
        nom_requete.addWidget(self.suivant, 1)
        nom_requete.addWidget(self.precedent, 1)
        layout.addLayout(nom_requete)
        layout.addLayout(graphi)
        layout.addLayout(analyse_expli)
        layout.addWidget(self.footer)
        
        self.image = QLabel()
        pixmap = QPixmap("Logo.png")
        pixmap = pixmap.scaled(90,90)
        self.image.setPixmap(pixmap)
        graphi.addWidget(self.image)
            
    def updateGraphi(self, graph):
        pixmap = QPixmap(graph)
        pixmap = pixmap.scaled(350,300)
        self.image.setPixmap(pixmap)
    
        
    def setRequete(self, req) -> None :
        self.requete.setText(req)
        
    def setGraph(self, graphique) -> None :
        self.graph.setText(graphique)
    
    def setAnalyse(self, an) -> None :
        self.analyse.setText(an)
        
    def setExplication(self, exp) -> None :
        self.explication.setText(exp)
    
    def changeRequete(self) -> None :
        self.requeteChanged.emit(self.getAllInfo())

    def requetePrecedente(self) -> None :
        self.previousClicked.emit()

    def requeteSuivante(self) -> None :
        self.nextClicked.emit()

    def getAllInfo(self) -> dict:
        resultat = {"requete":(self.requete.text()), 
                    "graph":self.graph.text(), 
                    "analyse":self.analyse.toPlainText(), 
                    "explication": self.explication.toPlainText()}
        return resultat


class Interface3(QWidget):
    
    def __init__(self) -> None:

        super().__init__()
        
        # Caractéristique de la fenetre de l'interface
        self.resize(800, 400)
        self.setWindowTitle("Interface 3: Graphiques de tests du CO2")
        self.setStyleSheet('Interface3{background:#FFD8BE}')

        # Ajout de l'icone Oasix
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("./Logo.png")
        self.setWindowIcon(self.iconeFenetre)
        
        # Création des instances des classes Listes_Pays et Liste_Compagnies
        self.liste_options = Liste_Options()
        self.footer = Footer()
        self.graphique = Graphique()

        # Affichage de l'interface
        self.layout_vertical = QVBoxLayout()
        
        # Ajout des widgets
        self.layout_vertical.addWidget(self.liste_options)
        self.layout_vertical.addWidget(self.graphique)
        self.layout_vertical.addWidget(self.footer)


        # Ajouter un espace extensible
        self.layout_vertical.addStretch(1)
        
        self.setLayout(self.layout_vertical)

class DemandeBDD(QWidget):
    def __init__(self) -> None:
    
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.resize(400, 100)
        self.setWindowTitle("Bienvenue sur notre interface")

        # Ajout de l'icone Oasix
        self.iconeFenetre = QIcon()
        self.iconeFenetre.addFile("./Logo.png")
        self.setWindowIcon(self.iconeFenetre)

        #pour obtenir le mdp et l'utilisateur pour accèder à la base de données
        self.db_name = QLineEdit()
        self.db_user = QLineEdit()
        self.db_pass = QLineEdit()

        self.db_name.setPlaceholderText("Nom de votre base de données")
        self.db_user.setPlaceholderText("Votre nom d'utilisateur SQL")
        self.db_pass.setPlaceholderText("Votre mot de passe de l'utilisateur SQL")

        self.accepte = QPushButton("Connection à la base de données")

        self.layout.addWidget(self.db_name)
        self.layout.addWidget(self.db_user)
        self.layout.addWidget(self.db_pass)
        self.layout.addWidget(self.accepte)


        #seule cette interface est montrée au début
        self.show()

class Total(QWidget):

    def __init__(self):
        super().__init__()

        self.interf_1 = Interface1()
        self.interf_2 = Interface2()
        self.interf_3 = Interface3()

        self.interf_1.footer.suivant.clicked.connect(self.changeFenetreSuiv)
        self.interf_2.footer.suivant.clicked.connect(self.changeFenetreSuiv)
        self.interf_3.footer.suivant.clicked.connect(self.changeFenetreSuiv)
        
        self.interf_1.footer.precedent.clicked.connect(self.changeFenetrePrec)
        self.interf_2.footer.precedent.clicked.connect(self.changeFenetrePrec)
        self.interf_3.footer.precedent.clicked.connect(self.changeFenetrePrec)
        
            
    # update : mise à jour de la vue pour la 2e interface
    def updateRequete(self, requete: str, graph:str, analyse: str, 
                        explication: str) -> None :
        self.interf_2.setRequete(requete)
        self.interf_2.setGraph(graph)
        self.interf_2.setAnalyse(analyse)
        self.interf_2.setExplication(explication)

    #si les 2 autres interfaces sont cachées, alors cache celle qui ne l'est pas et on affiche la suivante
    def changeFenetreSuiv(self):
        if self.interf_2.isHidden() == True and self.interf_1.isHidden() == True:
            self.interf_3.hide()
            self.interf_1.show()
        elif self.interf_3.isHidden() == True and self.interf_1.isHidden() == True:
            self.interf_2.hide()
            self.interf_3.show()
        else:
            self.interf_1.hide()
            self.interf_2.show()


    #si les 2 autres interfaces sont cachées, alors cache celle qui ne l'est pas et on affiche la precedente
    def changeFenetrePrec(self):
        if self.interf_2.isHidden() == True and self.interf_1.isHidden() == True:
            self.interf_3.hide()
            self.interf_2.show()
        elif self.interf_3.isHidden() == True and self.interf_1.isHidden() == True:
            self.interf_2.hide()
            self.interf_1.show()
        else:
            self.interf_1.hide()
            self.interf_3.show()


if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Total()
    sys.exit(app.exec())
