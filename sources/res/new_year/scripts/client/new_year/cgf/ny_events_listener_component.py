import CGF
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from skeletons.gui.game_control import IPlatoonController
from PlayerEvents import g_playerEvents
from Sound import Sound3DComponent
from helpers import dependency

@registerComponent
class NyEventsListenerComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'NY Actions Listener'
    category = 'New Year'
    fightSound = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Fight 3D Sound Component', value=Sound3DComponent)
    fightStopSound = ComponentProperty(type=CGFMetaTypes.LINK, editorName='Fight Stop 3D Sound Component', value=Sound3DComponent)

    def playFightSound(self):
        self.__playLinkedSound(self.fightSound)

    def playFightStopSound(self):
        self.__playLinkedSound(self.fightStopSound)

    @staticmethod
    def __playLinkedSound(soundLink):
        sound = soundLink()
        if sound is not None:
            sound.play()
        return


class NewYearEventsListenerManager(CGF.ComponentManager):
    __platoonController = dependency.descriptor(IPlatoonController)

    def __init__(self, *args):
        super(NewYearEventsListenerManager, self).__init__(*args)
        self.__wasFightActive = False
        self.__fightSoundStarted = False

    def activate(self):
        self.__wasFightActive = self.__isPlatoonFightActive()
        self.__fightSoundStarted = False
        g_playerEvents.onEnqueued += self.__onSingleFightClick
        g_playerEvents.onDequeued += self.__onSingleFightLeave
        g_playerEvents.onKickedFromQueue += self.__onSingleFightLeave
        self.__platoonController.onMembersUpdate += self.__onPlatoonMembersUpdate

    def deactivate(self):
        g_playerEvents.onEnqueued -= self.__onSingleFightClick
        g_playerEvents.onDequeued -= self.__onSingleFightLeave
        g_playerEvents.onKickedFromQueue -= self.__onSingleFightLeave
        self.__platoonController.onMembersUpdate -= self.__onPlatoonMembersUpdate
        self.__fightSoundStarted = False

    def __broadcastFightSound(self):
        if self.__fightSoundStarted:
            return
        for listener in CGF.Query(self.spaceID, NyEventsListenerComponent):
            listener.playFightSound()
            self.__fightSoundStarted = True

    def __broadcastFightStopSound(self):
        if not self.__fightSoundStarted:
            return
        for listener in CGF.Query(self.spaceID, NyEventsListenerComponent):
            listener.playFightStopSound()

        self.__fightSoundStarted = False

    def __onSingleFightClick(self, *_):
        self.__broadcastFightSound()

    def __onSingleFightLeave(self, *_):
        self.__broadcastFightStopSound()

    def __onPlatoonMembersUpdate(self, *_):
        isFightActive = self.__isPlatoonFightActive()
        if isFightActive == self.__wasFightActive:
            return
        if isFightActive:
            self.__broadcastFightSound()
        else:
            self.__broadcastFightStopSound()
        self.__wasFightActive = isFightActive

    def __isPlatoonFightActive(self):
        return self.__platoonController.isInQueue() or self.__platoonController.isInSearch()