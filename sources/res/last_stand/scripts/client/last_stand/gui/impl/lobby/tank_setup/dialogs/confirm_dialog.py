from __future__ import absolute_import
from gui.impl.lobby.tank_setup.dialogs.confirm_dialog import TankSetupConfirmDialog

class LSTankSetupConfirmDialog(TankSetupConfirmDialog):

    def __init__(self, *args, **kwargs):
        super(LSTankSetupConfirmDialog, self).__init__(*args, **kwargs)
        self._itemsType = 'ls_equipment'