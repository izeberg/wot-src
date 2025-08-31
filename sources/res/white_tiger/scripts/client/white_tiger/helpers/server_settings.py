from collections import namedtuple

class WhiteTigerConfig(namedtuple('WhiteTigerConfig', ('isEnabled', 'peripheryIDs', 'primeTimes', 'seasons',
                                'cycleTimes', 'squadConfig'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, primeTimes={}, seasons={}, cycleTimes={}, squadConfig={})
        defaults.update(kwargs)
        return super(WhiteTigerConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()