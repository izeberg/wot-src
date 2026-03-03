from __future__ import absolute_import
from fun_random.gui.feature.configs import initConfigurationsCache
from fun_random.gui.feature.sub_modes import registerFunRandomSubModes

def registerFunRandomFeature():
    initConfigurationsCache()
    registerFunRandomSubModes()