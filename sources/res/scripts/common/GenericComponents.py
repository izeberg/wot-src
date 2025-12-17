import enum
COMPOSITION_ROOT_SLOT_NAME = 'compositionRootSlot'

class TransformComponent:

    def __init__(self, matrix):
        pass


class EHealthGradation(enum.Enum):
    RED_ZONE = 'RED_ZONE'
    YELLOW_ZONE = 'YELLOW_ZONE'
    GREEN_ZONE = 'GREEN_ZONE'


class HealthGradationComponent:

    def __init__(self, redHealth, yellowHealth):
        self.__redHealth = redHealth
        self.__yellowHealth = yellowHealth

    def getHealthZone(self, health, maxHealth):
        if health < maxHealth * self.__redHealth / 100:
            return EHealthGradation.RED_ZONE
        if health < maxHealth * self.__yellowHealth / 100:
            return EHealthGradation.YELLOW_ZONE
        return EHealthGradation.GREEN_ZONE


class CyclicActivatorComponent(object):
    pass