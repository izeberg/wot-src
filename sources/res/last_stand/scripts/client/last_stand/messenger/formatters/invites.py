from __future__ import absolute_import
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter
from last_stand.skeletons.ls_controller import ILSController
from helpers import dependency

class LSPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter):
    lsCtrl = dependency.descriptor(ILSController)

    def canAcceptInvite(self, invite):
        canAccept = super(LSPrbInviteHtmlTextFormatter, self).canAcceptInvite(invite)
        return canAccept and self.lsCtrl.isAvailable()