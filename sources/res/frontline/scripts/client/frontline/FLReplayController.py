from __future__ import absolute_import
import BattleReplay

class FLReplayController(object):

    def __init__(self):
        pass

    @staticmethod
    def setDataCallback(eventName, callback):
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.setDataCallback(eventName, callback)

    @staticmethod
    def delDataCallback(eventName, callback):
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.delDataCallback(eventName, callback)

    @staticmethod
    def serializeCallbackData(eventName, data):
        BattleReplay.g_replayCtrl.serializeCallbackData(eventName, data)