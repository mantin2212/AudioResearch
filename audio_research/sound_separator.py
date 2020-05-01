from operator import itemgetter

import numpy as np

from audio_research.fourier_transform import get_freqs
from audio_research.utils.math_utils import RealFunction


class PeakSegment(RealFunction):

    def __init__(self, func, peak_x):
        points = find_peak_points(func, peak_x)
        super(PeakSegment, self).__init__(*zip(*points))

    def peak_center(self):
        center_x = np.average(self.dom(), weights=self.img())
        return center_x, self[center_x]


def find_peak_points(func, peak_x):
    min_limit = find_first_min(func[:peak_x:-1], key=itemgetter(1))
    max_limit = find_first_min(func[peak_x:], key=itemgetter(1))

    return func[min_limit:max_limit]


def find_first_min(lst, key=lambda x: x):
    try:
        min_idx = next(i for i in range(len(lst) - 1)
                       if key(lst[i]) < key(lst[i + 1]))
    except StopIteration:
        return
    else:
        return lst[min_idx]
