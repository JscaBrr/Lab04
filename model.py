import datetime
import richWord

class Model: #CLASS MODEL IMPORTA CLASS DI DATI

    def __init__(self):
       self.dizionario = None

    #def printDic(self):
        #print
        #assert isinstance(self.dizionario, object)
        #self.dizionario

    def searchWord(self, listatxt):
        start = datetime.datetime.now()
        errors = []
        for i in listatxt:
            r = richWord.RichWord(i)
            if i not in self.dizionario.setdizionario:
                errors.append(i)
            else:
                r.esito = True
        end = datetime.datetime.now()
        print(f"tempo impiegato: {end-start}")
        if errors:
            return errors

    def searchWordLinear(self, listatxt):
        errors = []
        for i in listatxt:
            r = richWord.RichWord(i)
            for k in self.dizionario.setdizionario:
                if i == k:
                    r.esito = True
            if not r.esito:
                errors.append(i)
        if errors:
            return errors

    def searchWordDichotomic(self, listatxt):
        start = datetime.datetime.now()
        errors = []
        for i in listatxt:
            r = richWord.RichWord(i)
            setordinato = sorted(self.dizionario.setdizionario)
            sx = 0
            dx = len(setordinato) - 1
            while sx <= dx:
                centro = (sx+dx)//2
                p = setordinato[centro]
                if i == p:
                    r.esito = True
                    break
                elif i < p:
                    dx = centro - 1
                else:
                    sx = centro + 1
            if not r.esito:
                errors.append(i)
        end = datetime.datetime.now()
        print(f"tempo impiegato: {end - start}")
        if errors:
            return errors