from __future__ import absolute_import

class IMetaTabState(object):

    @property
    def tabId(self):
        raise NotImplementedError