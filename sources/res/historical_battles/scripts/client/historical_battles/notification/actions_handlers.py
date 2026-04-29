from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE
from historical_battles.gui.shared.event_dispatcher import showHBFairplayDialog, showHBFairplayWarningDialog, showHBProgressionView
from helpers import dependency
from historical_battles.skeletons.gui.game_event_controller import IGameEventController

class ShowHBFairPlayActionHandler(NavigationDisabledActionHandler):

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        showHBFairplayDialog(data=notification.getSavedData())

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('showHistoricalBattlesFairPlayWindow', )


class ShowHBWarningFairPlayActionHandler(NavigationDisabledActionHandler):

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        data = notification.getSavedData()
        showHBFairplayWarningDialog(data.get('reason', ''))

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('showHistoricalBattlesWarningFairPlayWindow', )


class ShowHBProgressionActionHandler(NavigationDisabledActionHandler):

    def doAction(self, model, entityID, action):
        notification = model.getNotification(self.getNotType(), entityID)
        savedData = notification.getSavedData()
        forceSelectHBAction()
        showHBProgressionAction(frontId=savedData.get('frontId'))

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('showHistoricalBattlesProgression', )


@dependency.replace_none_kwargs(controller=IGameEventController)
def showHBProgressionAction(frontId, controller=None):
    if not controller.isEnabled():
        return
    showHBProgressionView(frontId=frontId)


@dependency.replace_none_kwargs(controller=IGameEventController)
def forceSelectHBAction(controller=None):
    controller.switchPrb()


class ShowHBEventStartHandler(NavigationDisabledActionHandler):

    def doAction(self, model, entityID, action):
        forceSelectHBAction()

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.MESSAGE

    @classmethod
    def getActions(cls):
        return ('OnHBStartedMessage', )