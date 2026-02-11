from gui.impl.gen.view_models.views.lobby.loadout.crew.crew_model import CrewModel
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter

class LunarPossessionCrewPresenter(CrewPresenter):

    def _updateAcceleratedTraining(self):
        self.viewModel.setAcceleratedTraining(CrewModel.HIDDEN_TRAINING_STATE)

    def _updateIntensiveTraining(self):
        self.viewModel.setIntensiveTraining(CrewModel.HIDDEN_TRAINING_STATE)