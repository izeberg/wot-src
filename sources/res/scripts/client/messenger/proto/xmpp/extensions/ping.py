from __future__ import absolute_import
from messenger.proto.xmpp.extensions import PyQuery, PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.gloox_constants import IQ_TYPE

class PingExtension(PyExtension):

    def __init__(self):
        super(PingExtension, self).__init__(_TAG.PING)
        self.setXmlNs(_NS.PING)


class PingQuery(PyQuery):

    def __init__(self, to):
        super(PingQuery, self).__init__(IQ_TYPE.GET, PingExtension(), to)