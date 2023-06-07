# --- import
import json
# ---------------------------------
# --- class Requete
# ---------------------------------
class Requete:
    # constructor
    def __init__(self, req : str, graph : str, analyse : str, explication : str) -> None: 
        
        self.__req : str = req
        self.__graph : str = graph
        self.__analyse : str = analyse
        self.__explication : str = explication
    
    def __repr__(self) -> str:
        res = ""
        res += "Requete :  " + self.__req + "\n"
        res += "Graph :  " + self.__graph + ".png\n"
        res += "Analyse :  " + self.__analyse + "\n"
        res += "Explication :  " + self.__explication + "\n"
        return res

    @property
    def req(self) -> str: return self.__req
    @req.setter
    def req(self, req :str) -> None: self.__req = req[0].upper()+req[1:].lower()  

    @property
    def graph(self) -> str: return self.__graph
    @graph.setter
    def graph(self, graph :str) -> None: self.__graph = graph[0:].lower() 
    
    @property
    def analyse(self) -> str: return self.__analyse
    @analyse.setter
    def analyse(self, analyse :str) -> None: self.__analyse = analyse[0].upper()+analyse[1:].lower()  

    @property
    def explication(self) -> str : return self.__explication
    @explication.setter
    def explication(self, explication : str) : self.__explication = explication

    # toJSON
    def toJSON(self) -> str:
        dictP = {
            'requete'  : self.__req,
            'graph' : self.__graph,
            'analyse' : self.__analyse,
            'explication' : self.__explication
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
    def new(): return Requete("Req", "graph", "analyse", "explication") 

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
