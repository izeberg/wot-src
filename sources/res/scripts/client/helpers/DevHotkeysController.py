import Keys, os, subprocess

def handleKeyEvent(event):
    if event.isShiftDown() and event.isCtrlDown() and event.isAltDown() and event.isKeyDown() and not event.isRepeatedEvent():
        if event.key == Keys.KEY_P:
            subprocess.Popen([os.getcwd() + './../tools/PixelsHunter/PixelsHunter.exe', str(os.getpid())])
            __runSizeManager()
        elif event.key == Keys.KEY_S:
            __runSizeManager()


def __runSizeManager():
    from development.as_tools.change_window_size_manager import g_change_manager as m
    m.start()