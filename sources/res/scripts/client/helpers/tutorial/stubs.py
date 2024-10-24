from skeletons.tutorial import ITutorialLoader, IGuiController

class StubGuiController(IGuiController):

    def getViewTutorialID(self, _):
        return

    def init(self, guiProviders):
        pass

    def setup(self, isEnabled=False, path=''):
        pass

    def fini(self):
        pass

    def setHintsWithClientTriggers(self, clientTriggers):
        pass

    def getFoundComponentsIDs(self):
        return []

    def setCriteria(self, name, value):
        pass

    def setViewCriteria(self, componentID, viewUniqueName):
        pass

    def setTriggers(self, componentID, triggers):
        pass

    def clearTriggers(self, componentID):
        pass

    def showInteractiveHint(self, componentID, content, triggers=None, silent=False):
        pass

    def closeInteractiveHint(self, componentID):
        pass

    def setComponentProps(self, componentID, props):
        pass

    def playComponentAnimation(self, componentID, animType):
        pass

    def stopComponentAnimation(self, componentID, animType):
        pass

    def setupViewContextHints(self, viewTutorialID, hintsData, hintsArgs=None):
        pass

    def clear(self):
        pass


class StubTutorialLoader(ITutorialLoader):

    def __init__(self):
        super(StubTutorialLoader, self).__init__()
        self.__gui = StubGuiController()

    @property
    def gui(self):
        return self.__gui

    @property
    def tutorial(self):
        return

    @property
    def hintsManager(self):
        return

    @property
    def tutorialID(self):
        return ''

    @property
    def isRunning(self):
        return False

    def isTutorialStopped(self):
        return False

    def init(self):
        pass

    def fini(self):
        pass

    def run(self, settingsID, state=None):
        pass

    def stop(self, restore=True):
        pass

    def refuse(self):
        pass