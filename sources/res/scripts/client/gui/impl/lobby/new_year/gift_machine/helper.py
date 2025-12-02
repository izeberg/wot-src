from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.views.gift_machine.ny_gift_machine_view_model import MachineState
from gui.impl.lobby.new_year.gift_machine.ho_gift_machine_view import HOGiftMachineView
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
_HO_MAIN_VIEW_RES_ID = R.views.mono.holiday_ops.main()
_NON_ANIMATION_STATES = (
 MachineState.IDLE,
 MachineState.REWARD,
 MachineState.RAREREWARD,
 MachineState.SPECIALREWARD,
 MachineState.ERROR,
 MachineState.SPECIALREWARDPREVIEW,
 MachineState.BUYTOKENS)

def isGiftMachineAnimationPlaying():
    uiLoader = dependency.instance(IGuiLoader)
    hoMainView = uiLoader.windowsManager.getViewByLayoutID(_HO_MAIN_VIEW_RES_ID)
    if hoMainView:
        presenter = hoMainView.currentPresenter
        if isinstance(presenter, HOGiftMachineView):
            if presenter.viewModel.getMachineState() not in _NON_ANIMATION_STATES:
                return True
    return False