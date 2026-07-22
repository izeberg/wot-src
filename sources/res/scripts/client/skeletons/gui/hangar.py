

class ICarouselEventEntry(object):

    @staticmethod
    def getIsActive(state):
        raise NotImplementedError


class IBattleModifiersEntry(object):

    @classmethod
    def getIsActive(cls):
        raise NotImplementedError