import CGF
from cgf_components.marker_component import MarkerType
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery
from helpers.events_handler import EventsHandler
from new_year.skeletons.new_year import ITamagotchiDataProvider, INewYearController
from new_year.gui.shared.ny_machine_helper import isMachineEnabled
from helpers import dependency

@registerComponent
class ObjectLobbyMarker(object):
    domain = CGF.DomainOption.DomainClient
    createType = ComponentProperty(type=CGFMetaTypes.STRING, editorName='creation method type', value=MarkerType.RACCOON, annotations={'comboBox': {MarkerType.RACCOON: MarkerType.RACCOON, 
                    MarkerType.MACHINE: MarkerType.MACHINE, 
                    MarkerType.QUESTS: MarkerType.QUESTS}})


class ObjectLobbyMarkersManager(CGF.ComponentManager, EventsHandler):
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _nyController = dependency.descriptor(INewYearController)

    @property
    def _componentConditionsTypeMap(self):
        return {MarkerType.RACCOON: self._isRaccoonVisible, 
           MarkerType.MACHINE: self._isMachineVisible, 
           MarkerType.QUESTS: self._isQuestsVisible}

    def activate(self):
        self._subscribe()

    def deactivate(self):
        self._unsubscribe()

    def _getEvents(self):
        return (
         (
          self._nyController.onNySettingsChanged, self._onStateUpdated),
         (
          self._nyController.onOnboardingFinished, self._onStateUpdated),
         (
          self._dataProvider.onRaccoonStateUpdated, self._onStateUpdated))

    @onAddedQuery(CGF.GameObject, ObjectLobbyMarker)
    def handleMarkerAdded(self, go, marker):
        for child in CGF.HierarchyManager(self.spaceID).getChildrenIncludingInactive(go):
            self._setMarkerActive(child, self._isMarkerVisible(marker.createType))

    def _update(self):
        for go, marker in CGF.Query(self.spaceID, (CGF.GameObject, ObjectLobbyMarker)):
            for child in CGF.HierarchyManager(self.spaceID).getChildrenIncludingInactive(go):
                self._setMarkerActive(child, self._isMarkerVisible(marker.createType))

    @staticmethod
    def _setMarkerActive(marker, isVisible):
        if isVisible:
            marker.activate()
        else:
            marker.deactivate()

    def _isMarkerVisible(self, createType):
        condition = self._componentConditionsTypeMap.get(createType, lambda : False)
        return condition()

    def _isRaccoonVisible(self):
        return self._dataProvider.raccoonState

    def _isMachineVisible(self):
        return self._nyController.isOnboardingFinished() and isMachineEnabled()

    def _isQuestsVisible(self):
        return self._nyController.isOnboardingFinished()

    def _onStateUpdated(self, *_):
        self._update()