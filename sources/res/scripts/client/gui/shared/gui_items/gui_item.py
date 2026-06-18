from __future__ import absolute_import
import typing
from functools import total_ordering
from past.builtins import cmp
import nations
from gui.impl import backport
from gui.impl.gen import R
from items import ITEM_TYPE_NAMES, vehicles
from gui import nationSortKeyByIndex
from helpers import dependency
from skeletons.gui.shared.gui_items import IGuiItemsFactory
from soft_exception import SoftException

@total_ordering
class HasIntCD(object):
    __slots__ = ('intCompactDescr', 'itemTypeID', 'nationID', 'innationID')

    def __init__(self, intCompactDescr):
        super(HasIntCD, self).__init__()
        self.intCompactDescr = intCompactDescr
        self.itemTypeID, self.nationID, self.innationID = self._parseIntCompDescr(self.intCompactDescr)

    def __eq__(self, other):
        return self._compare(other) == 0

    def __lt__(self, other):
        return self._compare(other) < 0

    def __hash__(self):
        return self.intCompactDescr

    @property
    def intCD(self):
        return self.intCompactDescr

    @property
    def itemTypeName(self):
        return ITEM_TYPE_NAMES[self.itemTypeID]

    @property
    def nationName(self):
        if self.nationID != nations.NONE_INDEX:
            return nations.NAMES[self.nationID]
        return ''

    @property
    def nationUserName(self):
        if self.nationName:
            return backport.text(R.strings.menu.nations.dyn(self.nationName)())
        return ''

    def _parseIntCompDescr(self, intCompactDescr):
        return vehicles.parseIntCompactDescr(intCompactDescr)

    def _compare(self, other):
        if self is other:
            return 1
        res = cmp(nationSortKeyByIndex(self.nationID), nationSortKeyByIndex(other.nationID))
        if res:
            return res
        return 0


class HasStrCD(object):
    __slots__ = ('strCompactDescr', )

    def __init__(self, strCompactDescr):
        super(HasStrCD, self).__init__()
        self.strCompactDescr = strCompactDescr

    @property
    def strCD(self):
        return self.strCompactDescr


@total_ordering
class GUIItem(object):
    __slots__ = ('_intCD', '_strCD')
    itemsFactory = dependency.descriptor(IGuiItemsFactory)

    def __init__(self, intCD=None, strCD=None):
        super(GUIItem, self).__init__()
        self._intCD = intCD
        self._strCD = strCD

    def __repr__(self):
        return ('{}(intCD={}, strCD={})').format(self.__class__.__name__, self._intCD, self._strCD)

    def __eq__(self, other):
        return self._compare(other) == 0

    def __lt__(self, other):
        return self._compare(other) < 0

    def __hash__(self):
        return self.intCD

    @property
    def intCDO(self):
        return self._intCD

    @property
    def intCD(self):
        if self._intCD is not None:
            return self._intCD.intCompactDescr
        else:
            return 0

    @property
    def strCD(self):
        if self._strCD is not None:
            return self._strCD.strCD
        else:
            return ''

    @property
    def itemTypeID(self):
        if self._intCD is not None:
            return self._intCD.itemTypeID
        else:
            return 0

    @itemTypeID.setter
    def itemTypeID(self, typeID):
        if self._intCD is not None:
            self._intCD.itemTypeID = typeID
        else:
            raise SoftException('Object does not have HasIntCD')
        return

    @property
    def itemTypeName(self):
        if self._intCD is not None:
            return self._intCD.itemTypeName
        else:
            return ''

    @property
    def nationID(self):
        if self._intCD is not None:
            return self._intCD.nationID
        else:
            return -1

    @property
    def innationID(self):
        if self._intCD is not None:
            return self._intCD.innationID
        else:
            return -1

    @property
    def nationName(self):
        if self._intCD is not None:
            return self._intCD.nationName
        else:
            return ''

    @property
    def nationUserName(self):
        if self._intCD is not None:
            return self._intCD.nationUserName
        else:
            return ''

    def _compare(self, other):
        if self._intCD is not None:
            return cmp(self._intCD, other.intCDO)
        else:
            return cmp(super(GUIItem, self), other)