from __future__ import absolute_import
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.pub import ViewImpl

class MinorTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.mono.vehicle_hub.tooltips.minor_tooltip(), model=ViewModel())
        super(MinorTooltip, self).__init__(settings)