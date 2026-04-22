from gui.impl.gen_utils import DynAccessor

class Areas(DynAccessor):
    __slots__ = ()
    context_menu = DynAccessor(4)
    default = DynAccessor(5)
    flattening_window = DynAccessor(6)
    pop_over = DynAccessor(7)
    restored = DynAccessor(8)
    specific = DynAccessor(9)