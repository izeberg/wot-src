import CGF
from constants import IS_EDITOR
if IS_EDITOR:

    class WTDomeComponent(object):
        pass


else:
    from WTDomeComponent import WTDomeComponent
WT_DOME_COMPONENTS = (CGF.GameObject, WTDomeComponent)