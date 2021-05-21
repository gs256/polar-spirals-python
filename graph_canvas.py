from tkinter import Tk, Canvas
from point import Point
import math


class GraphCanvas:

    def __init__(self, root, size, position):
        self.canvas = Canvas(root, width=size.x, height=size.y)
        self.canvas.pack()
        self.size = size 
        self.position = position
        self.scale = 1
        self.point_color = 'red'
        self.point_size = 1
        self.axis_color = 'black'
        self.axis_width = 1
        self.__draw_axis()

    def draw_point(self, point) -> None:
        point = self.__graph_to_canvas(point, self.scale)
        self.canvas.create_rectangle(
            point.x, 
            point.y, 
            point.x+math.ceil(self.scale), 
            point.y+math.ceil(self.scale), 
            fill=self.point_color
        )

    def set_scale(self, value) -> None:
        self.scale = value

    def is_point_visible(self, point) -> bool:
        point = self.__graph_to_canvas(point, self.scale)
        if (point.x <= self.size.x and point.x >= 0 and \
            point.y <= self.size.y and point.y >= 0):
            return True
        return False

    def __draw_axis(self):
        self.canvas.create_line(0, self.size.y//2, self.size.x, self.size.y//2)
        self.canvas.create_line(self.size.x//2, 0, self.size.x//2, self.size.y)

    def __graph_to_canvas(self, point, scale) -> Point:
        point = point * scale
        x = self.size.x// 2 + point.x
        y = self.size.y// 2 - point.y
        return Point(x, y)
