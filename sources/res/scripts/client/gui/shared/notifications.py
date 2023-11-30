from constants import NC_MESSAGE_PRIORITY

class NotificationPriorityLevel(object):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'
    RANGE = (
     HIGH, MEDIUM, LOW)
    NC_MAPPING = {NC_MESSAGE_PRIORITY.HIGH: HIGH, 
       NC_MESSAGE_PRIORITY.MEDIUM: MEDIUM, 
       NC_MESSAGE_PRIORITY.LOW: LOW}

    @classmethod
    def convertFromNC(cls, priority):
        result = NotificationPriorityLevel.MEDIUM
        if priority in cls.NC_MAPPING:
            result = cls.NC_MAPPING[priority]
        return result


class NotificationGroup(object):
    INFO = 'info'
    INVITE = 'invite'
    OFFER = 'offer'
    ALL = (INFO, INVITE, OFFER)


class NotificationGuiSettings(object):
    __slots__ = ('isNotify', 'priorityLevel', 'isAlert', 'auxData', 'showAt', '__customEvent',
                 'groupID', 'messageType', 'messageSubtype', 'decorator', 'lifeTime',
                 'onlyPopUp', 'onlyNCList')

    def __init__(self, isNotify=False, priorityLevel=NotificationPriorityLevel.MEDIUM, isAlert=False, auxData=None, showAt=0, groupID=NotificationGroup.INFO, messageType=None, messageSubtype=None, decorator=None, lifeTime=0, onlyPopUp=False, onlyNCList=False):
        super(NotificationGuiSettings, self).__init__()
        self.isNotify = isNotify
        self.priorityLevel = priorityLevel
        self.isAlert = isAlert
        self.auxData = auxData or []
        self.showAt = showAt
        self.groupID = groupID
        self.messageType = messageType
        self.messageSubtype = messageSubtype
        self.decorator = decorator
        self.lifeTime = lifeTime
        self.onlyPopUp = onlyPopUp
        self.onlyNCList = onlyNCList
        self.__customEvent = None
        return

    def setCustomEvent(self, eType, ctx=None):
        self.__customEvent = (eType, ctx)

    def getCustomEvent(self):
        return self.__customEvent