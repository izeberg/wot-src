from gui.Scaleform.daapi.view.battle.shared.messages import VehicleMessages
from gui.doc_loaders import messages_panel_reader
_VEHICLE_MESSAGES_FILE = 'gui/wt_vehicle_messages_panel.xml'

class WTVehicleMessages(VehicleMessages):

    def _populate(self):
        super(WTVehicleMessages, self)._populate()
        _, _, messages = messages_panel_reader.readXML(_VEHICLE_MESSAGES_FILE)
        self._messages.update(messages)