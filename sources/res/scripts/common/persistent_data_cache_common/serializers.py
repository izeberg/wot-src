import abc, typing, wg_pickle
if typing.TYPE_CHECKING:
    from persistent_data_cache_common.types import TData

class ISerializer(object):
    __slots__ = ()
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def deserialize(self, serializedData):
        pass

    @abc.abstractmethod
    def serialize(self, rawData):
        pass

    @abc.abstractmethod
    def rollbackSideEffects(self):
        pass


class WGPickleSerializer(ISerializer):
    __slots__ = ()

    def deserialize(self, serializedData):
        return wg_pickle.loads(serializedData)

    def serialize(self, rawData):
        return wg_pickle.dumps(rawData)

    def rollbackSideEffects(self):
        pass


defaultSerializer = WGPickleSerializer()