#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib import *


def main():
    # testowa lista zakupów
    listsList.append(ShoppingList("testowaLista"))
    listsList[0].list_.append("zakup 1")
    listsList[0].list_.append("zakup 2")
    listsList[0].list_.append("zakup 3")
    listsList[0].list_.append("zakup 4")
    listsNum = len(listsList)

    f1.pack(side=tk.LEFT)
    f2.pack(side=tk.LEFT)
    closeListButton.pack(side=tk.TOP, anchor=tk.N)
    tk.Label(
        f1,
        text="Tworzenie nowej listy:"
    ).pack()
    # funkcja tworząca przycisk tworzący nową listę i pole do wpisania jej nazwy
    createNewListButton()
    tk.Label(
        f1,
        text="Wyszukiwarka:"
    ).pack()
    createSearchBarButton()  # pole do wyszukiwania list - same as above
    tk.Label(
        f1,
        text="lista list zakupów:"
    ).pack()

    # pętla zbierająca istniejace listy z talicy listsList i tworząca przyciski do nich stworzona w celach testowych - trzeba będzie to przenieść do funkcji wczytującej z pliku
    for i in listsList:
        listButton = tk.Button(
            f1,
            text=i.name_,
            width=25,
            height=2,
            command=i.printList
        )
        listButton.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
