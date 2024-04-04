import tkinter as tk
from tkinter import colorchooser
from shapes import CircleDrawer, SquareDrawer, TriangleDrawer, RectangleDrawer
from edit.delete import ShapeDeleter
from save.openFile import ProjectOpener
from save.saveFile import ProjectSaver

class ShapeApp:
    def __init__(self, master):
        self.master = master
        master.title("Shapes Drawer")

        self.canvas = tk.Canvas(master, width=600, height=400, bg='grey')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.shape_drawers = {
            "Square": SquareDrawer(self.canvas),
            "Rectangle": RectangleDrawer(self.canvas),
            "Circle": CircleDrawer(self.canvas),
            "Triangle": TriangleDrawer(self.canvas)
        }

        self.shape_deleter = ShapeDeleter(self.canvas)
        self.project_saver = ProjectSaver(self.canvas)
        self.project_opener = ProjectOpener(self.canvas)

        self.create_menus()

        self.canvas.bind('<BackSpace>', self.shape_deleter.delete_last_shape)
        self.canvas.bind('<KeyPress-Up>', self.resize_shape)
        self.canvas.bind('<KeyPress-Down>', self.resize_shape)
        self.canvas.bind('<KeyPress-Left>', self.resize_shape)
        self.canvas.bind('<KeyPress-Right>', self.resize_shape)
        self.canvas.bind('<ButtonPress-3>', self.move_and_zoom)

    def create_menus(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        shapes_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Shape", menu=shapes_menu)
        for shape_name in self.shape_drawers:
            shapes_menu.add_command(label=shape_name, command=lambda shape=shape_name: self.bind_shape(shape))
        shapes_menu.add_separator()
        shapes_menu.add_command(label="Exit", command=self.master.quit)

        file_menu = tk.Menu(menubar, tearoff=0, bg='#ffffff', fg='#000000')
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self.open_project)
        file_menu.add_command(label='Save As', command=self.save_project)

    def bind_shape(self, shape):
        self.canvas.bind('<ButtonPress-1>', lambda event: self.shape_drawers[shape].draw_shape(event))

    def resize_shape(self, event):
        resize = getattr(self.shape_drawers.get("resize"), None)
        if resize:
            resize.resize_shape(event)

    def move_and_zoom(self, event):
        move_and_zoom = getattr(self.shape_drawers.get("move_and_zoom"), None)
        if move_and_zoom:
            move_and_zoom.start_move(event)

    def save_project(self):
        self.project_saver.save_project()

    def open_project(self):
        self.project_opener.open_project()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()
