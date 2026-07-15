from __future__ import absolute_import, print_function
enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print('WARNING: WWISE support is not enabled.')
    enabled = False