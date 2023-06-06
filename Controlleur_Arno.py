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
        self.DB_USER = "crpsim"
        self.DB_PASS = "simoncrp"
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

        self.ajoutComboBox()
        self.vue.interf_1.liste_compagnies.resetCompRequete()
        self.vue.interf_1.liste_aero.resetAeroRequete()

        self.vue.interf_1.footer.requete.clicked.connect(self.Commande)
 
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
            points_x.append(d[1])
            points_y.append(d[0])

        plt.scatter(points_x, points_y)

        # fig, ax = plt.subplots(1, figsize=(4, 4), dpi=300)
        # ax.plot([1, 3, 5, 8, 4, 2])
        # fig.canvas.draw()
        # temp_canvas = fig.canvas
        # plt.close()

        plt.show()

    def ajoutComboBox(self):

        self.cur.execute("SELECT compagnie_nom FROM compagnie ORDER BY compagnie_nom")

        rows = self.cur.fetchall()

        for i in rows:
            self.vue.interf_1.liste_compagnies.combo_total.addItem(i[0])

        self.cur.execute("SELECT aeroport_nom FROM aeroport ORDER BY aeroport_nom")

        rows = self.cur.fetchall()

        for i in rows:
            self.vue.interf_1.liste_aero.combo_total.addItem(i[0])

    def fabriqueRequete(self):
        requetefinale = "SELECT aeroport_id FROM aeroport WHERE "
        aerorequete = self.vue.interf_1.liste_aero.aero_requete

        if len(aerorequete)>1:
            for p in range(len(aerorequete)-1):
                requetefinale = requetefinale + "aeroport_nom LIKE '" + aerorequete[p] + "' OR "
            requetefinale = requetefinale + "aeroport_nom LIKE '" + aerorequete[p] + "'"

        else:
            requetefinale = requetefinale + "aeroport_nom LIKE '" + aerorequete[0] + "'"
        
        self.requeteSQL = requetefinale
        print(self.requeteSQL)

if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Controller()
    sys.exit(app.exec())