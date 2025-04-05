from zope.interface import Interface, implementer
from persistent import Persistent
from persistent.mapping import PersistentMapping


class BeeHive(PersistentMapping):
    """A container of Honeycombs. This represents the top-level hierarchy which gives entry to honeycombs. It should
    display the user a mosaic view of available honeycombs, highlighting already completed and recently visited ones,
    as well as those featured by creators and managers."""
    __name__ = None
    __parent__ = None

    def set_name(self, name, title=""):
        self.__name__ = name
        self.title = title

    def set_icon(self, icon):
        self.icon = icon


class Honeycomb(PersistentMapping):
    """A collection of interactive and non-interactive cells. It must have an associated map (either static or dynamic) which will be displayed when the honeycomb is opened."""

    def __init__(self, name, title=""):
        PersistentMapping.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = None
        self.map = None

    def set_map(self, honeycombmap):
        self.map = honeycombmap

    def get_map(self):
        return self.map

class HoneyStaticMap(Persistent):
    """A graphical representation of the Honeycomb structure."""
    def __init__(self, url):
        Persistent.__init__(self)
        self.href = url

    def render(self):
        return f'<img src="{self.href}">'

    def update(self, url):
        self.href = url

class HoneyDynamicMap(Persistent):
    """A complex representation of the Honeycomb structure."""
    def __init__(self, structure):
        Persistent.__init__(self)
        self.structure = structure


class InteractiveCell(Persistent):
    """A BeeHive cell containing an interactive element"""
    def __init__(self, name, title=""):
        Persistent.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = None


class StaticCell(Persistent):
    """A BeeHive cell containing static elements"""
    def __init__(self, name, title=""):
        Persistent.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = None


class CellIcon(Persistent):
    """A BeeHive cell icon"""
    pass


class CellText(Persistent):
    def __init__(self, name, contents, title=""):
        Persistent.__init__(self)
        self.__name__ = name
        self.title = title
        self.contents = contents


class CellRichText(Persistent):
    def __init__(self, name, contents, title=""):
        Persistent.__init__(self)
        self.__name__ = name
        self.title = title
        self.source = contents


class CellAnimation(Persistent):
    def __init__(self, url):
        Persistent.__init__(self)
        self.href = url


class CellWebContent(Persistent):
    def __init__(self, url):
        Persistent.__init__(self)
        self.href = url
