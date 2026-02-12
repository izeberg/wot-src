import logging
from gui.battle_control.controllers.repositories import SharedControllersRepository, ClassicControllersRepository
from lunar_possession.gui.battle_control.controllers.lunar_help_ctrl import LunarIngameHelpController
from lunar_possession.gui.battle_control.controllers.lunar_possession_battle_ctrl import createLunarPossessionBattleController
from gui.armor_flashlight.battle_controller import ArmorFlashlightBattleController
from gui.battle_control.controllers import aiming_sounds_ctrl
from gui.battle_control.controllers import arena_border_ctrl, arena_load_ctrl, avatar_stats_ctrl, chat_cmd_ctrl, spectator_ctrl, consumables, drr_scale_ctrl, feedback_adaptor, game_messages_ctrl, hit_direction_ctrl, period_ctrl, personal_efficiency_ctrl, vehicle_state_ctrl, view_points_ctrl, vehicle_passenger, vehicles_tracking, anonymizer_fakes_ctrl, game_restrictions_msgs_ctrl, callout_ctrl, deathzones_ctrl, prebattle_setups_ctrl, kill_cam_ctrl, spotting_indicators_ctrl
from gui.battle_control.controllers import map_zones_ctrl
from gui.battle_control.controllers.auto_shoot_guns.auto_shoot_ctrl import AutoShootControllerFactory
from gui.battle_control.controllers.quest_progress import quest_progress_ctrl
from gui.battle_control.controllers.spam_protection import battle_spam_ctrl
from gui.battle_control.controllers.vse_hud_settings_ctrl import vse_hud_settings_ctrl
_logger = logging.getLogger(__name__)

class LunarPossessionSharedControllersRepository(SharedControllersRepository):

    @classmethod
    def create(cls, setup):
        repository = cls()
        from gui.battle_control.controllers import crosshair_proxy
        repository.addController(crosshair_proxy.CrosshairDataProxy())
        ammo = consumables.createAmmoCtrl(setup)
        repository.addViewController(ammo, setup)
        repository.addController(consumables.createEquipmentCtrl(setup))
        repository.addController(cls.getOptionalDevicesController(setup))
        state = vehicle_state_ctrl.createCtrl(setup)
        repository.addController(state)
        passenger = vehicle_passenger.createVehiclePassengerController(state)
        repository.addController(passenger)
        repository.addController(vehicles_tracking.createVehiclesTrackingController(passenger))
        repository.addController(avatar_stats_ctrl.AvatarStatsController())
        messages = cls.getMessagesController(setup)
        feedback = feedback_adaptor.createFeedbackAdaptor(setup)
        repository.addController(feedback)
        repository.addController(messages)
        repository.addController(chat_cmd_ctrl.ChatCommandsController(setup, feedback, ammo))
        repository.addController(drr_scale_ctrl.DRRScaleController(messages))
        repository.addController(personal_efficiency_ctrl.createEfficiencyCtrl(setup, feedback, state))
        repository.addController(game_restrictions_msgs_ctrl.createGameRestrictionsMessagesController())
        repository.addController(kill_cam_ctrl.KillCameraController())
        repository.addArenaController(quest_progress_ctrl.createQuestProgressController(), setup)
        repository.addArenaController(view_points_ctrl.ViewPointsController(setup), setup)
        guiVisitor = setup.arenaVisitor.gui
        if guiVisitor.isBattleRoyale():
            repository.addArenaController(arena_border_ctrl.BattleRoyaleBorderCtrl(), setup)
        else:
            repository.addArenaController(arena_border_ctrl.ArenaBorderController(), setup)
        repository.addArenaController(anonymizer_fakes_ctrl.AnonymizerFakesController(setup), setup)
        repository.addArenaViewController(prebattle_setups_ctrl.PrebattleSetupsController(), setup)
        repository.addArenaViewController(arena_load_ctrl.createArenaLoadController(setup), setup)
        repository.addArenaViewController(period_ctrl.createPeriodCtrl(setup), setup)
        repository.addViewController(hit_direction_ctrl.createHitDirectionController(setup), setup)
        repository.addViewController(game_messages_ctrl.createGameMessagesController(setup), setup)
        repository.addViewController(callout_ctrl.createCalloutController(setup), setup)
        repository.addViewController(spectator_ctrl.SpectatorViewController(), setup)
        repository.addArenaController(cls.getAreaMarkersController(), setup)
        repository.addArenaController(deathzones_ctrl.DeathZonesController(), setup)
        repository.addController(AutoShootControllerFactory.createAutoShootController(setup))
        repository.addController(LunarIngameHelpController(setup))
        repository.addController(map_zones_ctrl.MapZonesController(setup))
        repository.addController(battle_spam_ctrl.BattleSpamController())
        repository.addController(aiming_sounds_ctrl.AimingSoundsCtrl())
        repository.addArenaController(ArmorFlashlightBattleController(), setup)
        repository.addController(spotting_indicators_ctrl.createCtrl(setup, state))
        return repository


class LunarPossessionControllersRepository(ClassicControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(LunarPossessionControllersRepository, cls).create(setup)
        repository.addArenaViewController(createLunarPossessionBattleController(), setup)
        repository.addController(vse_hud_settings_ctrl.VSEHUDSettingsController())
        return repository