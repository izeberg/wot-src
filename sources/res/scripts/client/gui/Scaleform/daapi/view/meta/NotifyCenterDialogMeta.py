from gui.Scaleform.daapi.view.meta.SimpleDialogMeta import SimpleDialogMeta

class NotifyCenterDialogMeta(SimpleDialogMeta):

    def doAction(self, actionId, isButtonClicked):
        self._printOverrideError('doAction')