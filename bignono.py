# --- import
import json, copy, os, requete

# -------------------------------------------------
# --- class Annuaire
# -------------------------------------------------
class Bignono:
    # constructor
    def __init__(self, jsonFile : (str|None) = None) -> None:
        # attributs
        self.__listRequete : list[requete.Requete] = []
        self.__current : (int|None) = None
        
        # si un fichier est fourni : on charge 
        if jsonFile: self.open(jsonFile)

    @property
    def current(self) -> int | None : return self.__current
    @current.setter
    def current(self, index :int|None) -> None : self.__current = index

    def update(self,r: requete.Requete) -> None:
        requ = self.getRequete()
        if requ:
            requ.req = r.req
            requ.graph = copy.deepcopy(r.graph)
            requ.analyse = copy.deepcopy(r.analyse)
            requ.explication = copy.deepcopy(r.explication)



    def open(self, jsonFile : str) -> None:
        with open(jsonFile, encoding='utf-8') as file:
            print(f'loading file: {jsonFile}', end='... ')
            js = json.load(file) 
            if  'dico' in js.keys():
                listRequete = js['dico']
                for p in listRequete:  
                    requ = requete.Requete.buildFromJSon(p) 
                    self.__listRequete.append(requ)
                print(f'{len(self.__listRequete)} requêtes trouvées')
                self.__current = 0 if self.__listRequete else None

    def save(self,jsonFile : str) -> None:
        print(f'saving file: {jsonFile}', end='... ')

        if not  os.path.exists(jsonFile): 
            f = open(jsonFile, "x"); f.close()

        with open(jsonFile, "w", encoding='utf-8') as file: 
            d : dict= {} 
            listRequete : list= []
            for p in self.__listRequete :listRequete.append(json.loads(p.toJSON()))
            d['dico'] = listRequete
            json.dump(d,file,ensure_ascii=False)
        print(f'done!')



    def getRequetebyReq(self, req: str) -> (requete.Requete|None):
        searchList : list[str] = list(map(lambda x: x.req.lower(), self.__listRequete))
        return self.__listRequete[searchList.index(req.lower())]
    
    def addRequete(self, r : requete.Requete, index : int|None = None) -> None :
        if not isinstance(index, int) or not isinstance(self.__current, int):
            self.__listRequete.append(r)
            self.current = len(self.__listRequete) -1 if len(self.__listRequete) != 0 else None
        else:
            self.__listRequete.insert(self.__current,r)


    def next(self) -> None :
        if self.__current != None :
            self.__current = (self.__current +1)% len(self.__listRequete) 
    
    def previous(self) -> None :
        if self.__current != None :
            self.__current = (self.__current - 1)% len(self.__listRequete)

    def getRequete(self) -> requete.Requete| None : 
        if self.__current != None: return self.__listRequete[self.__current]  
        else: return None

# --- main: kind of unit test
if __name__ == "__main__" :
    print('TEST: class bigbigbigbigbigbigbig Nnnnoooooowwwwnnnnnnnnnnooooowwwwwwwwwwwwwww')
    reqqq : requete.Requete= requete.Requete('Cmb de pet par heure xd', 'Pipiprout.png', "Lol un prout ", "Famous prout xd") 
    bignono : Bignono = Bignono()
    bignono.addRequete(reqqq)
    print("\ttesting add,getbyName:", end= ' ')
    print(bignono.getRequetebyReq("Cmb de pet par heure xd")) 

    print("\ttesting from json:", end= ' ')
    annuaireJS : Bignono = Bignono('dico.json')