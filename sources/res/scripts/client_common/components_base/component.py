from __future__ import absolute_import
from future.utils import with_metaclass
from components_base.auto_properties import AutoPropertyInitMetaclass

class Component(with_metaclass(AutoPropertyInitMetaclass, object)):

    def activate(self):
        pass

    def deactivate(self):
        pass

    def destroy(self):
        pass