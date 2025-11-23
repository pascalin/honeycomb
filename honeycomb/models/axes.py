from collections import namedtuple
from collections.abc import Sequence
from persistent import Persistent
from pyramid import traversal
import numpy as np
from scipy import spatial


LABELS_DEFAULT = 'problem_solving', 'integration', 'abstract_thinking'


class CellBuilder(Persistent):
    "Helper class to set cell properties"
    def __init__(self, axes=LABELS_DEFAULT, default=0):
        self.__axes__ = axes
        if isinstance(default, Sequence) and len(default) < len(axes):
            default = default * (len(axes) // len(default))
        elif not isinstance(default, Sequence):
            default = [default] * len(axes)
        CellBuilder.JellyPack = namedtuple('JellyPack', axes, defaults=default)

    def fill_cell(self, cell, *values, **kwvalues):
        cell.__axes__ = self.JellyPack(*values, **kwvalues)

    def set_walls(self, cell, limits):
        cell.__limits__ = {k:limits[k] for k in limits if k in self.__axes__}

    def set_badge(self, cell, badge):
        cell.__badge__ = badge



class HoneycombExplorer(Persistent):
    "Helper to create, update and employ the honeycomb node distance matrix"
    def __init__(self, honeycomb):
        self.__hc__ = honeycomb
        self.names = []
        self.matrix = None

    def update_matrix(self):
        root = traversal.find_root(self.__hc__)
        names = []
        coords = []
        for item in root.__nodes__.items():
            path = traversal.resource_path_tuple(item[1])
            if path and path[1] == self.__hc__.__name__:
                if getattr(item[1], '__axes__', None):
                    names.append(item[0])
                    coords.append(item[1].__axes__)
        print(coords)
        self.matrix = spatial.distance_matrix(np.array(coords), np.array(coords))
        self.nodes = names
