#utilizzo di flet: https://flet.dev/docs
#Flet è una libreria Python che permette di creare applicazioni
# con interfacce utente (UI) moderne e reattive,
# senza la necessità di scrivere codice JavaScript o HTML.
import flet as ft
from controller import SpellChecker #il main importa controller
from view import View #il main importa view
from model import Model #il main importa model

#no classi, 1 funzione
def main(page: ft.Page): #definizione funzione del main
    # Setup model, view, control according to MVC pattern
    v = View(page) #istanza di View
    m = Model() #istanza di Model
    controller = SpellChecker(v, m) #istanza di Controller
    v.setController(controller) #passare il Controller alla View
    v.add_content() #funzione per UI

ft.app(target=main)