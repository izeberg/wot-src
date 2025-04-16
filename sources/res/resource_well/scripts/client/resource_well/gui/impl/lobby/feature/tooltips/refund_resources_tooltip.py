from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from resource_well.gui.impl.gen.view_models.views.lobby.tooltips.refund_resources_tooltip_model import RefundResourcesTooltipModel

class RefundResourcesTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.resource_well.lobby.feature.tooltips.RefundResourcesTooltip())
        settings.model = RefundResourcesTooltipModel()
        super(RefundResourcesTooltip, self).__init__(settings)