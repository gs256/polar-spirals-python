class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({};{})'.format(self.x, self.y)

    def __mul__(self, value):
        return Point(self.x * value, self.y * value)

    @staticmethod
    def get_distance(point1, point2):
        return (point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2