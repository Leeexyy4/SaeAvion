import sys, Vue
import psycopg2
import matplotlib.pyplot as plt
from test_requete import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QDateEdit, QFileDialog, QRadioButton, QCheckBox
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets


class Controller():
    def __init__(self) -> None:
        self.DB_NAME = "saeavion"
        self.DB_USER = "emma"
        self.DB_PASS = "0111"
        self.DB_HOST = "172.28.144.1"
        self.DB_PORT = "5432"

        self.vue = Vue.Interface()

        self.vue.infos_pays.envoiCommande.connect(self.Commande)
 
    def Commande(self, requete):

        print(requete)

        try:
            conn = psycopg2.connect(database=self.DB_NAME,
                                    user=self.DB_USER,
                                    password=self.DB_PASS,
                                    host=self.DB_HOST,
                                    port=self.DB_PORT)
            print("Database connected successfully")
        except:
            print("Database not connected successfully")

        cur = conn.cursor()


        #cur.execute("SELECT COUNT(aeroport_id) FROM routes r, aeroport a, pays p WHERE r.aeroport_arr_id=a.aeroport_id AND p.pays_id = a.pays_id AND pays_nom ILIKE 'germany'")
        #cur.execute(requete)
        cur.execute("SELECT latitude, longitude FROM aeroport WHERE type LIKE 'airport' AND pays_id=(SELECT pays_id FROM pays WHERE pays_nom ILIKE 'FRANCE')")

        
        rows = cur.fetchall()

        points_x = []
        points_y = []

        for d in rows:
            points_x.append(d[1])
            points_y.append(d[0])

        plt.scatter(points_x, points_y)
        plt.show()

if __name__ == "__main__":
    print(f'main')
    app = QApplication(sys.argv)
    f = Controller()
    sys.exit(app.exec())