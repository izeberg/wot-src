from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE

def getContextMenuHandlers():
    from gui.Scaleform.daapi.view.lobby.messengerBar.ChannelListContextMenuHandler import ChannelListContextMenuHandler
    return (
     (
      CONTEXT_MENU_HANDLER_TYPE.CHANNEL_LIST, ChannelListContextMenuHandler),)


def getViewSettings():
    return ()


def getBusinessHandlers():
    return ()