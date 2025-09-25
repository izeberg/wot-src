import operator
from functools import wraps
from helpers import dependency
from skeletons.gui.game_control import IHangarGuiController

def ifComponentAvailable(componentType=None):

    def decorator(method):

        @wraps(method)
        def wrapper(hangar, *args, **kwargs):
            hangarGuiCtrl = dependency.instance(IHangarGuiController)
            if hangarGuiCtrl.sfController.isComponentAvailable(componentType):
                return method(hangar, *args, **kwargs)

        return wrapper

    return decorator


def ifComponentInPreset(componentType=None, defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(presetGetter, *args, **kwargs):
            preset = presetGetter.getPreset()
            if preset is not None and componentType in preset.visibleComponents:
                return method(presetGetter, preset, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(presetGetter)
                return defReturn

        return wrapper

    return decorator


def hasCurrentPreset(defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(hangarGuiSfCtrl, *args, **kwargs):
            currentPreset = hangarGuiSfCtrl.getCurrentPreset()
            if currentPreset is not None:
                return method(hangarGuiSfCtrl, currentPreset, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(hangarGuiSfCtrl)
                return defReturn

        return wrapper

    return decorator