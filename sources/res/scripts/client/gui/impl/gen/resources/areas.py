from gui.impl.gen_utils import DynAccessor

class Areas(DynAccessor):
    __slots__ = ()
    context_menu = DynAccessor(3)
    default = DynAccessor(4)
    flattening_window = DynAccessor(5)
    pop_over = DynAccessor(6)
    restored = DynAccessor(7)
    specific = DynAccessor(8)