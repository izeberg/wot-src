from gui.shared.system_factory import registerNotificationsListeners
from armory_yard.messenger.listeners import ArmoryYardListener

def registerArmoryYardNotificationListener():
    registerNotificationsListeners((ArmoryYardListener,))