from gui.Scaleform.daapi.view.meta.ResizableEntryPointMeta import ResizableEntryPointMeta
from helpers import dependency
from mt_birthday.gui.impl.lobby.banner.birthday_banner_view import BirthdayBannerView
from mt_birthday.skeletons.mt_birthday_controller import ITanksBirthdayController

def isBirthdayAvailable():
    birthday = dependency.instance(ITanksBirthdayController)
    return birthday.isEnabled() or birthday.isPaused()


class BirthdayBannerEntryPoint(ResizableEntryPointMeta):

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)

    def _makeInjectView(self):
        self.__view = BirthdayBannerView()
        return self.__view