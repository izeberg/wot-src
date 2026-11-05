from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    def with_metaclass(meta, *bases):
        return meta('temporary_class', bases, {})


else:

    def with_metaclass(meta, *bases):

        class metaclass(meta):
            __call__ = type.__call__
            __init__ = type.__init__

            def __new__(cls, name, this_bases, d):
                if this_bases is None:
                    return type.__new__(cls, name, (), d)
                else:
                    result = meta(name, bases, d)
                    result.__temporaryBase__ = this_bases[0]
                    return result

        return metaclass('temporary_class', None, {})