from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin import HelpHintContext

class LunarPossessionHelpPagesFilter(object):
    _FILTER_CTX_KEY = HelpHintContext.MECHANICS

    @classmethod
    def filter(cls, builders):
        return [ b for b in builders if b.HINT_CONTEXT != cls._FILTER_CTX_KEY ]