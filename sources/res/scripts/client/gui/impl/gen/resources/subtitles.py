from gui.impl.gen_utils import DynAccessor

class Subtitles(DynAccessor):
    __slots__ = ()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(110543)

    development = _development()