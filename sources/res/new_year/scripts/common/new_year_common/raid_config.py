

class RaidConfig(object):
    __slots__ = ('_config', )

    def __init__(self, config=None):
        self._config = config or {}

    def isEnabled(self):
        return self._config.get('isEnabled', False)

    def getTamagotchiUrl(self):
        return self._config.get('tamagotchiUrl')

    def getRaidBoost(self):
        return self._config.get('raidBoost')