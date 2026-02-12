from __future__ import absolute_import
import typing

class IVehiclePlaylistsGuiHelper(object):

    @classmethod
    def isPlaylistsSupported(cls):
        raise NotImplementedError


class EmptyVehiclePlaylistsGuiHelper(IVehiclePlaylistsGuiHelper):

    @classmethod
    def isPlaylistsSupported(cls):
        return


class DefaultVehiclePlaylistsGuiHelper(IVehiclePlaylistsGuiHelper):

    @classmethod
    def isPlaylistsSupported(cls):
        return False


class RandomVehiclePlaylistsGuiHelper(IVehiclePlaylistsGuiHelper):

    @classmethod
    def isPlaylistsSupported(cls):
        return True