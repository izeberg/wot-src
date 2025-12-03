from gui.battle_control.controllers.callout_ctrl import CalloutController

class GrinchCalloutController(CalloutController):

    def _openRadialMenu(self):
        pass


def createCalloutController(setup):
    return GrinchCalloutController(setup)