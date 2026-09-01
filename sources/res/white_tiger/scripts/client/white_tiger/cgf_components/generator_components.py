from __future__ import absolute_import
from cgf_script.registration import registerComponent

@registerComponent
class WTGeneratorActivationComponent(object):

    def __init__(self, genGO):
        super(WTGeneratorActivationComponent, self).__init__()
        self.generatorGO = genGO
        self.wasDamaged = False


@registerComponent
class WTGeneratorCapturedComponent(object):

    def __init__(self, vehiclesIDs):
        super(WTGeneratorCapturedComponent, self).__init__()
        self.vehiclesIDs = vehiclesIDs