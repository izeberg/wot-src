from gui.Scaleform.daapi.view.battle.shared.indicators import SixthSenseIndicator
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class StoryModeSixthSenseIndicator(SixthSenseIndicator):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _show(self):
        vehicle = self.sessionProvider.shared.vehicleState.getControllingVehicle()
        if vehicle is not None:
            self.enabled = 'SMDetectionDelayObservableComponent' not in vehicle.dynamicComponents
        super(StoryModeSixthSenseIndicator, self)._show()
        return