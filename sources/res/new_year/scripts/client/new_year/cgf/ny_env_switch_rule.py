import CGF
from new_year.skeletons.new_year import INewYearEnvironmentSwitchController
from helpers import dependency

class NewYearEnvironmentLoader(CGF.ComponentManager):
    __nyEnvSwitcherController = dependency.descriptor(INewYearEnvironmentSwitchController)

    def activate(self):
        self.__nyEnvSwitcherController.applyCurrentEnvironment()