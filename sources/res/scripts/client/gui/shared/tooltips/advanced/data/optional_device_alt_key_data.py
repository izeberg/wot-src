from gui.shared.tooltips.advanced.data.default_alt_key_data import DefaultAltKeyData

class OptionalDeviceAltKeyData(DefaultAltKeyData):

    @staticmethod
    def _getHeader(item, mechanicName):
        return item.shortUserName