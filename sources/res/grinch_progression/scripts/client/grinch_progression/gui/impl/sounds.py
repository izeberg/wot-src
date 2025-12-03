from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class GrinchProgressionSound(CONST_CONTAINER):
    STATE_GROUP = 'STATE_ext_hangar_newyear_place'
    STATE_GAMEMODE = 'STATE_ext_hangar_newyear_place_gamemode'
    GAMEMODE_ENTER = 'hangar_newyear_gamemode_enter'
    GAMEMODE_EXIT = 'hangar_newyear_gamemode_exit'


GAME_BOARD_SOUND_SPACE = CommonSoundSpaceSettings(name='game_board', entranceStates={GrinchProgressionSound.STATE_GROUP: GrinchProgressionSound.STATE_GAMEMODE}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=GrinchProgressionSound.GAMEMODE_ENTER, exitEvent=GrinchProgressionSound.GAMEMODE_EXIT)