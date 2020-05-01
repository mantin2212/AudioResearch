import matplotlib.pyplot as plt


class RealFunction(object):

    def __init__(self, domain, values):
        points = zip(domain, values)
        self.values = dict(points)

    def dom(self):
        return list(self.values.keys())

    def img(self):
        return list(self.values.values())

    def points(self):
        return self.values.items()

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self._slice(*self._get_indices(item))
        elif item in self.dom():
            return self.values[item]
        else:
            return self._estimate_value(item)

    def _slice(self, start, stop, step):
        domain = self._get_x_values(start, stop)
        points = [(x, self.values[x]) for x in domain]

        if step < 0:
            points = points[::-1]

        return points

    def _get_indices(self, s):
        return s.indices(len(self.values))

    @staticmethod
    def _fill_step(step):
        return 1 if (step or 1) > 0 else -1

    def _get_x_values(self, start, stop):
        x_values = self.values.keys()
        return [x for x in x_values if self._in_range(x, start, stop)]

    @staticmethod
    def _in_range(x, min, max):
        return min <= x < max

    def plot(self):
        plt.plot(self.dom(), self.img())
        plt.show()

    def _estimate_value(self, x):
        """
        Estimate the value of the function in a certain point.
        :param float x: The x value to estimate.
        :return: The estimated value of f(x).
        :rtype: float
        """
        point1, point2 = self._find_closest_points(x)
        ratio = (point2[0] - x) / (x - point1[0])

        return divide_line(point1, point2, ratio)

    def _find_closest_points(self, x):
        """
        Finds the closest points above and below some x values.
        :param float x: The x value.
        :return: The two points surrounding x.
        :rtype: tuple
        """
        return self[:x][-1], self[x:][0]


def divide_line(point1, point2, ratio=1.0):
    """
    Divide the line between two points by given ratio.
    :param tuple point1: Line start point.
    :param tuple point2: Line end point
    :param float ratio: The ratio to divide the line by.
    :return: A point 'O' on the line p1-p2, such as that
             len(p1-o)/len(o-p2) = ratio.
    :rtype: tuple
    """
    result_x = _divide_by_ratio(point1[0], point2[0], ratio)
    result_y = _divide_by_ratio(point1[1], point2[1], ratio)
    return result_x, result_y


def _divide_by_ratio(val1, val2, ratio=1.0):
    return (val1 + val2 * ratio) / (ratio + 1)
