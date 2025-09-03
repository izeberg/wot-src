from collections import namedtuple
VehicleAppearanceCacheInfo = namedtuple('VehicleAppearanceCacheInfo', ('typeDescr',
                                                                       'health',
                                                                       'isCrewActive',
                                                                       'isTurretDetached',
                                                                       'outfitCD',
                                                                       'forceDynAttachmentLoading',
                                                                       'entityGameObject'))
VehicleAppearanceCacheInfo.__new__.__defaults__ = (
 None, 0, False, False, '', False)