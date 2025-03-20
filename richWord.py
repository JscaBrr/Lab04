class RichWord:
    def __init__(self, parola):
        self._parola = parola
        self._esito = None

    @property
    def esito(self):
        print("getter of parola called" )
        return self._esito
    @esito.setter
    def esito(self, boolValue):
        print("setter of parola called" )
        self._esito = boolValue

    def __str__(self):
        return self._parola