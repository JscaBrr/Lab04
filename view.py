import flet as ft

class View: #CLASS VIEW CON ATTRIBUTO CONTROLLER
    def __init__(self, page: ft.Page): #page istanza di Page
        #PAGINA, TITOLO
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++" #TODO, aprendo con view=ft.AppView.WEB_BROWSER --> non visualizzato
        self.__title = None  # UI element (inizializzato sarà istanza di ft.Text() dopo)
        #---------------------------------------------------------------#
        #LAYOUT, PROPRIETÁ VISIVE
        #horizontal_alignment è una property definita all'interno di quella classe.
        # self.page.horizontal_alignment = "LEFT"   # Allinea a sinistra
        # self.page.horizontal_alignment = "CENTER" # Allinea al centro
        # self.page.horizontal_alignment = "RIGHT"  # Allinea a destra
        # self.page.horizontal_alignment = None     # Nessun allineamento specifico (default)
        self.page.horizontal_alignment = 'CENTER' #Allinea orizzontalmente il contenuto della pagina al centro.
        # self.page.theme_mode = ft.ThemeMode.LIGHT  # Tema chiaro
        # self.page.theme_mode = ft.ThemeMode.DARK   # Tema scuro
        # self.page.theme_mode = ft.ThemeMode.SYSTEM # Segue il tema del sistema operativo
        self.page.theme_mode = ft.ThemeMode.LIGHT #Imposta il tema della pagina in modalità chiara (light mode).
        self.__theme_switch = None  # UI element (inizializzata sarà istanza di ft.Switch() dopo)
        # ---------------------------------------------------------------#
        self.__controller = None #istanza controller come attributo della View

    def setController(self, controller): #SETTER del controller per il main
        self.__controller = controller

    def update(self): #update per la page
        self.page.update()

        # define the UI elements and populate the page
    def theme_changed(self, e): #istruzioni per modificare l'interfaccia
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        #self.__txt_container.bgcolor = (
           #ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        #)
        self.page.update()

    def languageprint(self, e):
        """Stampa la lingua selezionata nel menu a tendina"""
        print(f"Selected language: {self.__languagedropdown.value}") #stampa nel Run

    def modalityprint(self, e):
        """Stampa la lingua selezionata nel menu a tendina"""
        print(f"Selected modality: {self.__modalitydropdown.value}") #stampa nel Run

    def textinput(self, e):
        print(f"Inputted text: {self.__txtIn.value}")  #stampa nel Run

    def spellcheck(self, e): #funzione che esegue -->  chiamata al controller
        # Esegui il controllo ortografico o altre azioni necessarie
        print(f"Checking spelling for: {self.__txtIn.value}")
        ti = self.__txtIn
        l = self.__languagedropdown.value #--> oggetto dizionario contiene set e dict
        m = self.__modalitydropdown.value
        p, t = self.__controller.handleSentence(ti, l, m) #assegna valore/i al return della funzione chiamata
        print(f"Parole errate: {p}")
        print(f"Tempo impiegato: {t} secondi")
        #VALORI RESTITUITI DAL CONTROLLER STAMPATI IN VIEW DALLA VIEW
        self.__resultlistview.controls = [ #E return --> aggiorna i controls della UI inizializzata in precedenza -> necessario update()
            ft.Text(f"Frase inserita: {self.__txtIn.value}"),
            ft.Text(f"Parole errate: {' '.join(p) if p else 'Nessuna'}"),
            ft.Text(f"Tempo impiegato: {t:.5f} secondi"),
        ]
        self.__txtIn.value = ""
        self.page.update()

    """TODO - (ISTRUZIONI PER STAMPA IN VIEW DAL CONTROLLER) METODI PER PASSAGGIO DI ATTRIBUTI AL CONTROLLER
        def get_text_input(self):
            return self.__txtIn.value
        def get_resultview(self):
            return self.__resultlistview
    """

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed) #() == (definizione delle @property: attributi che definiscono le caratteristiche di un widget)
        #l'elemento viene effettivamente aggiunto alla pagina a livello logico,
        # ma la UI non si aggiorna visivamente
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START))
        self.__controller.printMenu() #stampa nel Run
        self.__languagedropdown = ft.Dropdown(label="Select language",
                                              options=[
                                                  ft.dropdown.Option("English"),
                                                  ft.dropdown.Option("Italian"),
                                                  ft.dropdown.Option("Spanish"),],
                                              on_change=self.languageprint, #se non deve eseguire un algoritmo, chiamare la funzione che stampa output nel Run
                                              width=self.page.width)
        self.page.controls.append(
            ft.Row(
                controls=[self.__languagedropdown],
                alignment=ft.MainAxisAlignment.START
            )
        )
        self.__modalitydropdown = ft.Dropdown(label="Search Modality",
                                              options=[
                                                  ft.dropdown.Option("Contain"),
                                                  ft.dropdown.Option("Linear"),
                                                  ft.dropdown.Option("Dichotomic"),
                                              ],
                                              on_change=self.modalityprint, width=self.__languagedropdown.width * 0.25)
        self.__resultlistview = ft.ListView(
            width=self.page.width,
            controls=[]  # Inizialmente vuoto, aggiungeremo i risultati dinamicamente
        )
        self.__txtIn = ft.TextField(label="Add your sentence here:", on_change = self.textinput, autofocus = True,  width=self.__languagedropdown.width * 0.50 )
        self.__spellcheckbutton = ft.ElevatedButton(
            text="Spell Check",
            on_click=self.spellcheck,  #esecuzione di funzione interna (--> contiene chiamata al controller)
            width=self.__languagedropdown.width * 0.20
        )
        self.page.controls.append(
            ft.Row(
                controls=[self.__modalitydropdown, self.__txtIn, self.__spellcheckbutton],
                alignment=ft.MainAxisAlignment.START
            )
        )
        self.page.controls.append(self.__resultlistview)
        self.page.update()





