import BigWorld, CGF, SoundGroups
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from cgf_components.highlight_component import HighlightComponent
from cgf_components.hover_component import SelectionComponent, IsHoveredComponent
from constants import IS_CLIENT
from helpers import dependency
from new_year.skeletons.new_year import INewYearMetricsLogger, INewYearController
from PlayerEvents import g_playerEvents
from skeletons.gui.game_control import IPlatoonController
DEFAULT_REQUIRED_CLICKS = 11
DEFAULT_CLICK_INTERVAL = 1.0

class NyClickBonusVideoIds(object):
    CLIP_1 = 'clip_1'
    CLIP_2 = 'clip_2'


if IS_CLIENT:
    from gui.impl.gen import R
    from new_year.helpers.ny_helpers import showEmbeddedAudioVideoView
    _VIDEO_CONFIG = {NyClickBonusVideoIds.CLIP_1: R.videos.new_year.clips.clip_1, 
       NyClickBonusVideoIds.CLIP_2: R.videos.new_year.clips.clip_2}

@registerComponent
class NyClickBonusVideoComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'NY Click Bonus Video'
    category = 'New Year'
    __uiLogger = dependency.descriptor(INewYearMetricsLogger)
    requiredClicks = ComponentProperty(type=CGFMetaTypes.INT, editorName='Required clicks', value=DEFAULT_REQUIRED_CLICKS)
    clickInterval = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName='Click interval (sec)', value=DEFAULT_CLICK_INTERVAL)
    videoId = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Video', value=NyClickBonusVideoIds.CLIP_1, annotations={'comboBox': {NyClickBonusVideoIds.CLIP_1: NyClickBonusVideoIds.CLIP_1, 
                    NyClickBonusVideoIds.CLIP_2: NyClickBonusVideoIds.CLIP_2}})
    hoverSound = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Hover sound', value='')
    clickSound = ComponentProperty(type=CGFMetaTypes.STRING, editorName='Click sound', value='')

    def __init__(self):
        super(NyClickBonusVideoComponent, self).__init__()
        self.__clickCount = 0
        self.__lastClickTime = 0.0
        self.__video = None
        return

    def clickAction(self):
        if self.clickSound:
            SoundGroups.g_instance.playSound2D(self.clickSound)
        if self.__video is not None:
            return
        else:
            now = BigWorld.time()
            if self.__clickCount > 0 and now - self.__lastClickTime > self.clickInterval:
                self.__clickCount = 0
            self.__clickCount += 1
            self.__lastClickTime = now
            if self.__clickCount >= self.requiredClicks:
                self.__clickCount = 0
                self.__showVideo()
            return

    def hoverAction(self):
        if self.hoverSound:
            SoundGroups.g_instance.playSound2D(self.hoverSound)

    def destroy(self):
        self.__stopVideo(destroy=True)

    def __showVideo(self):
        videoSourceAccessor = _VIDEO_CONFIG.get(self.videoId)
        if videoSourceAccessor is None:
            return
        else:
            self.__uiLogger.logEasterEggVideoOpened(self.videoId)
            self.__video = showEmbeddedAudioVideoView(videoSource=videoSourceAccessor(), onVideoClosed=self.__onVideoClosed, isControlsVisible=False)
            return

    def __onVideoClosed(self):
        self.__stopVideo()

    def __stopVideo(self, destroy=False):
        video = self.__video
        self.__video = None
        if destroy and video is not None:
            video.destroy()
        return


class NewYearClickBonusVideoManager(CGF.ComponentManager):
    __platoonController = dependency.descriptor(IPlatoonController)
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, *args):
        super(NewYearClickBonusVideoManager, self).__init__(*args)
        self.__wasFightActive = False

    def activate(self):
        self.__wasFightActive = self.__isPlatoonFightActive()
        if self.__wasFightActive:
            self.__stopAllVideos()
        g_playerEvents.onEnqueued += self.__onSingleFightStarted
        self.__platoonController.onMembersUpdate += self.__onPlatoonMembersUpdate
        self.__nyController.onOnboardingFinished += self.__updateSelectionActive
        self.__updateSelectionActive()

    def deactivate(self):
        g_playerEvents.onEnqueued -= self.__onSingleFightStarted
        self.__platoonController.onMembersUpdate -= self.__onPlatoonMembersUpdate
        self.__nyController.onOnboardingFinished -= self.__updateSelectionActive

    @onAddedQuery(NyClickBonusVideoComponent, CGF.GameObject, SelectionComponent)
    def handleClickBonusAdded(self, clickBonusComp, gameObject, selectionComp):
        selectionComp.onClickAction += clickBonusComp.clickAction
        if not self.__isSelectionActive():
            gameObject.removeComponentByType(SelectionComponent)

    @onRemovedQuery(NyClickBonusVideoComponent, SelectionComponent)
    def handleClickBonusRemoved(self, clickBonusComp, selectionComp):
        selectionComp.onClickAction -= clickBonusComp.clickAction
        clickBonusComp.destroy()

    @onAddedQuery(NyClickBonusVideoComponent, IsHoveredComponent)
    def handleClickBonusHover(self, clickBonusComp, _):
        clickBonusComp.hoverAction()

    @onAddedQuery(NyClickBonusVideoComponent, CGF.GameObject, HighlightComponent)
    def onClickBonusOutlineAdded(self, _, gameObject, highlight):
        isActive = self.__isSelectionActive()
        highlight.isActive = isActive
        self.__setSelection(gameObject, isActive)

    def __onSingleFightStarted(self, *_):
        self.__stopAllVideos()

    def __onPlatoonMembersUpdate(self, *_):
        isFightActive = self.__isPlatoonFightActive()
        if isFightActive == self.__wasFightActive:
            return
        self.__wasFightActive = isFightActive
        if isFightActive:
            self.__stopAllVideos()

    def __stopAllVideos(self):
        for clickBonusComp in CGF.Query(self.spaceID, NyClickBonusVideoComponent):
            clickBonusComp.destroy()

    def __isPlatoonFightActive(self):
        return self.__platoonController.isInQueue() or self.__platoonController.isInSearch()

    def __isSelectionActive(self):
        return self.__nyController.isOnboardingFinished()

    def __updateSelectionActive(self, *_):
        query = CGF.Query(self.spaceID, (CGF.GameObject, NyClickBonusVideoComponent, HighlightComponent))
        for go, _, highlight in query:
            isActive = self.__isSelectionActive()
            if highlight.isActive != isActive:
                self.__setSelection(go, isActive)
            highlight.isActive = isActive

    @staticmethod
    def __setSelection(go, isActive):
        hasSelection = go.findComponentByType(SelectionComponent) is not None
        if not isActive and hasSelection:
            go.removeComponentByType(SelectionComponent)
        elif isActive and not hasSelection:
            go.createComponent(SelectionComponent)
        return