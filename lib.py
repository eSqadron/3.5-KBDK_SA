#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from lib_var import f1, listsList
from shopping_list_class import ShoppingList

##biblioteka zawierająca funkcje

# Funkcje operujące na liście wszystkich list zakupów (działające na lewej połówce ekranu, przypsiane do f1)

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
    pass


# funkcja używana w opcji menu górnego poziomego "Wczytaj", służąca wczytywaniu z pliku
def readFromFile():
    pass
