import tkinter as tk
###########
#FUNCTIONS
def newList():
    listButton = tk.Button(
        text=newListName,
        width=25,
        height=2
    )
    listButton.pack()

#############
root=tk.Tk()

listsList=["pierwsza list", "druga"] #lista zawierająca nazwy list
listsNum=len(listsList) #obecna ilosc list
listsNumMax=4 #maksymalna ilość list



#pętla zbierająca istniejace listy z talicy listsList
for i in listsList:
    listButton = tk.Button(
        text=i,
        width=25,
        height=2
    )
    listButton.pack()

#pole do wpisania tytułu nowej listy
entry = tk.Entry(
    width=25
)
entry.insert(0, "a default value")
entry.pack()
newListName = entry.get()
#tworzę przycisk tworzący nową listę
newListButton = tk.Button(
    text="utworz liste",
    width=25,
    height=4,
    command=newList
)
newListButton.pack()

#jezeli jest za duzo list opcja tworzenia list ma byc wylaczona, trzeba to przerobic do funkcji, tak aby wywoływało się też po dodaniu nowej listy
if listsNum>=listsNumMax:
    newListButton['text']="limit list przekroczony"
    newListButton['state']=tk.DISABLED





#frame = tk.Frame()
#frame.pack()


root.mainloop()
