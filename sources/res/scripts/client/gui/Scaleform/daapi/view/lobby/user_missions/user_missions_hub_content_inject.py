from gui.Scaleform.daapi.view.meta.UserMissionsHubContentInjectMeta import UserMissionsHubContentInjectMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class UserMissionsHubContentInject(InjectComponentAdaptor, UserMissionsHubContentInjectMeta):

    def __init__(self, tabID, questId):
        super(UserMissionsHubContentInject, self).__init__()
        self.tabID = tabID
        self.questId = questId

    def _makeInjectView(self):
        from gui.impl.lobby.user_missions.hub.hub_view import HubView
        return HubView(self.tabID, self.questId)