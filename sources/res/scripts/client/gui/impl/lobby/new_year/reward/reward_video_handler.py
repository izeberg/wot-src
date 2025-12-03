from gui.impl.new_year.sounds_helper.video_handler import VideoStartStopHandler
from shared_utils import CONST_CONTAINER

class _PetRewardVideoStates(CONST_CONTAINER):
    GROUP = 'STATE_video_overlay'
    START = 'STATE_video_overlay_on'
    DONE = 'STATE_video_overlay_off'


class _PetRewardVideoEvents(CONST_CONTAINER):
    VIDEO_DAY_START = 'hangar_newyear_dog_reward_day_start'
    VIDEO_NIGHT_START = 'hangar_newyear_dog_reward_night_start'
    VIDEO_DONE = 'hangar_newyear_dog_reward_stop'
    VIDEO_PAUSE = 'hangar_newyear_dog_reward_pause'
    VIDEO_RESUME = 'hangar_newyear_dog_reward_resume'


class PetRewardVideoStartStopHandler(VideoStartStopHandler):
    _videoStates = _PetRewardVideoStates
    _videoSoundEvents = _PetRewardVideoEvents

    def onVideoStart(self, isDayHangar=True):
        self.onVideoStartEvent(self._videoSoundEvents.VIDEO_DAY_START if isDayHangar else self._videoSoundEvents.VIDEO_NIGHT_START)