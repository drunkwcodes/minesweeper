# reference: https://stackoverflow.com/questions/43020833/python-minesweeper-game-gtk3-get-button-value-after-click

import gi
from random import randrange

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


# Button States:
#
# unclicked
# clicked
#
# unclicked
# flagged
# question


# Game functions:
# New Game
# Restart
# Reset
# High Score
#


#  The event.button is a integer value, representing which mouse button was pressed. So 1 is the left button, 2 is the middle and 3 is the right mouse button. By checking to see if the event.button is 3,


#
# In [4]: Gdk.BUTTON_PRIMARY
# Out[4]: 1
#
# In [5]: Gdk.BUTTON_MIDDLE
# Out[5]: 2
#
# In [6]: Gdk.BUTTON_SECONDARY
# Out[6]: 3
#


class Cell(Gtk.Button):
    def __init__(self):
        Gtk.Button.__init__(self)
        self.set_size_request(30, 30)

    def on_clicked(self, widget, event):
        if event.type == Gdk.BUTTON_PRIMARY:
            # open tile
            pass
        elif event.type == Gdk.BUTTON_SECONDARY:
            # mark
            pass
        elif event.type == Gdk.BUTTON_MIDDLE:
            # open adjacent tiles
            pass


class CellGrid(Gtk.Grid):
    def __init__(self, rows, cols, homogeneous=True):
        Gtk.Grid.__init__(self)
        self.rows = rows
        self.cols = cols
        self.cells = []
        for row in range(rows):
            for col in range(cols):
                cell = Cell()
                self.cells.append(cell)
                self.attach(cell, col, col + 1, row, row + 1)


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        vbox = Gtk.VBox()

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.grid = CellGrid(8, 8)
        vbox.pack_start(self.button, False, False, 100)
        vbox.pack_start(self.grid, False, False, 0)
        self.add(vbox)

    def on_button_clicked(self, widget):
        print("Hello World")

    def create_grid(self, rows, cols):

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.vbox.pack_start(self.grid, expand=True, fill=True, padding=0)


win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
