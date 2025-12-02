import WWISE
from gui.impl.new_year.sounds import NewYearSoundStates

def setOverlayHangarGeneral(onState):
    if onState:
        WWISE.WW_setState(NewYearSoundStates.STATE_OVERLAY_HANGAR_GENERAL, NewYearSoundStates.STATE_OVERLAY_HANGAR_GENERAL_ON)
    else:
        WWISE.WW_setState(NewYearSoundStates.STATE_OVERLAY_HANGAR_GENERAL, NewYearSoundStates.STATE_OVERLAY_HANGAR_GENERAL_OFF)