from __future__ import absolute_import
import gui.impl.lobby.hangar.states as hangar, gui.impl.lobby.hangar.playlists_states as playlists

def registerStates(machine):
    hangar.registerStates(machine)
    playlists.registerStates(machine)


def registerTransitions(machine):
    hangar.registerTransitions(machine)