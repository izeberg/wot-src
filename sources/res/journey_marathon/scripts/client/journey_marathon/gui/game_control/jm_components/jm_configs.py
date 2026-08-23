from __future__ import absolute_import
import logging, typing
from collections import Counter
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.shared.utils.functions import deepMergeDicts
from helpers.dependency import descriptor
from items import _xml
from journey_marathon.jm_helpers import jmCtrl
from journey_marathon.jm_helpers.jm_account_settings import updateJmAccountSettings
from journey_marathon_common.journey_marathon_constants import JM_GAME_PARAMS_KEY, PREFIX, SEPARATOR, JM_ANNIVERSARY_PRESENT_POSTFIX
from skeletons.gui.lobby_context import ILobbyContext
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Dict, Optional, Tuple, List
    from helpers.server_settings import ServerSettings
    Position = Tuple[(int, int)]
    Positions = List[Tuple[(str, Position)]]
_logger = logging.getLogger(__name__)

class JmConfig(object):
    __lobbyContext = descriptor(ILobbyContext)

    def __init__(self):
        self.__serverConfig = {}
        self.__clientConfig = ClientConfig()
        self.__nodeErrors = []
        self.__questTokenPrefix = ''
        self.__anniversaryPresentQuestId = ''
        self.__settings = None
        return

    def init(self):
        self.__serverConfig = _makeDefaultServerConfig()
        self.__clientConfig.read()
        self.__nodeErrors.extend(self.__clientConfig.getJmClientConfigErrors())
        self.__initSettings()

    def fini(self):
        self.__finiSettings()
        self.__settings = None
        self.__serverConfig.clear()
        self.__clientConfig.clear()
        del self.__nodeErrors[:]
        self.__questTokenPrefix = ''
        self.__anniversaryPresentQuestId = ''
        return

    def getJmStatuses(self):
        return (self.__serverConfig['isEnabled'], self.__serverConfig['isSuspended'])

    def getJmJourneyId(self):
        return self.__serverConfig['journeyId']

    def getJmNodesConfig(self):
        return self.__serverConfig['nodes']

    def getJMInfoPageUrl(self):
        return self.__serverConfig['infoPageUrl']

    def getJmClientConfig(self):
        return self.__clientConfig

    def getJmQuestTokenPrefix(self):
        return self.__questTokenPrefix

    def getJmAnniversaryPresentQuestId(self):
        return self.__anniversaryPresentQuestId

    def getJmConfigErrors(self):
        return self.__nodeErrors

    def getJmShopLink(self):
        return self.__serverConfig['shopLink']

    def __getJmDateTime(self):
        return (
         self.__serverConfig['startDateTime'], self.__serverConfig['finishDateTime'])

    def __initSettings(self, settings=None):
        lobbyCtx = self.__lobbyContext
        self.__settings = settings = settings or lobbyCtx.getServerSettings()
        lobbyCtx.onServerSettingsChanged += self.__onServerSettingsReset
        if settings is not None:
            settings.onServerSettingsChange += self.__onServerSettingsChange
            self.__updateServerConfig(settings.getSettings().get(JM_GAME_PARAMS_KEY))
        return

    def __finiSettings(self):
        self.__lobbyContext.onServerSettingsChanged -= self.__onServerSettingsReset
        if self.__settings is not None:
            self.__settings.onServerSettingsChange -= self.__onServerSettingsChange
        return

    def __onServerSettingsReset(self, serverSettings):
        self.__finiSettings()
        self.__initSettings(serverSettings)

    def __onServerSettingsChange(self, diff):
        if JM_GAME_PARAMS_KEY in diff:
            self.__updateServerConfig(diff[JM_GAME_PARAMS_KEY])

    def __updateServerConfig(self, newServerConfig):
        if newServerConfig is None:
            return
        else:
            serverConfig, diff = _mergeWithDefaultsAndMakeDiff(self.__serverConfig, newServerConfig, _makeDefaultServerConfig)
            if not diff:
                return
            self.__serverConfig = serverConfig
            journeyIdDiff = 'journeyId' in diff
            if journeyIdDiff:
                updateJmAccountSettings(diff['journeyId'])
            ctrl = jmCtrl()
            nodesDiff = 'nodes' in diff
            if nodesDiff:
                self.__nodeErrors.extend(_validateConfigs(self.__clientConfig, serverConfig))
                if self.__nodeErrors:
                    ctrl.onJmConfigErrors()
            if 'isEnabled' in diff or 'isSuspended' in diff:
                ctrl.jmSwitcher.invalidateJmFeatureState()
            if 'startDateTime' in diff or 'finishDateTime' in diff:
                ctrl.jmTime.invalidateJmDatesConfig(self.__getJmDateTime())
            if journeyIdDiff:
                self.__questTokenPrefix = qPrefix = PREFIX + SEPARATOR + diff['journeyId'] + SEPARATOR
                self.__anniversaryPresentQuestId = qPrefix + JM_ANNIVERSARY_PRESENT_POSTFIX
                ctrl.jmQuests.invalidateJmQuests()
            if journeyIdDiff or nodesDiff:
                ctrl.jmTokens.buildJmTokensFromConfig(journeyIdDiff, nodesDiff)
            if nodesDiff and not self.__nodeErrors:
                ctrl.jmNodes.invalidateJmNodesConfig()
            ctrl.onJmConfigChange(diff)
            return


def _makeDefaultServerConfig():
    return {'isEnabled': False, 
       'isSuspended': False, 
       'startDateTime': 0, 
       'finishDateTime': float('+inf'), 
       'journeyId': '', 
       'nodes': {}, 'infoPageUrl': '', 
       'shopLink': ''}


class ClientConfig(object):
    _PATH = 'journey_marathon/gui/jm_map_config.xml'

    def __init__(self):
        self.__nodesPos = {}
        self.__loresPos = {}
        self.__errors = []

    def clear(self):
        self.__nodesPos.clear()
        self.__loresPos.clear()
        del self.__errors[:]

    def read(self):
        self.clear()
        nodesPos, loresPos, errors = _readClientConfig(self._PATH)
        self.__nodesPos.update(nodesPos)
        self.__loresPos.update(loresPos)
        self.__errors[:] = errors

    def getJmClientConfigErrors(self):
        return self.__errors

    def getJmNodePositions(self):
        return self.__nodesPos

    def getJmLorePositions(self):
        return self.__loresPos

    def __repr__(self):
        return ('\n    ').join((
         'JmClientConfig(',
         'errors=%s' % self.__errors,
         'nodes=%s' % self.__nodesPos,
         'narrative=%s' % self.__loresPos))


def _mergeWithDefaultsAndMakeDiff(old, new, defaultMaker):
    newDict = defaultMaker()
    deepMergeDicts(newDict, new)
    newDiff = {}
    for k in newDict:
        oldValue = old.get(k)
        newValue = newDict.get(k)
        if oldValue != newValue:
            newDiff[k] = newValue

    return (
     newDict, newDiff)


def _validateConfigs(clientConfig, serverConfig):
    if 'nodes' not in serverConfig:
        return ['Must have section missing from server config = <nodes>']
    clientNodes = clientConfig.getJmNodePositions()
    serverNodes = serverConfig['nodes']
    errors = []

    def logAndStoreError(error):
        _logger.error(error)
        errors.append(error)

    for nodeId in clientNodes:
        if nodeId not in serverNodes:
            logAndStoreError('Client config has a node which is missing from the server config nodeId=%s' % nodeId)

    for nodeId in serverNodes:
        if nodeId not in clientNodes:
            logAndStoreError('Server config has a node which is missing from the client config nodeId=%s' % nodeId)

    if len(clientNodes) != len(serverNodes):
        logAndStoreError('Different number of nodes in server=%s & client=%s' % (len(clientNodes), len(serverNodes)))
    return errors


_mapConfigTags = frozenset(('nodes', ))
_nodesSecTags = frozenset(('node', ))
_nodeSecTags = frozenset(('id', 'x', 'y', 'narrative'))
_nodeSecMustHaveTags = frozenset(('id', 'x', 'y'))

def _readClientConfig(path):
    import ResMgr

    def error(msg, *args):
        if args:
            msg += str(args)
        try:
            _xml.raiseWrongXml(xmlCtx, '', msg)
        except SoftException as __:
            LOG_CURRENT_EXCEPTION()
            errors.append(msg)

    result = nodesPos, loresPos, errors = ([], [], [])
    xmlCtx = (None, path)
    mapSec = ResMgr.openSection(path)
    if mapSec is None:
        error('Cannot open this xml')
        return result
    else:
        rootItems = _xml.getItemsWithContext(xmlCtx, mapSec)
        tags = [ tag for tag, _ in rootItems ]
        dupes = {tag for tag, count in Counter(tags).items() if count > 1 if count > 1}
        if dupes:
            error('Duplicates in <root> not allowed', dupes)
        tags = set(tags)
        if tags != _mapConfigTags:
            error('Wrong tags in <root>, (missing, extra)', _mapConfigTags - tags, tags - _mapConfigTags)
        rootItems = dict(rootItems)
        xmlCtx, nodesSec = rootItems['nodes']
        nodesCtx = xmlCtx
        nodeItems = _xml.getItemsWithContext(xmlCtx, nodesSec)
        for nodeIdx, (secName, (xmlCtx, nodeSec)) in enumerate(nodeItems):
            if secName not in _nodesSecTags:
                error('Wrong tag: (found, tagIdx, expected)', secName, nodeIdx, _nodesSecTags)
                continue
            nodeItems = _xml.getItemsWithContext(xmlCtx, nodeSec)
            tags = [ t for t, _ in nodeItems ]
            dupes = {tag for tag, count in Counter(tags).items() if count > 1 if count > 1}
            if dupes:
                error('Duplicates in <node> not allowed: (nodeIdx, duplicates)', nodeIdx, dupes)
            tags = set(tags)
            invalids = tags - _nodeSecTags
            if invalids:
                error('Unexpected tags found in <node> (nodeIdx, unexpectedTags)', nodeIdx, invalids)
            invalids = _nodeSecMustHaveTags - tags
            if invalids:
                error('Expected tags not found in <node> (nodeIdx, missingTags)', nodeIdx, invalids)
            nodeId = nodeSec.readString('id', None)
            if nodeId is None or nodeId == '':
                error('Invalid nodeId, (nodeIdx, nodeId)', nodeId)
                nodeId = 'Invalid_Node_ID_' + str(nodeIdx)
            posX = nodeSec.readInt('x', None)
            posY = nodeSec.readInt('y', None)
            if posX is None or posY is None:
                error('Node coords are invalid, (nodeId, (x, y))', nodeId, (posX, posY))
            nodesPos.append((nodeId, (posX, posY)))
            nodeItems = dict(nodeItems)
            if 'narrative' in nodeItems:
                xmlCtx, loreSec = nodeItems['narrative']
                loreX = loreSec.readInt('x', None)
                loreY = loreSec.readInt('y', None)
                if loreX is None or loreY is None:
                    error('Narrative coords are invalid (nodeId, (x, y))', nodeId, (loreX, loreY))
                loresPos.append((nodeId, (loreX, loreY)))

        xmlCtx = nodesCtx
        nodeIds = [ nodeId for nodeId, _ in nodesPos ]
        dupes = {nodeId for nodeId, count in Counter(nodeIds).items() if count > 1 if count > 1}
        if dupes:
            error('Duplicate node IDs are not allowed', dupes)
        allPos = set()
        for nodeId, pos in nodesPos:
            if pos not in allPos:
                allPos.add(pos)
            else:
                error('Duplicate positons not allowed (nodeId, position)', nodeId, pos)

        nodesPos = dict(nodesPos)
        appliedLores = set()
        for nodeId, (xLore, yLore) in loresPos:
            xPos, yPos = nodesPos[nodeId]
            appliedLore = (xPos + xLore, yPos + yLore)
            if appliedLore not in appliedLores:
                appliedLores.add(appliedLore)
            else:
                error('Duplicate narratives not allowed (nodeId, posision, applied)', nodeId, (xLore, yLore), appliedLore)

        return result