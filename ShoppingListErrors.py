#!/usr/bin/python
# -*- coding: utf-8 -*-
from lib import *
import tkinter as tk
from tkinter import messagebox


class ListError(Exception):
    """Podstawowa klasa wyjątku rzucana przez listy"""

    def __init__(self, msg=None):
        if msg is None:
            msg = "Wystąpił problem z listą zakupów"
        super().__init__(msg)


class ListAmountError(ListError):
    """Zbyt wiele list"""

    def __init__(self, listsNum):
        super().__init__(
            msg=f"Ilość list: {listsNum} przekracza maksymalną")

        tk.messagebox.showerror(
            title="ListAmountError",
            message=f"Ilość list: {listsNum} przekracza maksymalną")


class ListElementsAmountError(ListError):
    """Zbyt wiele pozycji na liście"""

    def __init__(self, currentList):
        super().__init__(msg=f"Ilość produktów: {len(currentList.list_)} przekracza maskymalną")

        tk.messagebox.showerror(
            title="ListElementsAmountError",
            message=f"Ilość produktów: {len(currentList.list_)} przekracza maksymalną")


class ListNameLengthError(ListError):
    """Nazwa listy zbyt długa"""

    def __init__(self, currentList):
        super().__init__(
            msg=f"Ilość znaków w nazwie: {len(currentList.name_)} przekracza maksymalną: {currentList.maxNameLen}")

        tk.messagebox.showerror(
            title="ListNameLengthError",
            message=f"Ilość znaków w nazwie: {len(currentList.name_)} przekracza maksymalną: {currentList.maxNameLen}")


class ListNameAlreadyTakenError(ListError):
    """Nazwa listy zajęta"""

    def __init__(self, currentList):
        super().__init__(
            msg=f"Nazwa \"{currentList.name_}\" jest już zajęta")

        tk.messagebox.showerror(
            title="ListNameAlreadyTakenError",
            message=f"Nazwa \"{currentList.name_}\" jest już zajęta")