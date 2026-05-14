from __future__ import absolute_import
from io import BytesIO, StringIO
from py2to3.utils import PY3
if PY3:
    FastBytesIO = BytesIO
    FastStringIO = StringIO
else:
    from cStringIO import StringIO as FastStringIO
    FastBytesIO = FastStringIO