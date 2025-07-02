from helpers import dependency
from mt_birthday.skeletons.mt_birthday_controller import ITanksBirthdayController

def isBirthdayActive():
    tanksBirthdayController = dependency.instance(ITanksBirthdayController)
    return tanksBirthdayController.isEnabled()