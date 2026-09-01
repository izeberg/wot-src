from __future__ import absolute_import
from white_tiger.gui.Scaleform.daapi.view.meta.WhiteTigerSettingsWindowMeta import WhiteTigerSettingsWindowMeta
from helpers import dependency
from white_tiger.skeletons.white_tiger_controller import IWhiteTigerController

class WhiteTigerSettingsWindow(WhiteTigerSettingsWindowMeta):
    __wtController = dependency.descriptor(IWhiteTigerController)

    def __init__(self, **kwargs):
        super(WhiteTigerSettingsWindow, self).__init__(ctx={'redefinedKeyMode': True, 
           'isBattleSettings': True, 
           'tabIndex': 0})

    def _update(self):
        super(WhiteTigerSettingsWindow, self)._update()
        self.__setEventSettingVisibility()

    def __setEventSettingVisibility(self):
        self.as_setIsEventS(self.__wtController.isInWhiteTigerMode())