import flet as ft
import string
import time
from dictionary import Dictionary

class SpellChecker: #CLASS CONTROLLER IMPORTA MODEL (CLASS DI LOGICA e DATI) > CHE IMPORTANO ALTRE CLASS DI LOGICA
                    #CLASS CONTROLLER IMPORTA+ATTR. MODEL + (VIEW <-> NECESSARIO)+ OGG. DIZIONARIO

    def __init__(self, view, model):
        self._Dictionary = None
        #self._multiDic = model.multiDictionary()
        self._model = model
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        self._Dictionary = Dictionary(language) #l'oggetto è già nel costruttore
        self._model.dizionario = self._Dictionary
        #self._multiDic.dizionario = self._Dictionary #m = self._multiDic non serve passarlo, è già nel costruttore
        listatxt = replaceChars(txtIn)
        paroleErrate = "-"
        match modality:
            case "Contain":
                t1 = time.time()
                paroleErrate = self._model.searchWord(listatxt)
                t2 = time.time()

                """TODO - ISTRUZIONI PER STAMPA IN VIEW DAL CONTROLLER + STAMPA NEL RUN (MAIN) 
                self._view.get_resultview().controls = [ #E return --> aggiorna i controls della UI inizializzata in precedenza -> necessairo update()
                    ft.Text(f"Frase inserita: {self._view.get_text_input()}"),
                    ft.Text(f"Parole errate: {' '.join(paroleErrate) if paroleErrate else 'Nessuna'}"),
                    ft.Text(f"Tempo impiegato: {t2-t1:.5f} secondi"),
                        ]
                print("<Controller>: stampa nella view eseguita")"""

                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                paroleErrate = self._model.searchWordLinear(listatxt)
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                paroleErrate = self._model.searchWordLinear(listatxt)
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

def replaceChars(testo):
    testo = testo.value.lower()
    testo = testo.translate(str.maketrans("", "", string.punctuation)).strip()
    listatesto = testo.split(" ")
    return listatesto