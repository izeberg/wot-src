from collections import namedtuple
VehicleAppearanceCacheInfo = namedtuple('VehicleAppearanceCacheInfo', ('typeDescr',
                                                                       'health',
                                                                       'isCrewActive',
                                                                       'isTurretDetached',
                                                                       'outfitCD',
                                                                       'forceDynAttachmentLoading',
                                                                       'entityGameObject'))