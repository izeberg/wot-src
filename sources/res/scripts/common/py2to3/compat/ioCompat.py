from __future__ import absolute_import
import typing
from past.builtins import unicode

def _toUnicode(value, errors='replace'):
    if isinstance(value, unicode):
        return value
    if isinstance(value, bytes):
        return value.decode('utf-8', errors=errors)
    return unicode(value)


class UnicodeFileAdapter(object):

    def __init__(self, target):
        self.target = target

    def write(self, data):
        return self.target.write(_toUnicode(data))

    def writelines(self, lines):
        return self.target.writelines(_toUnicode(line) for line in lines)

    def __getattr__(self, name):
        return getattr(self.target, name)