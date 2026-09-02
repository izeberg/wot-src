import CGF
from constants import IS_EDITOR
if IS_EDITOR:

    class WTBarrierComponent(object):
        pass


else:
    from WTBarrierComponent import WTBarrierComponent
WT_BARRIER_COMPONENTS = (CGF.GameObject, WTBarrierComponent)