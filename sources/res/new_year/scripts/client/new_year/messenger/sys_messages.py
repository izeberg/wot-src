from gui.SystemMessages import SM_TYPE
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from messenger import MessengerEntry
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from new_year_account_settings import getIsFirstMachineToken, setIsFirstMachineToken

def pushNewYearEventButtonMessage(text, msgType, priority=None, messageData=None, savedData=None):
    MessengerEntry.g_instance.protos.BW.serviceChannel.pushClientMessage(text, SCH_CLIENT_MSG_TYPE.NY_EVENT_BUTTON_MESSAGE, isAlert=False, auxData=[
     msgType.name(), priority, messageData, savedData])


def showMachineNotification():
    if not getIsFirstMachineToken():
        pushNewYearEventButtonMessage(text=backport.text(R.strings.ny.notification.machine.text()), msgType=SM_TYPE.NewYearMachine, priority=NotificationPriorityLevel.MEDIUM, messageData={'header': backport.text(R.strings.ny.notification.machine.header())})
        setIsFirstMachineToken(True)