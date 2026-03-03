from __future__ import absolute_import
from fun_random.gui.feature.configs.providers.fun_mode_configuration import FunModeConfigurationProvider
from fun_random.gui.feature.configs.providers.fun_sub_mode_configuration import FunSubModeConfigurationProvider

def initConfigurationsCache():
    FunModeConfigurationProvider.initConfigurationsCache()
    FunSubModeConfigurationProvider.initConfigurationsCache()