from __future__ import absolute_import
from helpers.dependency import instance
from journey_marathon.skeletons.game_control import IJourneyMarathonController

def jmCtrl():
    return instance(IJourneyMarathonController)