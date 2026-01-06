from gui.impl.battle.battle_page.battle_context_hints.hint_inject_component import HintInjectComponent

class InfoBattleContextHintMeta(HintInjectComponent):

    def as_setVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibility(isVisible)