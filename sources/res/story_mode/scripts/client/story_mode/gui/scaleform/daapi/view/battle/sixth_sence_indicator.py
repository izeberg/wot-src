from gui.Scaleform.daapi.view.battle.shared.indicators import SixthSenseIndicator
from helpers.dependency import descriptor
from skeletons.gui.battle_session import IBattleSessionProvider

class StoryModeSixthSenseIndicator(SixthSenseIndicator):
    __session = descriptor(IBattleSessionProvider)

    def _isSixthSenseEnabled(self):
        vehicle = self.__session.shared.vehicleState.getControllingVehicle()
        enabled = vehicle and 'SMDetectionDelayObservableComponent' not in vehicle.dynamicComponents
        return enabled