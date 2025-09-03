from script_component.DynamicScriptComponent import DynamicScriptComponent

class WTGeneratorActivationComponent(object):

    def __init__(self, genGO):
        super(WTGeneratorActivationComponent, self).__init__()
        self.generatorGO = genGO
        self.wasDamaged = False


class WTGeneratorCapturedComponent(object):

    def __init__(self, vehiclesIDs):
        super(WTGeneratorCapturedComponent, self).__init__()
        self.vehiclesIDs = vehiclesIDs


class WTGeneratorActivation(DynamicScriptComponent):

    def damaged(self):
        go = self.entity.entityGameObject
        activation = go.findComponentByType(WTGeneratorActivationComponent)
        if activation:
            activation.wasDamaged = True