from gui.impl.gen_utils import DynAccessor

class Subtitles(DynAccessor):
    __slots__ = ()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(114194)

    development = _development()

    class _white_tiger(DynAccessor):
        __slots__ = ()
        wt_intro = DynAccessor(114195)
        wt_outro = DynAccessor(114196)

    white_tiger = _white_tiger()