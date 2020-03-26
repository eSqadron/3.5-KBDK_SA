import tkinter as tk

#zmienne gloablne używane WSZĘDZIE
listsList=[] #lista zawierająca nazwy list
listsNum=len(listsList) #obecna ilosc list
listsNumMax=3 #maksymalna ilość list, obecnie ustawiona na 3 w celach testowych, normalnie to bedzie ze 100 czy coś

###########
#FUNCTIONS
#funkcja tworząca przycisk służący do tworzenia nowych list
def createNewListButton():
    global newListButton #aby do obu pól można było się odwoływać gdzie indziej muyszą byc globalne
    global entry
    # pole do wpisania tytułu nowej listy
    entry = tk.Entry(
        width=25
    )
    entry.insert(0, "Podaj nazwę nowej listy")
    entry.pack()
    #tworzę sam przycisk
    newListButton = tk.Button(
        text="utworz liste",
        width=25,
        height=4,
        command=newList
    )
    newListButton.pack()
    limitCheck()

#sprawdzenie czy został osiągnięty limi
def limitCheck():
    # jezeli jest za duzo list opcja tworzenia list ma byc wylaczona
    if listsNum >= listsNumMax:
        newListButton['text'] = "limit list przekroczony"
        newListButton['state'] = tk.DISABLED


#tworzenie nowej listy, wraz z przyciskiem, dodaniem nazwy do tabeli nazw itp
def newList():
    global listsNum #gloabal aby używał oryginalnej globalnej zmiennej a nie lokalnej kopii
    newListName = entry.get() #zbieram z pola entry nazwę nowej listy
    #przycisk do tworzenia nowej listy
    listButton = tk.Button(
        text=newListName,
        width=25,
        height=2
    )

    listButton.pack()
    #odpinam od okna przycisk nowej listy i pole do wpisywania tytułu nowej listy aby później podpiąć je poniżej
    entry.pack_forget()
    entry.pack()
    newListButton.pack_forget()
    newListButton.pack()

    listsList.append(newListName) #dodaje do tablicy nazw list nową nazwę
    listsNum = len(listsList)
    limitCheck() #sprawdzam czy osiągnięto limi list



#############

root=tk.Tk()

"""
#pętla zbierająca istniejace listy z talicy listsList i tworząca przyciski do nich stworzona w celach testowych
for i in listsList:
    listButton = tk.Button(
        text=i,
        width=25,
        height=2
    )
    listButton.pack()
*/
"""
#tworzę przycisk tworzący nową listę
createNewListButton()

root.mainloop()
