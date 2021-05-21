from point import Point
from graph_app import GraphApp
from point import Point
import math


WIDTH = 720 
HEIGHT = 720
SCALE = 0.08
NUMBER_OF_POINTS = 10000


def polar_to_cartesian(point) -> Point: 
    x = point.x * math.cos(point.y)
    y = point.x * math.sin(point.y)
    return Point(x, y)


def has_to_stop_drawing(point, canvas) -> bool:
    if point.x > canvas.size.x and point.y > canvas.size.y:
        return True 
    return False


def draw(event):
    app.graph_canvas.set_scale(SCALE)
    i = 1 
    has_to_stop = False

    while not has_to_stop:
        point = Point(i, i)
        point = polar_to_cartesian(point)

        if app.graph_canvas.is_point_visible(point):
            app.graph_canvas.draw_point(point)

        has_to_stop = i > NUMBER_OF_POINTS 

        i += 1

    # master.mainloop()


app = GraphApp(Point(WIDTH, HEIGHT))
app.on_draw_button_click(draw)

app.mainloop()
