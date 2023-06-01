import sys, TestInterface
import psycopg2
import matplotlib.pyplot as plt
from Controlleur_Arno import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QFileDialog, QRadioButton, QCheckBox
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets


class Controller():
    def __init__(self) -> None:
        self.DB_NAME = "SAE_BDD" #A CHANGER POUR QUE CA MARCHE POUR VOUS /!\/!\/!\/!\/!\/!\/!\
        self.DB_USER = "wissocq"
        self.DB_PASS = "arnaudwq"
        self.DB_HOST = "172.25.176.1"
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

        self.cur = conn.cursor()

        self.vue = TestInterface.Interface()

        #self.vue.infos_pays.envoiCommande.connect(self.Commande)
        self.ajoutComboBox()
 
    def Commande(self, requete):

        print(requete)
        #cur.execute("SELECT COUNT(aeroport_id) FROM routes r, aeroport a, pays p WHERE r.aeroport_arr_id=a.aeroport_id AND p.pays_id = a.pays_id AND pays_nom ILIKE 'germany'")
        #cur.execute(requete)
        self.cur.execute(requete)

        
        rows = self.cur.fetchall()

        points_x = []
        points_y = []

        for d in rows:
            points_x.append(d[1])
            points_y.append(d[0])

        plt.scatter(points_x, points_y)
        plt.show()

    def ajoutComboBox(self):

        self.cur.execute("SELECT compagnie_nom FROM compagnie")
        print("e")

        rows = self.cur.fetchall()

        for i in rows:
            self.vue.liste_compagnies.combo_total.addItem(i[0])

        self.cur.execute("SELECT pays_nom FROM pays")

        rows = self.cur.fetchall()

        for i in rows:
            self.vue.listes_pays.combo_total.addItem(i[0])

if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Controller()
    sys.exit(app.exec())