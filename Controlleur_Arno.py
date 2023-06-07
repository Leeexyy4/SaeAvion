import sys, TestSecondeInterface
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from Controlleur_Arno import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QFileDialog, QRadioButton, QCheckBox
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets


class Controller():
    def __init__(self) -> None:
        self.DB_NAME = "sae_bdd" #A CHANGER POUR QUE CA MARCHE POUR VOUS /!\/!\/!\/!\/!\/!\/!\
        self.DB_USER = "wissocq"
        self.DB_PASS = "arnaudwq"
        self.DB_HOST = "127.0.0.1"
        self.DB_PORT = "5432"


        try:
            conn = psycopg2.connect(database=self.DB_NAME,
                                    user=self.DB_USER,
                                    password=self.DB_PASS,
                                    host=self.DB_HOST,
                                    port=self.DB_PORT)
            print("Database connected successfully")
        except:
            print("Database not connected successfully")
            sys.exit()

        self.cur = conn.cursor()

        self.requeteSQL = ""
        self.vue = TestSecondeInterface.Total()

        self.ajoutComboBoxPays()

        self.vue.interf_1.footer.requete.clicked.connect(self.Commande)
        self.vue.interf_1.liste_pays.paysChange.connect(self.ajoutComboBoxComp)
 
    def Commande(self):

        self.fabriqueRequete()

        print(self.requeteSQL)
        #cur.execute("SELECT COUNT(aeroport_id) FROM routes r, aeroport a, pays p WHERE r.aeroport_arr_id=a.aeroport_id AND p.pays_id = a.pays_id AND pays_nom ILIKE 'germany'")
        #cur.execute(requete)
        self.cur.execute(self.requeteSQL)

        
        rows = self.cur.fetchall()

        points_x = []
        points_y = []

        for d in rows:
            print(d)
            points_x.append(d[1])
            points_y.append(d[0])


        plt.scatter(points_x, points_y)
        plt.savefig(fname="graphique")
        self.vue.interf_1.graphique.updateGraphique("graphique.png")

        # fig, ax = plt.subplots(1, figsize=(4, 4), dpi=300)
        # ax.plot([1, 3, 5, 8, 4, 2])
        # fig.canvas.draw()
        # temp_canvas = fig.canvas
        # plt.close()

        print("a")

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

    def fabriqueRequete(self):
        requetefinale = "SELECT latitude, longitude FROM aeroport WHERE aeroport_id IN (SELECT aeroport_arr_id FROM routes WHERE compagnie_id IN (SELECT compagnie_id FROM compagnie WHERE "
        comprequete = self.vue.interf_1.liste_compagnies.compagnie_requete

        if len(comprequete)>1:
            for p in range(len(comprequete)-1):
                requetefinale = requetefinale + "compagnie_nom LIKE '" + comprequete[p] + "' OR "
            requetefinale = requetefinale + "compagnie_nom LIKE '" + comprequete[p] + "'"

        else:
            requetefinale = requetefinale + "compagnie_nom LIKE '" + comprequete[0] + "'"
        
        self.requeteSQL = requetefinale + "))"

if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Controller()
    sys.exit(app.exec())