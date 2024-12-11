from gui.impl.dialogs.builders import InfoDialogBuilder
from new_year.gui.impl.pub.ny_info_dialog_window import NYInfoDialogWindow

class NYInfoDialogBuilder(InfoDialogBuilder):

    def __init__(self):
        super(NYInfoDialogBuilder, self).__init__()
        self._windowClass = NYInfoDialogWindow