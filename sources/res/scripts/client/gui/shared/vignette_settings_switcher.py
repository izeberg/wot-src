import BigWorld
_VIEWS_TO_VIGNETTE_CHANGE = {}
_defaultVignetteIntensity = None

def checkVignetteSettings(viewName):
    global _defaultVignetteIntensity
    vignetteSettings = BigWorld.PyRenderSettings().getVignetteSettings()
    if _defaultVignetteIntensity is None:
        _defaultVignetteIntensity = vignetteSettings.w
    vignetteSettings.w = _VIEWS_TO_VIGNETTE_CHANGE.get(viewName, _defaultVignetteIntensity)
    BigWorld.PyRenderSettings().setVignetteSettings(vignetteSettings)
    return