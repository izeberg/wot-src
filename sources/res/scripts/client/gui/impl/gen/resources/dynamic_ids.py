from gui.impl.gen_utils import DynAccessor

class DynamicIds(DynAccessor):
    __slots__ = ()

    class _dialog_window(DynAccessor):
        __slots__ = ()
        bottom_content = DynAccessor(119493)
        balance_content = DynAccessor(119494)

    dialog_window = _dialog_window()

    class _tooltip(DynAccessor):
        __slots__ = ()
        normal_content = DynAccessor(119495)
        advanced_content = DynAccessor(119496)

    tooltip = _tooltip()

    class _blueprint_screen(DynAccessor):
        __slots__ = ()
        balance_content = DynAccessor(119497)

    blueprint_screen = _blueprint_screen()

    class _demo_window(DynAccessor):
        __slots__ = ()
        image_props = DynAccessor(119498)
        bottom_panel = DynAccessor(119499)

    demo_window = _demo_window()