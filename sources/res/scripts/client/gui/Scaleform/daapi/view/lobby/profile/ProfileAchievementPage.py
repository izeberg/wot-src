from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.achievements.achievements_main_view import AchievementMainView, AchievementsViewCtx

class ProfileAchievementPage(InjectComponentAdaptor):

    def __init__(self, *args):
        self.__userID = args[1]
        if len(args) > 3 and args[3]:
            self.__closeCallback = args[3].get('closeCallback')
        else:
            self.__closeCallback = None
        super(ProfileAchievementPage, self).__init__()
        return

    def _makeInjectView(self):
        ctx = AchievementsViewCtx(menuName=VIEW_ALIAS.PROFILE_ACHIEVEMENTS_PAGE, userID=self.__userID, closeCallback=self.__closeCallback)
        self.__view = AchievementMainView(ctx)
        return self.__view

    def onSectionActivated(self):
        pass

    def onSectionDeactivated(self):
        pass