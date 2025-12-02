from ny_common.settings import ObjectsConsts
from typing import Optional, List, Dict

class ObjectsConfig(object):

    def __init__(self, config):
        self._config = config

    def getObjectByID(self, objectID):
        if objectID in self._config:
            return ObjectDescriptor(self._config[objectID])
        else:
            return


class ObjectDescriptor(object):

    def __init__(self, levels):
        self._levels = levels

    def getLevels(self):
        return map(ObjectLevelDescriptor, self._levels)

    def getNextLevel(self, currentLevel):
        if currentLevel + 1 < len(self._levels):
            return ObjectLevelDescriptor(self._levels[(currentLevel + 1)])
        else:
            return


class ObjectLevelDescriptor(object):

    def __init__(self, config):
        self._config = config

    def getLevelID(self):
        return self._config.get(ObjectsConsts.OBJECT_LEVEL_ID, 0)

    def getLevelPrice(self):
        return self._config.get(ObjectsConsts.OBJECT_LEVEL_PRICE, {})

    def getLevelPoints(self):
        return self._config.get(ObjectsConsts.OBJECT_LEVEL_POINTS, 0)

    def getLevelToken(self):
        return self._config.get(ObjectsConsts.OBJECT_LEVEL_TOKEN, None)