# --- import
import json
# ---------------------------------
# --- class Requete
# ---------------------------------
class Requete:
    # constructor
    def __init__(self, requete : str, graph : str, analyse : str, explication : str) -> None: 
        
        self.requete : str = requete
        self.graph : str = graph
        self.analyse : str = analyse
        self.explication : str = explication
    
    def __repr__(self) -> str:
        res = ""
        res += "Requete :  " + self.requete + "\n"
        res += "Graph :  " + self.graph + "\n"
        res += "Analyse :  " + self.analyse + "\n"
        res += "Explication :  " + self.explication + "\n"
        return res


    def getReq(self) -> str: return self.requete

    def setReq(self, req :str) -> None: self.requete = req[0].upper()+req[1:].lower()  

    def getGraph(self) -> str: return self.graph

    def setGraph(self, graph :str) -> None: self.graph = graph[0:].lower() 
    
    def getAnalyse(self) -> str: return self.analyse
    
    def setAnalyse(self, analyse :str) -> None: self.analyse = analyse[0].upper()+analyse[1:].lower()  

    def getExplication(self) -> str : return self.explication
    
    def setExplication(self, explication : str) : self.explication = explication

    # toJSON
    def toJSON(self) -> str:
        dictP = {
            'requete'  : self.requete,
            'graph' : self.graph,
            'analyse' : self.analyse,
            'explication' : self.explication
        }
        return json.dumps(dictP,ensure_ascii=False)

    # buildFromJson
    @staticmethod
    def buildFromJSon(d: dict):
        # Requete
        requete : str =  d['requete']
        # prenom
        graph :str =  d['graph'] 
        #analyse
        analyse : str =  d['analyse'] 
        #explication
        explicaton : str = d['explication']


        return Requete(requete, graph, analyse, explicaton)

    # new
    @staticmethod
    def new(): return Requete("requete", "graph", "analyse", "explication") 

# --- main: kind of unit test
if __name__ == "__main__" :
    print('TEST: class Requete')
    print('\t création de Requete',  end=': ')
    a : Requete = Requete("", '"non"', "", "C'est un pilote !")
    b : Requete = Requete.new()
    print(' done!')
    print(a.toJSON())
    print(b.toJSON())
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print(repr(a))
