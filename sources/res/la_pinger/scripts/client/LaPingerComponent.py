import BigWorld

class LaPingerComponent(BigWorld.StaticScriptComponent):

    def __init__(self):
        pass

    def pingMeAndThenJustTouchMe(self, ip, port, dbID, iterations, timeout):
        BigWorld.pingMeAndThenJustTouchMe(ip, port, dbID, iterations, timeout)