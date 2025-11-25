from __future__ import absolute_import
from advent_calendar.gui.impl.gen.view_models.views.lobby.tooltips.simple_tooltip_model import SimpleTooltipModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class AdventCalendarSimpleTooltip(ViewImpl[SimpleTooltipModel]):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.advent_calendar.mono.lobby.tooltips.advent_calendar_simple_tooltip(), model=SimpleTooltipModel(), args=args, kwargs=kwargs)
        super(AdventCalendarSimpleTooltip, self).__init__(settings)

    def _onLoading(self, payload):
        with self.getViewModel().transaction() as (vm):
            vm.setPayload(payload)