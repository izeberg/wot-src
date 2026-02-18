from gui.shared.system_factory import CollectEventsManager

class FunFactoryConstants(object):
    PRESETS_CONFIG = 0
    SUB_MODE = 1
    BATTLE_RESULTS_SUB_FORMATTER = 2
    BATTLE_RESULTS_PRESENTER = 3
    HANGAR_COMPONENTS = 4


__collectFunRandomEM = CollectEventsManager()

def registerFunRandomSubMode(subModeImpl, subMode):

    def onCollect(ctx):
        ctx[subModeImpl] = subMode

    __collectFunRandomEM.addListener((FunFactoryConstants.SUB_MODE, subModeImpl), onCollect)


def collectFunRandomSubMode(subModeImpl):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.SUB_MODE, subModeImpl), {}).get(subModeImpl)


def registerFunBattleResultsPresenter(subModeImpl, presenterCls, layoutID=None):

    def onCollect(ctx):
        ctx[subModeImpl] = (
         presenterCls, layoutID)

    __collectFunRandomEM.addListener((FunFactoryConstants.BATTLE_RESULTS_PRESENTER, subModeImpl), onCollect)


def collectFunBattleResultsPresenter(subModeImpl):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.BATTLE_RESULTS_PRESENTER, subModeImpl), {}).get(subModeImpl, (None,
                                                                                       None))


def registerBattleResultsMessageSubFormatter(arenaGuiType, battleResultsFormatterCls):

    def onCollect(ctx):
        ctx['battleResultsSubFormatter'] = battleResultsFormatterCls

    __collectFunRandomEM.addListener((FunFactoryConstants.BATTLE_RESULTS_SUB_FORMATTER, arenaGuiType), onCollect)


def collectBattleResultsMessageSubFormatter(arenaGuiType):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.BATTLE_RESULTS_SUB_FORMATTER, arenaGuiType), ctx={}).get('battleResultsSubFormatter')


def registerFunHangarComponent(subModeImpl, alias, presenterClass):

    def onCollect(ctx):
        ctx[alias] = presenterClass

    __collectFunRandomEM.addListener((FunFactoryConstants.HANGAR_COMPONENTS, subModeImpl, alias), onCollect)


def collectFunHangarComponent(subModeImpl, alias, default=None):
    return __collectFunRandomEM.handleEvent((
     FunFactoryConstants.HANGAR_COMPONENTS, subModeImpl, alias), {}).get(alias, default)