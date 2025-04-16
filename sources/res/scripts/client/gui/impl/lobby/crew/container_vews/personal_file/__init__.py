import typing
from helpers.dependency import replace_none_kwargs
from gui.impl.gen import R
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from gui.impl.lobby.crew.container_vews.personal_file.personal_file_view import PersonalFileView

@replace_none_kwargs(uiLoader=IGuiLoader)
def getPersonalFileView(uiLoader=None):
    return uiLoader.windowsManager.getViewByLayoutID(R.views.lobby.crew.personal_case.PersonalFileView())