from gui.shared.event_dispatcher import showCustomizationResourceMainWindow
from helpers import dependency
from web.common import formatCustomizationResourceState
from web.web_client_api import W2CSchema, w2c, w2capi

@w2capi(name='customization_resource', key='action')
class CustomizationResourceWebApi(object):

    @w2c(W2CSchema, 'get_feature_state')
    def getFeatureState(self, _):
        return formatCustomizationResourceState()

    @w2c(W2CSchema, 'exchange')
    def exchange(self, _):
        showCustomizationResourceMainWindow()