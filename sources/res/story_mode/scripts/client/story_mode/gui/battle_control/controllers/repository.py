from gui.battle_control.controllers import _ControllersRepository, debug_ctrl, SharedControllersRepository
from gui.battle_control.controllers.battle_hints import controller as battle_hints_ctrl
from gui.battle_control.controllers.sound_ctrls.epic_battle_sounds import EpicShotsResultSoundsController
from gui.battle_control.controllers.vse_hud_settings_ctrl import vse_hud_settings_ctrl
from story_mode.gui.battle_control.controllers.appearance_cache_controller import AppearanceCacheController
from story_mode.gui.battle_control.controllers.messages_controller import StoryModeBattleMessagesPlayer, StoryModeBattleMessagesController
from story_mode.gui.battle_control.controllers.settings_contoller import OverrideSettingsController

class StoryModeRepository(_ControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(StoryModeRepository, cls).create(setup)
        repository.addArenaController(AppearanceCacheController(setup), setup)
        repository.addViewController(debug_ctrl.DebugController(), setup)
        repository.addController(EpicShotsResultSoundsController())
        repository.addViewController(battle_hints_ctrl.BattleHintsController(), setup)
        repository.addController(vse_hud_settings_ctrl.VSEHUDSettingsController())
        return repository


class OnboardingRepository(StoryModeRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(OnboardingRepository, cls).create(setup)
        repository.addArenaController(OverrideSettingsController(), setup)
        return repository


class StoryModeSharedRepository(SharedControllersRepository):
    __slots__ = ()

    @classmethod
    def getMessagesController(cls, setup):
        if setup.isReplayPlaying:
            return StoryModeBattleMessagesPlayer(setup)
        return StoryModeBattleMessagesController(setup)

    @classmethod
    def getAreaMarkersController(cls):
        from story_mode.gui.battle_control.controllers.area_marker_ctrl import StoryModeAreaMarkersController
        return StoryModeAreaMarkersController()