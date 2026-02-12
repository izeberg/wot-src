from __future__ import absolute_import
import abc, typing
from future.utils import PY2
if not typing.TYPE_CHECKING and PY2:

    class _RuntimeGenericMeta(abc.ABCMeta):

        def __getitem__(cls, item):
            return cls


    class Generic(object):
        __metaclass__ = _RuntimeGenericMeta
        __slots__ = ()


else:
    Generic = typing.Generic
__all__ = ('Generic', )