from __future__ import absolute_import
from fort_rush_common import fort_rush_constants
from gui.shared.system_factory import registerAwardControllerHandlers
from fort_rush.gui.game_control.AwardController import FortRushPunishWindowHandler, FortRushAwardsController

def registerFortRushAwardControllers():
    registerAwardControllerHandlers((FortRushAwardsController, FortRushPunishWindowHandler))


def registerFortRushSMTypes():
    from gui import SystemMessages
    SystemMessages.SM_TYPE.inject(['FREventProgression'])


def registerControlModeOverrides():
    from aih_constants import CTRL_MODE_NAME, CTRL_TYPE
    from AvatarInputHandler import OVERWRITE_CTRLS_DESC_MAP
    from fort_rush_control_modes import FortRushPostMortemControlMode
    OVERWRITE_CTRLS_DESC_MAP[fort_rush_constants.ARENA_BONUS_TYPE.FORT_RUSH] = {CTRL_MODE_NAME.POSTMORTEM: (
                                 FortRushPostMortemControlMode,
                                 'postMortemMode',
                                 CTRL_TYPE.USUAL)}