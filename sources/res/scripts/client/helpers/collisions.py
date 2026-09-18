from __future__ import absolute_import
from collections import namedtuple
SegmentCollisionResultExt = namedtuple('SegmentCollisionResultExt', ('dist', 'hitAngleCos',
                                                                     'matInfo', 'compName'))