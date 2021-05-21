from tkinter import Tk, Frame, Button
from graph_canvas import GraphCanvas 
from point import Point


class GraphApp(Frame):

    def __init__(self, canvas_size):
        self.root = Tk()
        super().__init__(self.root)
        self.graph_canvas = GraphCanvas(self.root, canvas_size, Point(0, 0))
        self.__init_controls()

    def __init_controls(self):
        self.draw_button = Button(self.root, text="Draw")
        self.draw_button.pack()

    def draw_polar_graph(self):
        pass

    def on_draw_button_click(self, function):
        self.draw_button.bind("<Button-1>", function)