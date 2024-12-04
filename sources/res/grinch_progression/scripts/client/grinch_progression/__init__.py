

def initProgression():
    from gui.game_control import registerGrinchProgressionGameControllers
    from gui.notifications import registerGPNotifications
    registerGrinchProgressionGameControllers()
    registerGPNotifications()