from gui.impl.gen_utils import DynAccessor

class default(DynAccessor):
    __slots__ = ()
    battle = DynAccessor(1)
    lobby = DynAccessor(2)


class last_stand(DynAccessor):
    __slots__ = ()
    battle = DynAccessor(3)


class Entries(DynAccessor):
    __slots__ = ()
    default = default()
    last_stand = last_stand()