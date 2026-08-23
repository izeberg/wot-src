from __future__ import absolute_import
import logging
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_lore_overlay_view_model import JmLoreOverlayViewModel
from journey_marathon.jm_helpers import jmCtrl
_logger = logging.getLogger(__name__)

class JmLoreOverlayWindow(WindowImpl):

    def __init__(self, nodeId):
        super(JmLoreOverlayWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=JmLoreOverlayView(nodeId))


class JmLoreOverlayView(ViewImpl):

    def __init__(self, *args, **kwargs):
        super(JmLoreOverlayView, self).__init__(ViewSettings(R.views.journey_marathon.mono.lobby.lore_view(), ViewFlags.VIEW, JmLoreOverlayViewModel(), args=args, kwargs=kwargs))

    @property
    def viewModel(self):
        return super(JmLoreOverlayView, self).getViewModel()

    def _getEvents(self):
        return (
         (
          self.getViewModel().onClose, self.destroyWindow),)

    def _onLoading(self, nodeId, *args, **kwargs):
        super(JmLoreOverlayView, self)._onLoading(*args, **kwargs)
        node = jmCtrl().jmNodes.getJmNodes().get(nodeId)
        if node is None:
            _logger.error('There is no node with id %s', nodeId)
            return
        else:
            with self.viewModel.transaction() as (tx):
                tx.setNodeId(nodeId)
            return