"""
MyGUI
=====
A **simple** UI class
----------------------
With logging
............

*Use it like this*::

    from mygui import MyGUI

    ui = MyGUI("my name")
    ui.run()

"""

import logging
import tkinter
from tkinter import ttk

logger = logging.getLogger(__name__)

class MyGUI:
    """A simple class
    """

    def __init__(self, name:str) -> None:
        """
        MyGUI constructor

        :param name: The name of this thing
        :type name: str
        """
        self._colors = ["red", "green", "blue"]
        self._idx = 0
        self._root = tkinter.Tk()
        self._root.title(name)
        self._root.geometry("300x300+250+100") 
        self.__style = ttk.Style(self._root)
        mainframe = ttk.Frame(self._root)
        mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        self._root.columnconfigure(0, weight=2)
        self._root.rowconfigure(0, weight=2)
        self._button_text = tkinter.StringVar(value='Click')
        button = ttk.Button(mainframe, textvariable=self._button_text, command=self.click)
        button.grid(column=1, row=2, columnspan=2, rowspan=2)
        # Set button colour
        self.__style.configure('TButton', background='lightblue')
        # Set frame background colour
        self.__style.configure('TFrame', background=self._colors[0])

    def run(self, a:str):
        """[summary]

        Args:
            a (str): [description]
        """
        self._root.mainloop()

    def set_color(self, color:str):
        """Set the display colour.

        :param color: a colour name or RGB value
        :type color: str
        """
        logger.info(f"color={color}")
        self.__style.configure('TFrame', background=color)

    def click(self):
        """Called when button clicked.
        """
        logger.info("click")
        self.click_action()

    def click_action(self):
        """An example action to use with click()
        """
        self._idx += 1
        if self._idx == len(self._colors): self._idx = 0
        self.set_color(self._colors[self._idx])

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    a = MyGUI("thing")
    a.run()
