#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk

from lib_var import f2, currentlyOpenedList #problem z importem?


class ShoppingList:
    def __init__(self, name):
        self.name_ = name  # nazwa tej konkretnej listy
        self.list_ = []  # zawartość tej listy (str)
        self.entryFields_ = []  # lista z polami Entry Field wyświetlanymi po prawej stronie
        self.newButton = None  # zmienna w której zapisany jest przycisk dodającegy nowe pole do tej listy
        self.newEntry = None  # zmienna w której zapisane jest pole tekstowe Entry Field do którego należy podać nazwę nowego pola

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


