import tkinter as tk

#biblioteka zawierająca zmienne globalne

currentlyOpenedList = None  # obecnie otwarta lista

# tworzę framey. w lewej (1) ramce zamieszczam kolejno przyciski z listami. W prawej po kliknięciu pojawia się konkretna lista
f1 = tk.Frame(
    width=25,
    height=100,
    bd=1
)
f2 = tk.Frame(
    width=25,
    height=100,
    bd=5
)
# tworzenie przycisku zamykającego otwartą listę
closeListButton = tk.Button(
    f2,  # przypisanie do prawego framea
    text="zamknij obecną listę",
    width=25,
    height=1,
    command=lambda: currentlyOpenedList.closeList if currentlyOpenedList is not None else None #Nie działa?
)

listsList = []  # lista list - lista zawierająca listy zakupów