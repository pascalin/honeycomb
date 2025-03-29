from .beehive import *


def appmaker(zodb_root):
    if 'app_root' not in zodb_root:
        app_root = BeeHive()
        hc = Honeycomb('default', "Convida Abejas")
        hc.__parent__ = app_root
        app_root['default'] = hc
        cell = CellText('intro', """This is the first cell of this honeycomb.
         Here you can welcome your visitors and give them some instructions about how to follow.""", title="Introduction")
        cell.__parent__ = hc
        hc["intro"] = cell
        zodb_root['app_root'] = app_root
    return zodb_root['app_root']
