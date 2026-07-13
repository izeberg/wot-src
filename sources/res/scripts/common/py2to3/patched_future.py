from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    def with_metaclass(meta, *bases):
        return meta('temporary_class', bases, {})


else:
    from future.utils import with_metaclass