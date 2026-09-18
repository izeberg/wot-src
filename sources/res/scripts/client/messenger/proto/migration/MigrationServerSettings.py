from __future__ import absolute_import
from messenger.proto.interfaces import IProtoSettings

class MigrationServerSettings(IProtoSettings):

    def isEnabled(self):
        return True