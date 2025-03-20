class Dictionary:
    def __init__(self, lingua):
        self.lingua = lingua
        self.setdizionario = set()
        self._dictdizionario = {}
        self.loadDictionary(f"resources/{lingua}.txt")

    def loadDictionary(self,filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                # self.setdizionario = set(line.strip().lower() for line in file)
                for line in file:
                    w = line.strip().lower()
                    self.setdizionario.add(w)
                    if w[0] in self.dictdizionario:
                        self.dictdizionario[w[0]].append(w)
                    else:
                        self.dictdizionario[w[0]] = [w]
        except FileNotFoundError:
            print(f"Errore: dizionario per {self.lingua} non trovato.")

    def printAll(self):
        for value in self._dict:
            print(f" {value}")

    @property
    def dictdizionario(self):
        return self._dictdizionario