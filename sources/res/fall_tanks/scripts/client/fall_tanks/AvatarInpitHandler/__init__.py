from __future__ import absolute_import
from aih_constants import CTRL_TYPE, CTRL_MODE_NAME
from fall_tanks.AvatarInpitHandler import control_modes
FALL_TANKS_CTRLS_DESC_MAP = {CTRL_MODE_NAME.POSTMORTEM: (
                             control_modes.FallTanksPostMortemCtrlMode, 'postMortemMode', CTRL_TYPE.USUAL)}