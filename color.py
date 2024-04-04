import tkinter as tk
from tkinter import colorchooser

class Shape:
    def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        self.selected_shape = None
        self.x0, self.y0 = None, None
        
    def change_color_dialog(self):
        """Open a color chooser dialog and change the color of the selected shape."""
        color = colorchooser.askcolor()
        if color and self.selected_shape:
            self.canvas.itemconfig(self.selected_shape, fill=color[1])

    def shape_click(self, event: tk.Event):
        """Handle shape click event."""
        self.selected_shape = event.widget.find_closest(event.x, event.y)
        self.change_color_dialog()
