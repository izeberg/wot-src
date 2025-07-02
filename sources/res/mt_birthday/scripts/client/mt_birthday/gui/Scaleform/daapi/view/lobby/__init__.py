from gui.Scaleform.framework import ScopeTemplates, ComponentSettings
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.shared.system_factory import registerBannerEntryPointValidator
from mt_birthday.gui.Scaleform.daapi.view.lobby.hangar.birthday_entry_point import isBirthdayAvailable
registerBannerEntryPointValidator(HANGAR_ALIASES.BIRTHDAY_BANNER_ENTRY_POINT, isBirthdayAvailable)

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from mt_birthday.gui.Scaleform.daapi.view.lobby.hangar.birthday_entry_point import BirthdayBannerEntryPoint
    return (
     ComponentSettings(HANGAR_ALIASES.BIRTHDAY_BANNER_ENTRY_POINT, BirthdayBannerEntryPoint, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()