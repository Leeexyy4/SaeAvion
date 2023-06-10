import sys, TestSecondeInterface, psycopg2, json, copy, os
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from controller import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QFileDialog, QRadioButton, QCheckBox
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets
import bignono, requete

simon = "skyblue"
class Controller():
    def __init__(self) -> None:

        self.requeteSQL = ""
        self.modele = bignono.Bignono('dico.json')
        self.vue = TestSecondeInterface.Total()

        self.demandeBDD = TestSecondeInterface.DemandeBDD()
        self.demandeBDD.accepte.clicked.connect(self.connectionBDD)

        # slots ie callback
        self.vue.interf_2.nextClicked.connect(self.next)
        self.vue.interf_2.previousClicked.connect(self.previous)
        self.vue.interf_2.requeteChanged.connect(self.update)

        self.vue.interf_1.footer.requete.clicked.connect(self.CommandeMap)
        self.vue.interf_1.liste_pays.paysChange.connect(self.ajoutComboBoxComp)

        self.vue.interf_1.liste_compagnies.combo_total.currentIndexChanged.connect(self.getInfosCompagnie)


    def connectionBDD(self):
        # Connection to database
        self.DB_NAME = "sae_bdd"
        self.DB_USER = self.demandeBDD.db_user.text()
        self.DB_PASS = self.demandeBDD.db_pass.text()
        self.DB_HOST = "127.0.0.1"
        self.DB_PORT = "5432"

        try:
            conn = psycopg2.connect(database=self.DB_NAME,
                                    user=self.DB_USER,
                                    password=self.DB_PASS,
                                    host=self.DB_HOST,
                                    port=self.DB_PORT)
            print("Database connected successfully")
            self.demandeBDD.hide()
            self.cur = conn.cursor()
            self.vue.interf_1.show()
            self.ajoutComboBoxPays()
        except:
            print("Database not connected successfully")


    def getInfosCompagnie(self):

        comp_requete = self.vue.interf_1.liste_compagnies.combo_total.currentText()
        self.cur.execute("SELECT DISTINCT c.compagnie_nom, p.pays_nom, AVG((e.pollution/nr.nb_routes)) co2_par_vol, na.nb_avions/3 nb_avions_par_jour, na.nb_avions FROM compagnie c, routes r, pays p, emissions_co2_compagnie e, nb_routes_compagnies nr, nb_avions_compagnies na WHERE c.compagnie_id = r.compagnie_id AND c.pays_id = p.pays_id AND e.compagnie_id = c.compagnie_id AND nr.compagnie_id = c.compagnie_id AND na.compagnie_id = c.compagnie_id  AND c.compagnie_nom ILIKE '"+ comp_requete +"' GROUP BY c.compagnie_nom, p.pays_nom, nb_avions_par_jour, na.nb_avions")

        rows = self.cur.fetchall()[0]

        self.vue.interf_1.informations.UpdateInfos(rows[0],rows[1],rows[2],rows[3],rows[4])
        
    def maj_vue(self) -> None:
        r = self.modele.getRequete()
        print(r)
        if isinstance(r, requete.Requete):
            self.vue.updateRequete(r.requete,r.graph,r.analyse,r.explication)
    
    def update(self,d) -> None :
        r2 = requete.Requete(d['requete'], d['graph'], d['analyse'], d['explication'])
        self.modele.update(r2)

    def CommandeMap(self):
        try:
            self.fabriqueRequeteMap()
        except:
            print("ERREUR: Aucune compagnie entrée")
            return

        print(self.requeteSQL)
        #cur.execute("SELECT COUNT(aeroport_id) FROM routes r, aeroport a, pays p WHERE r.aeroport_arr_id=a.aeroport_id AND p.pays_id = a.pays_id AND pays_nom ILIKE 'germany'")
        #cur.execute(requete)
        
        self.cur.execute(self.requeteSQL)

        
        rows = self.cur.fetchall()

        points_x = []
        points_y = []

        for d in rows:
            points_x.append(d[1])
            points_y.append(d[0])



        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        # base = world.plot(color='white', edgecolor='black')
        world.plot(color=simon)
        plt.scatter(points_x, points_y, color="red", marker=".")
        plt.savefig(fname="./images/graphique")
        self.vue.interf_1.graphique.updateGraphique("./images/graphique.png")



        #plt.show()
        
    def next(self) -> None:
        self.modele.next()
        self.maj_vue()

    def previous(self) -> None:
        self.modele.previous()
        self.maj_vue()

    def ajoutComboBoxPays(self):

        self.cur.execute("SELECT pays_nom FROM pays ORDER BY pays_nom")

        rows = self.cur.fetchall()

        for i in rows:
            self.vue.interf_1.liste_pays.combo_total.addItem(i[0])

    def ajoutComboBoxComp(self, pays_comp:str):

        self.vue.interf_1.liste_compagnies.combo_total.clear()

        requete = "SELECT compagnie_nom FROM compagnie WHERE pays_id=(SELECT pays_id FROM pays WHERE pays_nom ILIKE '" + pays_comp + "') ORDER BY compagnie_nom "

        self.cur.execute(requete)

        rows = self.cur.fetchall()

        for i in rows:
            self.vue.interf_1.liste_compagnies.combo_total.addItem(i[0])

    def fabriqueRequeteMap(self):
        requetefinale = "SELECT latitude, longitude FROM aeroport WHERE aeroport_id IN (SELECT aeroport_dep_id FROM routes WHERE compagnie_id IN (SELECT compagnie_id FROM compagnie WHERE "
        comprequete = self.vue.interf_1.liste_compagnies.compagnie_requete

        if len(comprequete)>1:
            for p in range(len(comprequete)-1):
                requetefinale = requetefinale + "compagnie_nom LIKE '" + comprequete[p] + "' OR "
            requetefinale = requetefinale + "compagnie_nom LIKE '" + comprequete[len(comprequete)-1] + "'"

        else:
            requetefinale = requetefinale + "compagnie_nom LIKE '" + comprequete[0] + "'"
        
        self.requeteSQL = requetefinale + "))"

if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Controller()
    sys.exit(app.exec())