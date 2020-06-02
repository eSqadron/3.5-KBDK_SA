import tkinter as tk

#klasa- pojedyncza lista zakupów
class ShoppingList:
    def __init__(self, name):
        self.name_=name #nazwa tej konkretnej listy
        self.list_ = [] #zawartość tej listy (str)
        self.entryFields_ = [] #lista z polami Entry Field wyświetlanymi po prawej stronie
        self.newButton = None #zmienna w której zapisany jest przycisk dodającegy nowe pole do tej listy
        self.newEntry = None #zmienna w której zapisane jest pole tekstowe Entry Field do którego należy podać nazwę nowego pola


    #metoda wypisująca zawartość zmiennej list_
    def printList(self):
        global currentlyOpenedList #aby była używana globalna wersja zmiennej
        if currentlyOpenedList is not None: currentlyOpenedList.closeList() #zamyka obecnie otwartą listę zanim otworzy nową
        if currentlyOpenedList is None: #może coś wyświetlić tylko jeżeli nic nie jest wyświetlone
            currentlyOpenedList = self #przypisuje siebie jako otawrta liste
            while "" in self.list_: self.list_.remove("") #czyszczenie listy z pustych elementów
            #pętla wypisująca wszystkie wartości z list_ do poszczególnych pól entry
            for j in self.list_:
                w = tk.Entry(   #tworzy pola typu entry w których są nazwy produktów
                    f2,
                    width=25
                )
                w.insert(0, j)
                w.pack(side=tk.TOP)
                self.entryFields_.append(w) #dodaje te pola do listy aby potem dało się je usunac
            ##############
            
            #pole tekstowe odpowiedzialne za zebranie nazwy nowego porduktu
            self.newEntry = tk.Entry(
                f2,
                width=25
            )
            self.newEntry.insert(0, "Podaj nazwę nowego produktu")
            self.newEntry.pack(side=tk.BOTTOM)
            ############

            #przycisk odpowiedzialny za dodawnia nowego produktu
            self.newButton = tk.Button(
                f2,
                width=25,
                height=1,
                text="dodaj produkt",
                command=lambda: self.addProduct(self.newEntry.get())
            )
            self.newButton.pack(side=tk.BOTTOM)
            ##########

    #metoda dodająca nowy produkt do listy
      def addProduct(self, productName):
        self.list_.append(productName)
        if self == currentlyOpenedList:
            self.printList()
            
            
    #metoda zamykająca obecnie otwartą listę
    def closeList(self):
        pass

    #metoda zapisująca obecnie otwartą listę do listy list
    def saveList(self):
        pass

    #Zamiast 4 powyższych metod można zaimplementować funkcje printCurrentlyOpenedList(), addProductToCurrentlyOpenedList(), closeCurrentlyOpenedList() i saveCurrentlyOpenedList().
    #Jeżeli projekt który mam w głowie okaże się niemożliwy do wykonania może się to w niektórych przypadkach okazać konieczne. Lub po prostu tak może być łatwiej.





#zmienne gloablne używane WSZĘDZIE
listsList=[] #lista list - lista zawierająca listy zakupów

currentlyOpenedList = None #obecnie otwarta lista


#testowa lista zakupów
listsList.append(ShoppingList("testowaLista"))
listsList[0].list_.append("zakup 1")
listsList[0].list_.append("zakup 2")
listsList[0].list_.append("zakup 3")
listsList[0].list_.append("zakup 4")


listsNum=len(listsList) #obecna ilosc list



###########
#FUNCTIONS
#Funkcje operujące na liście wszystkich list zakupów (działające na lewej połówce ekranu, przypsiane do f1)

#funkcja tworząca przycisk służący do tworzenia nowych list i pole tekstowe typu entry gdzie trzeba podać nazwę nowej listy
def createNewListButton():
    global newListButton #aby do obu pól można było się odwoływać gdzie indziej muyszą byc globalne
    global entry

    # pole do wpisania tytułu nowej listy
    entry = tk.Entry(
        f1, #f1 przypisuje ten przycisk do ramki1
        width=25
    )
    entry.insert(0, "Podaj nazwę nowej listy") #insert "wkłada" bazowy tekst do pola entry
    entry.pack() #"pakuje" pole aby było odpowiednio wyświetlane w ramce

    # przycisk, po kliknięciu którego dodaje się lista o tytule wpisanym w entry
    newListButton = tk.Button(
        f1,
        text="utworz liste",
        width=25,
        height=3,
        command=newList #command to funkcja która ma być wywołana po kliknięciu przycisku. MUSI być bez (), inaczej funkcja wykona się przy interpretacji kodu, a nie przy klinkięciu.
    )
    newListButton.pack()

#funkcja tworząca przycisk służący do wyszukiwania list z listy i pole tekstowe typu entry gdzie trzeba podać nazwę wyszukiwanej listy
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
    )
    searchButton.pack()


#tworzenie nowej listy, wraz z przyciskiem, dodaniem przycisku do tablicy przycisków itp
def newList():
    global listsNum 
    newListInstance = ShoppingList(entry.get()) #zbieram z pola entry (funkcja createNewListButton() odpowiada za tworzenie tego pola) nazwę nowej listy

    #przycisk do wyświetlania nowo utworzonej listy
    listButton = tk.Button(
        f1,
        text=newListInstance.name_,
        width=25,
        height=2,
        command = newListInstance.printList
    )
    listButton.pack()


    listsList.append(newListInstance) #dodaje do tablicy z listami zakupów nową listę
    listsNum = len(listsList) #zwiększa ilość zapisanych list



#############



#tworzy okno, chyba, wiem że musi być
root=tk.Tk()


#tworzę framey. w lewej (1) ramce zamieszczam kolejno przyciski z listami. W prawej po kliknięciu pojawia się konkretna lista
f1 = tk.Frame(
    width = 25,
    height = 100,
    bd = 1
)
f1.pack(side = tk.LEFT)
f2 = tk.Frame(
    width = 25,
    height = 100,
    bd = 5
)
f2.pack(side = tk.LEFT)


#tworzenie przycisku zamykającego otwartą listę
closeListButton = tk.Button(
    f2, #przypisanie do prawego framea
    text="zamknij obecną listę",
    width=25,
    height=1,
    command=lambda: currentlyOpenedList.closeList if currentlyOpenedList is not None else None #jeżeli ktoś zamiast metody closeList zdecyduje się zaimplementować funkcję closeCurrentlyOpenedList należy zamienić tą linijkę na command=closeCurrentlyOpenedList
)
closeListButton.pack(side = tk.TOP, anchor = tk.N)





#funkcja tworząca przycisk tworzący nową listę i pole do wpisania jej nazwy - możnaby całą funckjonalność tej funkcji umieścić tutaj, nie musi być funkcji
createNewListButton()
createSearchBarButton() #pole do wyszukiwania list - same as above



#pętla zbierająca istniejace listy z talicy listsList i tworząca przyciski do nich stworzona w celach testowych - trzeba będzie to przenieść do funkcji wczytującej z pliku
for i in listsList:
    listButton = tk.Button(
        f1,
        text=i.name_,
        width=25,
        height=2,
        command = i.printList
    )
    listButton.pack()


root.mainloop()
