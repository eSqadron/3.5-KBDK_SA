#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib import *
from lib_var import *


def main():
    # tworzy okno, chyba, wiem że musi być
    root = tk.Tk()

    menu = tk.Menu(root)
    root.config(menu=menu)
    menu.add_command(label="Zapisz", command=saveToFile)
    menu.add_command(label="Wczytaj", command=readFromFile)

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

    # Menu górne poziome

    root.mainloop()


if __name__ == "__main__":
    main()
