import tkinter as tk
import tkinter.filedialog
from typing import Optional
from ShoppingListErrors import ListAmountError, ListElementsAmountError, ListNameAlreadyTakenError, ListNameLengthError


class ShoppingList:
    def __init__(self, name):
        self.name_ = name  # nazwa tej konkretnej listy
        self.list_ = []  # zawartość tej listy (str)
        self.entryFields_ = []  # lista z polami Entry Field wyświetlanymi po prawej stronie
        self.newButton = None  # zmienna w której zapisany jest przycisk dodającegy nowe pole do tej listy
        self.newEntry = None  # zmienna w której zapisane jest pole tekstowe Entry Field do którego należy podać nazwę nowego pola
        self.maxNameLen = 25  # zmienna dodana, aby w łatwy sposób umożliwić późniejsze zmienianie limitu długości nazw

        # sprawdzenie, czy nazwa nie jest za długa
        if len(name) > self.maxNameLen:
            raise ListNameLengthError(self)

        # sprawdzenie, czy nazwa listy jest zajęta
        for i in listsList:
            if name in i.name_:
                raise ListNameAlreadyTakenError(self)

    # metoda wypisująca zawartość zmiennej list_
    def printList(self):
        global currentlyOpenedList  # aby była używana globalna wersja zmiennej
        if currentlyOpenedList is not None: currentlyOpenedList.closeList()  # zamyka obecnie otwartą listę zanim otworzy nową
        if currentlyOpenedList is None:  # może coś wyświetlić tylko jeżeli nic nie jest wyświetlone
            currentlyOpenedList = self  # przypisuje siebie jako otawrta liste
            while "" in self.list_: self.list_.remove("")  # czyszczenie listy z pustych elementów
            # pętla wypisująca wszystkie wartości z list_ do poszczególnych pól entry
            for j in self.list_:
                w = tk.Entry(  # tworzy pola typu entry w których są nazwy produktów
                    f2,
                    width=25
                )
                w.insert(0, j)
                w.pack(side=tk.TOP)
                self.entryFields_.append(w)  # dodaje te pola do listy aby potem dało się je usunac
            ##############

            # pole tekstowe odpowiedzialne za zebranie nazwy nowego porduktu
            self.newEntry = tk.Entry(
                f2,
                width=25
            )
            self.newEntry.insert(0, "Podaj nazwę nowego produktu")
            self.newEntry.pack(side=tk.BOTTOM)
            ############

            # przycisk odpowiedzialny za dodawnia nowego produktu
            self.newButton = tk.Button(
                f2,
                width=25,
                height=1,
                text="dodaj produkt",
                command=lambda: self.addProduct(self.newEntry.get())
            )
            self.newButton.pack(side=tk.BOTTOM)
            ##########

    # metoda dodająca nowy produkt do listy
    def addProduct(self, productName):

        # sprawdzenie czy ilość produktów nie przekracza maksymalnej
        if len(self.list_) > 20:
            raise ListElementsAmountError(self)

        self.list_.append(productName)
        if self == currentlyOpenedList:
            self.printList()

    # metoda zamykająca obecnie otwartą listę
    def closeList(self):
        global currentlyOpenedList
        isShowed = False
        self.saveList()
        for i in self.entryFields_:
            i.destroy()
        self.newButton.destroy()
        self.newEntry.destroy()
        self.entryFields_.clear()
        currentlyOpenedList = None

    # metoda zapisująca obecnie otwartą listę do listy list
    def saveList(self):
        global currentlyOpenedList
        for i in range(len(self.entryFields_)):
            self.list_[i] = (self.entryFields_[i]).get()


#########################################
# FUCTIONS

# funkcja tworząca przycisk służący do tworzenia nowych list i pole tekstowe typu entry gdzie trzeba podać nazwę nowej listy
def createNewListButton():
    global newListButton  # aby do obu pól można było się odwoływać gdzie indziej muyszą byc globalne
    global entry

    # pole do wpisania tytułu nowej listy
    entry = tk.Entry(
        f1,  # f1 przypisuje ten przycisk do ramki1
        width=25
    )
    entry.insert(0, "Podaj nazwę nowej listy")  # insert "wkłada" bazowy tekst do pola entry
    entry.pack()  # "pakuje" pole aby było odpowiednio wyświetlane w ramce

    # przycisk, po kliknięciu którego dodaje się lista o tytule wpisanym w entry
    newListButton = tk.Button(
        f1,
        text="utworz liste",
        width=25,
        height=3,
        command=newList
        # command to funkcja która ma być wywołana po kliknięciu przycisku. MUSI być bez (), inaczej funkcja wykona się przy interpretacji kodu, a nie przy klinkięciu.
    )
    newListButton.pack()


# funkcja tworząca przycisk służący do wyszukiwania list z listy i pole tekstowe typu entry gdzie trzeba podać nazwę wyszukiwanej listy
def createSearchBarButton():
    global searchButton
    global searchEntry

    searchEntry = tk.Entry(
        f1,
        width=25
    )
    searchEntry.insert(0, "podaj szukaną frazę")
    searchEntry.pack()

    searchButton = tk.Button(
        f1,
        text="wyszukaj",
        width=25,
        height=3,
        command=openSearchedList
    )
    searchButton.pack()


def openSearchedList():
    found = False
    for i in listsList:
        if i.name_ == searchEntry.get():
            found = True
            i.printList()
    if not found:
        searchEntry.delete(0, tk.END)
        searchEntry.insert(0, "brak takiej listy")


# tworzenie nowej listy, wraz z przyciskiem, dodaniem przycisku do tablicy przycisków itp
def newList():
    global listsNum

    # sprawdzenie czy ilosc list nie przekracza maksymalnej
    if listsNum >= 20:
        raise ListAmountError(listsNum)

    newListInstance = ShoppingList(
        entry.get())  # zbieram z pola entry (funkcja createNewListButton() odpowiada za tworzenie tego pola) nazwę nowej listy

    # przycisk do wyświetlania nowo utworzonej listy
    listButton = tk.Button(
        f1,
        text=newListInstance.name_,
        width=25,
        height=2,
        command=newListInstance.printList
    )
    listButton.pack()

    listsList.append(newListInstance)  # dodaje do tablicy z listami zakupów nową listę
    listsNum = len(listsList)  # zwiększa ilość zapisanych list


# funkcja używana w opcji menu górnego poziomego "Zapisz", służąca zapisowi do pliku
def saveToFile():
    file = tk.filedialog.asksaveasfile(mode="w",filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    for i in listsList:
        file.write("**" + i.name_ + '\n')


# funkcja używana w opcji menu górnego poziomego "Wczytaj", służąca wczytywaniu z pliku
def readFromFile():
    pass


def onClosingEvent():
    popup = tk.messagebox.askyesnocancel(title="Quit", message="Do you want to save before closing?")
    if popup:
        saveToFile()
        root.destroy()
    elif popup is not None:
        root.destroy()
    elif popup is None:
        pass

############################
# variables

currentlyOpenedList: Optional[ShoppingList] = None  # obecnie otwarta lista
root = tk.Tk()  # głowne okno

# tworzę framey. w lewej (1) ramce zamieszczam kolejno przyciski z listami. W prawej po kliknięciu pojawia się konkretna lista
f1 = tk.Frame(
    root,
    width=25,
    height=100,
    bd=1
)
f2 = tk.Frame(
    root,
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
    command=lambda: currentlyOpenedList.closeList() if currentlyOpenedList is not None else None  # Nie działa?
)

listsList = []  # lista list - lista zawierająca listy zakupów
listsNum = 0

# Menu górne
menu = tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="Zapisz", command=saveToFile)
menu.add_command(label="Wczytaj", command=readFromFile)
