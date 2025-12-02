from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.markers.ny_total_resource_marker_model import NyTotalResourceMarkerModel, MarkerType
from gui.impl.lobby.new_year.markers.ho_hangar_marker_view import HOHangarMarkerView
from gui.impl.new_year.navigation import NewYearNavigation
from new_year.ny_resource_collecting_helper import getAvgResourcesByCollecting, isCollectingAvailable, getCollectingCooldownTime
from new_year.ny_helper import getNYGeneralConfig
from helpers import dependency, time_utils
from new_year.ny_constants import NYObjects, RESOURCES_ORDER
from skeletons.new_year import IFriendServiceController, INewYearController

class HOTotalResourceMarkerView(HOHangarMarkerView):
    __friendService = dependency.descriptor(IFriendServiceController)
    __nyController = dependency.descriptor(INewYearController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops_marker.ho_total_resource_marker())
        settings.model = NyTotalResourceMarkerModel()
        settings.args = args
        settings.kwargs = kwargs
        super(HOTotalResourceMarkerView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(HOTotalResourceMarkerView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(HOTotalResourceMarkerView, self)._onLoading(*args, **kwargs)
        self.__updateMarker()

    def _getEvents(self):
        events = super(HOTotalResourceMarkerView, self)._getEvents()
        return events + (
         (
          self._objectObserver.onObjectStateChanged, self.__onObjectStateChanged),
         (
          self.__nyController.resourceCollecting.onSwitchCollectingState, self.__onSwitchCollectingState),
         (
          self.__friendService.onSwitchFriendCollectingState, self.__onSwitchCollectingState),
         (
          self.__friendService.onFriendHangarEnter, self.__onFriendHangar),
         (
          self.__friendService.onFriendHangarExit, self.__onFriendHangar),
         (
          self.__friendService.onBestFriendsUpdated, self.__onFriendHangar))

    def __onObjectStateChanged(self, _):
        self.__updateMarker()

    def __updateMarker(self):
        with self.viewModel.transaction() as (model):
            model.setAmount(getAvgResourcesByCollecting() * len(RESOURCES_ORDER))
            model.setMarkerType(MarkerType.FRIEND if self.__friendService.isInFriendHangar else MarkerType.DEFAULT)
            model.setIsDisabled(not isCollectingAvailable())

    def _canShowMarkers--- This code section failed: ---

 L.  59         0  LOAD_GLOBAL           0  'getCollectingCooldownTime'
                3  CALL_FUNCTION_0       0  None
                6  STORE_FAST            1  'cooldownTime'

 L.  60         9  LOAD_GLOBAL           1  'getNYGeneralConfig'
               12  CALL_FUNCTION_0       0  None
               15  LOAD_ATTR             2  'getEventEndTime'
               18  CALL_FUNCTION_0       0  None
               21  LOAD_GLOBAL           3  'time_utils'
               24  LOAD_ATTR             4  'getServerUTCTime'
               27  CALL_FUNCTION_0       0  None
               30  BINARY_SUBTRACT  
               31  STORE_FAST            2  'eventEndTimeTill'

 L.  62        34  LOAD_FAST             0  'self'
               37  LOAD_ATTR             5  '__friendService'
               40  LOAD_ATTR             6  'isInFriendHangar'
               43  STORE_FAST            3  'isInFriendHangar'

 L.  63        46  LOAD_FAST             0  'self'
               49  LOAD_ATTR             5  '__friendService'
               52  LOAD_ATTR             7  'friendHangarSpaId'
               55  LOAD_FAST             0  'self'
               58  LOAD_ATTR             5  '__friendService'
               61  LOAD_ATTR             8  'bestFriendList'
               64  COMPARE_OP            6  in
               67  STORE_FAST            4  'isBestFriend'

 L.  64        70  LOAD_FAST             0  'self'
               73  LOAD_ATTR             5  '__friendService'
               76  LOAD_ATTR             9  'getFriendCollectingCooldownTime'
               79  CALL_FUNCTION_0       0  None
               82  STORE_FAST            5  'friendCooldown'

 L.  66        85  LOAD_GLOBAL          10  'super'
               88  LOAD_GLOBAL          11  'HOTotalResourceMarkerView'
               91  LOAD_FAST             0  'self'
               94  CALL_FUNCTION_2       2  None
               97  LOAD_ATTR            12  '_canShowMarkers'
              100  CALL_FUNCTION_0       0  None
              103  JUMP_IF_FALSE_OR_POP   137  'to 137'

 L.  67       106  LOAD_FAST             3  'isInFriendHangar'
              109  POP_JUMP_IF_FALSE   128  'to 128'
              112  LOAD_FAST             4  'isBestFriend'
              115  JUMP_IF_FALSE_OR_POP   137  'to 137'
              118  LOAD_FAST             5  'friendCooldown'
              121  LOAD_FAST             2  'eventEndTimeTill'
              124  COMPARE_OP            0  <
              127  RETURN_END_IF    
            128_0  COME_FROM           115  '115'
            128_1  COME_FROM           109  '109'
              128  LOAD_FAST             1  'cooldownTime'
              131  LOAD_FAST             2  'eventEndTimeTill'
              134  COMPARE_OP            0  <
            137_0  COME_FROM           103  '103'
              137  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `RETURN_END_IF' instruction at offset 127

    def _setMarkerVisible(self, value):
        with self.viewModel.transaction() as (model):
            model.setIsVisible(value and NewYearNavigation.getCurrentObject() != NYObjects.RESOURCES)

    def __onSwitchCollectingState(self, _):
        self.__updateMarker()

    def __onFriendHangar(self, *_):
        self.__updateMarker()# Decompile failed :(