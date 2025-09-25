from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import typing
    from typing import *
    __all__ = locals().keys()
else:
    __all__ = ('TYPE_CHECKING', )