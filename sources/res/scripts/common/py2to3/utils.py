from __future__ import absolute_import
import inspect, sys
PY3 = sys.version_info.major >= 3

def getargspec(func):
    if PY3:
        return inspect.getfullargspec(func)
    else:
        return inspect.getargspec(func)