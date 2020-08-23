# reference: https://stackoverflow.com/questions/43020833/python-minesweeper-game-gtk3-get-button-value-after-click

import gi
from random import randrange

gi.require_version('Gtk', '3.0')
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

class Cell(Gtk.Button):
    def __init__(self):
        Gtk.Button.__init__(self)
        self.set_size_request(50, 50)

class MainWindow:
    def __init__(self, rows, cols):
        self.window = Gtk.Window()
        self.rows = rows
        self.cols = cols
        self.vbox = Gtk.VBox()
        self.window.add(self.vbox)
        self.create_grid(rows, cols)
        self.window.connect('destroy', Gtk.main_quit)

    def create_grid(self, rows, cols):
        
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.vbox.pack_start(self.grid, expand=True, fill=True, padding=0)

win = MainWindow(5, 5)
win.window.show_all()
Gtk.main()
