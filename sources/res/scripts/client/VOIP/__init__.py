from __future__ import absolute_import
import BigWorld

def getVOIPManager():
    if not globals().has_key('__handler'):
        from VOIP.VOIPManager import VOIPManager
        globals()['__handler'] = VOIPManager()
    return __handler