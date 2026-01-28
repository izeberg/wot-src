from gui.Scaleform.genConsts.CROSSHAIR_CASSETTE_TYPES import CROSSHAIR_CASSETTE_TYPES

def getClipType(gunSettings):
    clipType = CROSSHAIR_CASSETTE_TYPES.NO_CASSETTE
    if gunSettings.isCassetteClip():
        if gunSettings.hasAutoReload():
            clipType = CROSSHAIR_CASSETTE_TYPES.AUTOLOADER
            if gunSettings.isMultiGun():
                clipType = CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_AUTOLOADER
        else:
            clipType = CROSSHAIR_CASSETTE_TYPES.CASSETTE
            if gunSettings.isMultiGun():
                clipType = CROSSHAIR_CASSETTE_TYPES.MULTIPLE_BARREL_CASSETTE
            elif gunSettings.hasAutoShoot():
                clipType = CROSSHAIR_CASSETTE_TYPES.AUTO_GUN_CASSETTE
    return clipType