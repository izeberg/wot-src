import logging, typing
from gui.impl.lobby.crew.container_vews.personal_file import getPersonalFileView
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from gui.impl.lobby.crew.container_vews.personal_file.controller import PersonalFileInteractionController

def loadSortingOrderType():
    personalFileView = getPersonalFileView()
    if personalFileView:
        ctrl = personalFileView.interactionCtrl
        return ctrl.getCrewAssistSortSelection()
    _logger.warning("Couldn't load setting because PersonalFileView is not found!")
    return 0


def saveSortingOrderType(sortingType):
    personalFileView = getPersonalFileView()
    if personalFileView:
        ctrl = personalFileView.interactionCtrl
        ctrl.setCrewAssistSortSelection(sortingType)
    else:
        _logger.warning("Couldn't save setting because PersonalFileView is not found!")