from zope.interface import Interface, implementer
from persistent import Persistent
from persistent.mapping import PersistentMapping

import uuid

class BeeHive(PersistentMapping):
    """A container of Honeycombs. This represents the top-level hierarchy which gives entry to honeycombs. It should
    display the user a mosaic view of available honeycombs, highlighting already completed and recently visited ones,
    as well as those featured by creators and managers."""
    __name__ = None
    __parent__ = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "BeeHive Root" 

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


class CellNode(PersistentMapping):
    """A node in the honeycomb structure, it can contain children nodes or be alone, it can also be static or interactive."""
    def __init__(self, name="", parent=None):
        PersistentMapping.__init__(self)
        self.__name__ = name
        self.__parent__ = parent
        self.title = ""
        self.icon = None
        self.id = uuid.uuid4()

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon


class HoneyStaticMap(CellNode):
    """A graphical representation of the Honeycomb structure."""
    def __init__(self, url, filename=None):
        CellNode.__init__(self)
        self.href = url
        self.filename = filename

    def render(self):
        return f'<img src="{self.href}">'

    def update(self, url, filename=None):
        self.href = url
        self.filename = filename

class HoneyDynamicMap(CellNode):
    """A complex representation of the Honeycomb structure."""
    def __init__(self, structure):
        CellNode.__init__(self)
        self.structure = structure


class InteractiveCell(CellNode):
    """A BeeHive cell containing an interactive element"""
    def __init__(self, name, title=""):
        CellNode.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = None


class StaticCell(CellNode):
    """A BeeHive cell containing static elements"""
    def __init__(self, name, title=""):
        CellNode.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = None


class CellIcon(CellNode):
    """A BeeHive cell icon."""
    def __init__(self, name, title="", icon=None):
        CellNode.__init__(self)
        self.__name__ = name
        self.title = title
        self.icon = icon

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon
    

class CellText(CellNode):
    def __init__(self, name, contents, title="", icon=None):
        CellNode.__init__(self)
        self.__name__ = name
        self.title = title
        self.contents = contents
        self.icon = icon

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon


class CellRichText(CellNode):
    def __init__(self, name, contents, title="", icon=None):
        CellNode.__init__(self)
        self.__name__ = name
        self.title = title
        self.source = contents
        self.icon = icon

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon


class CellAnimation(CellNode):
    def __init__(self, name, url, title="", icon=None):
        CellNode.__init__(self)
        self.__name__ = name
        self.href = url
        self.title = title
        self.icon = icon

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon


class CellWebContent(CellNode):
    def __init__(self, name, url, title="", icon=None):
        CellNode.__init__(self)
        self.__name__ = name
        self.href = url
        self.title = title
        self.icon = icon

    def set_icon(self, icon):
        self.icon = icon

    def get_icon(self):
        return self.icon

