from __future__ import absolute_import
from white_tiger.gui.game_control.awards_controller import WhiteTigerQuestsHandler, WhiteTigerPunishHandler
from gui.shared.system_factory import registerAwardControllerHandlers

def registerWhiteTigerAwardControllers():
    registerAwardControllerHandlers((WhiteTigerQuestsHandler, WhiteTigerPunishHandler))


def registerWhiteTigerSMTypes():
    from gui import SystemMessages
    SystemMessages.SM_TYPE.inject(['WTEventProgression', 'WTEventStart'])