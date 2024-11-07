

class VehicleAppearanceComponent(object):
    appearance = property(lambda self: self.__appearance)

    def __init__(self, appearance):
        self.__appearance = appearance