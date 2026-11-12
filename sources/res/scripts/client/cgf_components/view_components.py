import logging, CGF, GUI, Math, re
from GFViewTextureControl import GFViewTextureControlComponent, process3DMouseViewEvent
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, tickGroup
from frameworks.wulf import WindowFlags, MouseEventType, MouseButton
from gui.impl.gen import R
from skeletons.gui.impl import IGuiLoader
from helpers import dependency
from frameworks.wulf import ViewStatus
from skeletons.gui.shared.utils import IHangarSpace
from constants import IS_CLIENT
from hover_component import IsHoveredComponent, SelectionComponent, IsExternalHoveredComponent
if IS_CLIENT:
    from AvatarInputHandler import cameras
_logger = logging.getLogger(__name__)

@registerComponent
class ViewComponent(object):
    domain = CGF.DomainOption.DomainClient
    layoutID = ComponentProperty(type=CGFMetaTypes.INT, value=R.invalid())
    uniqueID = ComponentProperty(type=CGFMetaTypes.INT, value=0)
    active = ComponentProperty(type=CGFMetaTypes.BOOL, value=True)

    def __init__(self, view):
        super(ViewComponent, self).__init__()
        self.layoutID = view.layoutID
        self.uniqueID = view.uniqueID
        self.view = view


def parseLayoutPath(path):
    return R.views.recursiveDyn(re.split('[\\\\/]', path))()


class ViewTextureControlManager(CGF.ComponentManager):
    __guiLoader = dependency.descriptor(IGuiLoader)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, *args):
        super(ViewTextureControlManager, self).__init__(*args)
        self.__controlCompByTextureName = {}
        self.__controlCompByViewId = {}
        self.__viewIdByControlComp = {}

    def activate(self):
        self.__guiLoader.windowsManager.onViewStatusChanged += self.__onViewStatusChanged
        self.__hangarSpace.onMouseDown += self._onMouseDown
        self.__hangarSpace.onMouseUp += self._onMouseUp

    def deactivate(self):
        self.__guiLoader.windowsManager.onViewStatusChanged -= self.__onViewStatusChanged
        self.__hangarSpace.onMouseDown -= self._onMouseDown
        self.__hangarSpace.onMouseUp -= self._onMouseUp
        self.__controlCompByTextureName = {}
        self.__controlCompByViewId = {}
        self.__viewIdByControlComp = {}

    @onAddedQuery(CGF.GameObject, GFViewTextureControlComponent)
    def onSyncCreated(self, go, controlComponent):
        _logger.debug('onControlCreated %s %s', controlComponent.getViewLayoutPath(), controlComponent.getTexturePath())
        self.__controlCompByTextureName[controlComponent.getTexturePath()] = controlComponent
        layoutID = parseLayoutPath(controlComponent.getViewLayoutPath())
        views = self.__guiLoader.windowsManager.getViewsByLayout(layoutID)
        for view in views:
            window = view.getWindow()
            if not window or not window.windowFlags & WindowFlags.SURFACE:
                continue
            if window.proxy.name == controlComponent.getTexturePath():
                controlComponent.setView(view.proxy)
                self.__connect(view.uniqueID, controlComponent)
                break

    @onRemovedQuery(CGF.GameObject, GFViewTextureControlComponent)
    def onSyncDeleted(self, go, controlComponent):
        controlComponent.setView(None)
        viewId = self.__viewIdByControlComp.get(controlComponent)
        self.__disconnect(viewId, controlComponent)
        key = controlComponent.getTexturePath()
        if key in self.__controlCompByTextureName:
            del self.__controlCompByTextureName[key]
        return

    @onRemovedQuery(GFViewTextureControlComponent, IsHoveredComponent, SelectionComponent)
    def onMouseLeave(self, controlComponent, _, __):
        process3DMouseViewEvent(self.spaceID, controlComponent, MouseEventType.MOUSE_LEAVE, MouseButton.NONE, Math.Vector3(), Math.Vector3())

    @tickGroup(groupName='PostHierarchy')
    def tick(self):
        self.__proccessMouseEvent(MouseEventType.MOUSE_MOVE, MouseButton.NONE)

    def _onMouseDown(self):
        self.__proccessMouseEvent(MouseEventType.MOUSE_DOWN, MouseButton.LEFT)

    def _onMouseUp(self):
        self.__proccessMouseEvent(MouseEventType.MOUSE_UP, MouseButton.LEFT)

    def __onViewStatusChanged(self, uniqueID, newState):
        if newState == ViewStatus.LOADING:
            view = self.__guiLoader.windowsManager.getView(uniqueID)
            window = view.getWindow()
            if not window or not window.windowFlags & WindowFlags.SURFACE:
                return
            controlComponent = self.__controlCompByTextureName.get(window.proxy.name)
            if not controlComponent:
                return
            controlComponent.setView(view.proxy)
            self.__connect(uniqueID, controlComponent)
        elif newState == ViewStatus.DESTROYING:
            controlComponent = self.__controlCompByViewId.get(uniqueID)
            if controlComponent:
                controlComponent.setView(None)
                self.__disconnect(uniqueID, controlComponent)
        return

    def __connect(self, viewId, controlComponent):
        self.__controlCompByViewId[viewId] = controlComponent
        self.__viewIdByControlComp[controlComponent] = viewId

    def __disconnect(self, viewId, controlComponent):
        if viewId in self.__controlCompByViewId:
            del self.__controlCompByViewId[viewId]
        if controlComponent in self.__viewIdByControlComp:
            del self.__viewIdByControlComp[controlComponent]

    def __proccessMouseEvent(self, mouseEventType, mouseButton):
        hoverQuery = CGF.Query(self.spaceID, (
         GFViewTextureControlComponent, IsHoveredComponent, SelectionComponent, CGF.No(IsExternalHoveredComponent)))
        if hoverQuery.empty():
            return
        cursorPosition = GUI.mcursor().position
        ray, wpoint = cameras.getWorldRayAndPoint(cursorPosition.x, cursorPosition.y)
        for controlComponent, _, __ in hoverQuery:
            process3DMouseViewEvent(self.spaceID, controlComponent, mouseEventType, mouseButton, wpoint, ray)