from __future__ import absolute_import
import typing
from gui.impl.lobby.common.bonuses_layout_config_reader import BonusesLayout
if typing.TYPE_CHECKING:
    from typing import List, Iterable
    from gui.server_events.bonuses import SimpleBonus

class JmBonuses(object):
    __NODES_BONUSES_LAYOUT = 'journey_marathon/gui/jm_nodes_bonuses_layout.xml'
    __ANNIVERSARY_GIFT_LAYOUT = 'journey_marathon/gui/jm_anniversary_present_bonuses_layout.xml'

    def __init__(self):
        self.__nodesLayout = BonusesLayout(self.__NODES_BONUSES_LAYOUT)
        self.__anniversaryPresentLayout = BonusesLayout(self.__ANNIVERSARY_GIFT_LAYOUT)

    def init(self):
        self.__nodesLayout.init()
        self.__anniversaryPresentLayout.init()

    def fini(self):
        self.__nodesLayout.fini()
        self.__anniversaryPresentLayout.fini()

    def sortJmNodesBonuses(self, bonuses, reverse=True):
        return sorted(bonuses, key=self.__nodesLayout.getPriority, reverse=reverse)

    def sortJmAnniversaryPresentBonuses(self, bonuses, reverse=True):
        return sorted(bonuses, key=self.__anniversaryPresentLayout.getPriority, reverse=reverse)