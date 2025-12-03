from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.lobby.hangar.states import HangarState
from gui.impl.lobby.new_year.states import HolidayOpsState
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.event_dispatcher import showStylePreview, hideVehiclePreview, showHangar
from new_year.ny_navigation_helper import switchNewYearView
from new_year.ny_preview import getVehiclePreviewID

def createNavigationAction(objectName, executeBeforeSwitch=None):

    def switchTo():
        switchNewYearView(objectName, instantly=True, executeBeforeSwitch=executeBeforeSwitch)

    return switchTo


def createStylePreviewAction(style):

    def showPreview():
        hideVehiclePreview(back=False)
        showStylePreview(getVehiclePreviewID(style), style, descr=style.getDescription(), backCallback=showHangar)

    return showPreview


def isAcceptableState(prbEntity):
    lsm = getLobbyStateMachine()
    inHangar = lsm.getStateByCls(HangarState).isEntered()
    inHolidayOps = lsm.getStateByCls(HolidayOpsState).isEntered()
    isRandomPrbActive = bool(prbEntity.getModeFlags() & FUNCTIONAL_FLAG.RANDOM)
    return (inHangar or inHolidayOps) and isRandomPrbActive