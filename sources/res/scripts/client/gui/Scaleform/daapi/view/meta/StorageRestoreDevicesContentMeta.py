from gui.Scaleform.daapi.view.lobby.storage.inventory.opt_devices_tab import OptDevicesTabView

class StorageRestoreDevicesContentMeta(OptDevicesTabView):

    def restoreItem(self, itemId, reason):
        self._printOverrideError('restoreItem')