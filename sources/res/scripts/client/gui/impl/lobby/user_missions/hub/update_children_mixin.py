from future.utils import iteritems
from gui.impl.pub.view_component import ViewComponent

class UpdateChildrenMixin(ViewComponent):

    def update(self):
        for _, child in iteritems(self._childrenByUid):
            if isinstance(child, UpdateChildrenMixin):
                child.update()