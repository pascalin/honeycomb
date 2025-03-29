from zope.interface import Interface, implementer
from persistent import Persistent
from persistent.mapping import PersistentMapping


class BeeHive(PersistentMapping):
    """A container of Honeycombs."""
    __name__ = None
    __parent__ = None

    def set_name(self, name, title=""):
        self.__name__ = name
        self.title = title

    def set_icon(self, icon):
        self.icon = icon


class Honeycomb(PersistentMapping):
    """A collection of interactive and non-interactive cells."""

    def __init__(self, name, title=""):
        PersistentMapping.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = None


class HoneyStaticMap(Persistent):
    """A graphical representation of the Honeycomb structure."""
    def __init__(self, url):
        Persistent.__init__(self)
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
