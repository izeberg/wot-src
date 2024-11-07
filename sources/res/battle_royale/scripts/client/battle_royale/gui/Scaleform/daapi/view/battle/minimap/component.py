import logging, plugins
from gui.Scaleform.daapi.view.battle.epic.minimap import EpicMinimapComponent
_logger = logging.getLogger(__name__)

class BattleRoyaleMinimapComponent(EpicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(BattleRoyaleMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup[plugins.PERSONAL_PLUGIN] = plugins.BattleRoyalePersonalEntriesPlugin
        setup[plugins.DEATH_ZONES_PLUGIN] = plugins.DeathZonesPlugin
        setup[plugins.RADAR_PLUGIN] = plugins.RadarPlugin
        setup[plugins.DETECTOR_PLUGIN] = plugins.DetectorPlugin
        setup[plugins.AIRDROP_PLUGIN] = plugins.AirDropPlugin
        setup[plugins.VEHICLES_PLUGIN] = plugins.BattleRoyaleVehiclePlugin
        setup[plugins.PINGING_PLUGIN] = plugins.BattleRoyalMinimapPingPlugin
        return setup