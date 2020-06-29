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


class ListElementsAmountError(ListError):
    """Zbyt wiele pozycji na liście"""

    def __init__(self, currentList):
        super().__init__(msg=f"Ilość produktów: {len(currentList.list_)} przekracza maskymalną")


class ListNameLengthError(ListError):
    """Nazwa listy zbyt długa"""

    def __init__(self, currentList):
        super().__init__(
            msg=f"Ilość znaków w nazwie: {len(currentList.name_)} przekracza maksymalną: {currentList.maxNameLen}")



class ListNameAlreadyTakenError(ListError):
    """Nazwa listy zajęta"""

    def __init__(self, currentList):
        super().__init__(
            msg=f"Nazwa \"{currentList.name_}\" jest już zajęta")
