from collections import namedtuple

class GrinchProgressionConfig(namedtuple('GrinchProgressionConfig', ('progressionTokenID', 'seasons'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(progressionTokenID=str, seasons={})
        defaults.update(kwargs)
        return super(GrinchProgressionConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()