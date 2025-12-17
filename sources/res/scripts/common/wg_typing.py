import typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import *
    from _weakref import ProxyType as _ProxyType
    P = TypeVar('P', bound=_ProxyType)

    class Proxy(Generic[P], _ProxyType):
        pass


    __all__ = locals().keys()
else:
    __all__ = ('typing', 'TYPE_CHECKING')