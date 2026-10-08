from gui.impl.gen_utils import DynAccessor

class Subtitles(DynAccessor):
    __slots__ = ()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(113928)

    development = _development()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro_vp8_8_128 = DynAccessor(113929)

    portal = _portal()