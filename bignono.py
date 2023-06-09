# --- import
import json, copy, os, requete

# -------------------------------------------------
# --- class Annuaire
# -------------------------------------------------
class Bignono:
    # constructor
    def __init__(self, jsonFile : (str|None) = None) -> None:
        # attributs
        self.listRequete : list[requete.Requete] = []
        self.current : (int|None) = 1
        
        # si un fichier est fourni : on charge 
        if jsonFile: self.open(jsonFile)


    def getCurrent(self) -> int | None : return self.current

    def setCurrent(self, index :int|None) -> None : self.current = index

    def update(self,r: requete.Requete) -> None:
        requ = self.getRequete()
        if requ:
            requ.requete = copy.deepcopy(r.requete)
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
                    self.listRequete.append(requ)
                print(f'{len(self.listRequete)} requêtes trouvées')
                self.current = 0 if self.listRequete else None

    def save(self,jsonFile : str) -> None:
        print(f'saving file: {jsonFile}', end='... ')

        if not  os.path.exists(jsonFile): 
            f = open(jsonFile, "x"); f.close()

        with open(jsonFile, "w", encoding='utf-8') as file: 
            d : dict= {} 
            listRequete : list= []
            for p in self.listRequete :listRequete.append(json.loads(p.toJSON()))
            d['dico'] = listRequete
            json.dump(d,file,ensure_ascii=False)
        print(f'done!')



    def getRequetebyReq(self, req: str) -> (requete.Requete|None):
        searchList : list[str] = list(map(lambda x: x.requete.lower(), self.listRequete))
        return self.listRequete[searchList.index(req.lower())]
    
    def addRequete(self, r : requete.Requete, index : int|None = None) -> None :
        if not isinstance(index, int) or not isinstance(self.current, int):
            self.listRequete.append(r)
            self.current = len(self.listRequete) -1 if len(self.listRequete) != 0 else None
        else:
            self.listRequete.insert(self.current,r)


    def next(self) -> None :
        if self.current != None :
            self.current = (self.current +1)% len(self.listRequete) 
    
    def previous(self) -> None :
        if self.current != None :
            self.current = (self.current - 1)% len(self.listRequete)

    def getRequete(self) -> requete.Requete| None : 
        if self.current != None: return self.listRequete[self.current]  
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