from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    JM_MAP_STATE = 'STATE_ext_jm'
    JM_MAP_STATE_ON = 'STATE_ext_jm_on'
    JM_MAP_STATE_OFF = 'STATE_ext_jm_off'
    JM_MAP_EVENT_ENTER = 'ev_journey_marathon_enter'
    JM_MAP_EVENT_EXIT = 'ev_journey_marathon_exit'


JM_MAP_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.JM_MAP_STATE, entranceStates={SOUNDS.JM_MAP_STATE: SOUNDS.JM_MAP_STATE_ON}, exitStates={SOUNDS.JM_MAP_STATE: SOUNDS.JM_MAP_STATE_OFF}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.JM_MAP_EVENT_ENTER, exitEvent=SOUNDS.JM_MAP_EVENT_EXIT)