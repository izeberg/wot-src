import BigWorld, Event
from debug_utils import LOG_DEBUG

class ActionsChain(object):

    def __init__(self, actions):
        super(ActionsChain, self).__init__()
        self.__callbackID = None
        self.__actions = actions
        self.__current = None
        self.__isStopped = True
        self.__eManager = Event.EventManager()
        self.onStarted = Event.Event(self.__eManager)
        self.onStopped = Event.Event(self.__eManager)
        return

    @property
    def isActive(self):
        return not self.__isStopped

    def start(self):
        if self.__isStopped:
            LOG_DEBUG('Starts to perform actions', self)
            self.__isStopped = False
            self.onStarted()
            if self.__goToNextAction():
                self.__timeLoop()

    def stop(self):
        if self.__isStopped:
            return
        else:
            LOG_DEBUG('Stops to perform actions', self)
            self.__isStopped = True
            if self.__callbackID is not None:
                BigWorld.cancelCallback(self.__callbackID)
                self.__callbackID = None
            if self.__current is not None:
                isCompleted = self.__current.isCompleted()
            else:
                isCompleted = False
            self.onStopped(isCompleted)
            self.__eManager.clear()
            self.__actions = []
            return

    def __timeLoop(self):
        self.__callbackID = None
        if self.__tick():
            self.__callbackID = BigWorld.callback(0.1, self.__timeLoop)
        return

    def __tick(self):
        result = True
        if not self.__current.isRunning():
            result = self.__goToNextAction()
        return result

    def __goToNextAction(self):
        result = True
        if self.__current and not self.__current.isCompleted():
            self.stop()
            return False
        if self.__actions:
            self.__current = self.__actions.pop(0)
            self.__current.invoke()
            if self.__current.isInstantaneous() or not self.__current.isRunning():
                if self.__current.isCompleted():
                    result = self.__goToNextAction()
                else:
                    self.stop()
                    result = False
        else:
            self.stop()
            result = False
        return result