import CGF
from new_year.cgf.interactive_state_machine_components import PersonaStateMachineManager
from new_year.cgf.ny_surprice_machine_components import NewYearMachineButtonsManager, NewYearMachineActivatorManager
from cgf_components.view_camera_sync import ViewCameraSyncManager, ViewCameraLinksManager
from new_year.cgf.lobby_customization_components import LobbyCustomizableObjectsManager
from new_year.cgf.new_year_components import NewYearClickManager, NewYearHoverManager
from new_year.cgf.ny_click_bonus_video_component import NewYearClickBonusVideoManager
from new_year.cgf.ny_events_listener_component import NewYearEventsListenerManager
from cgf_script.managers_registrator import registerRule, registerManager, Rule
from new_year.cgf.raccoon_customization_components import RaccoonManager
from new_year.cgf.environment_dependent_component import NyEnvironmentDependentManager
from new_year.cgf.ny_env_switch_rule import NewYearEnvironmentLoader
from new_year.cgf.ny_lobby_markers_components import ObjectLobbyMarkersManager
from cgf_components.marker_component import LobbyGFMarkersManager
from new_year.cgf.ny_animations import NewYearAnimatorManager
from cgf_components.token_component import TokenManager

@registerRule
class NyHangarRule(Rule):
    category = 'New year rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(LobbyCustomizableObjectsManager)
    def reg1(self):
        return

    @registerManager(NewYearClickManager)
    def reg2(self):
        return

    @registerManager(ViewCameraSyncManager)
    def reg3(self):
        return

    @registerManager(ViewCameraLinksManager)
    def reg4(self):
        return

    @registerManager(LobbyGFMarkersManager)
    def reg5(self):
        return

    @registerManager(NewYearHoverManager)
    def reg6(self):
        return

    @registerManager(RaccoonManager)
    def reg7(self):
        return

    @registerManager(NewYearAnimatorManager)
    def reg8(self):
        return

    @registerManager(TokenManager)
    def reg9(self):
        return

    @registerManager(NewYearEnvironmentLoader)
    def reg10(self):
        return

    @registerManager(NewYearMachineButtonsManager)
    def reg11(self):
        return

    @registerManager(NewYearMachineActivatorManager)
    def reg12(self):
        return

    @registerManager(ObjectLobbyMarkersManager)
    def reg13(self):
        return

    @registerManager(PersonaStateMachineManager)
    def reg14(self):
        return

    @registerManager(NewYearEventsListenerManager)
    def reg15(self):
        return

    @registerManager(NewYearClickBonusVideoManager)
    def reg16(self):
        return

    @registerManager(NyEnvironmentDependentManager)
    def reg17(self):
        return