from dependency_injection_container import replace_none_kwargs
from goodies.goodie_constants import GOODIE_STATE
from gui.impl.lobby.loot_box.loot_box_sounds import PausedSoundManager
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.shared import IItemsCache
from new_year.helpers.server_settings import getNewYearObjectsConfig
from new_year_common.items.components.ny_constants import TOKEN_VARIADIC_DISCOUNT_PREFIX
from gui.impl.gen import R
from embeded_video import _EmbeddedAudioVideoWindow

def _getVariadicID(vCD):
    return TOKEN_VARIADIC_DISCOUNT_PREFIX + ':' + str(vCD)


@replace_none_kwargs(itemsCache=IItemsCache)
def getCurrentObjectLevel(objectName, itemsCache=None):
    config = getNewYearObjectsConfig()
    currentLevel = itemsCache.items.tokens.getTokenCount(config.getObjectToken(objectName))
    return currentLevel


def showWebmVideoView(videoSource, parent=None, onVideoStarted=None, onVideoStopped=None, onVideoClosed=None, isAutoClose=False, canEscape=True, isUIVisible=False, uiShowDelay=-1):
    from gui.impl.lobby.video.video_view import VideoViewWindow
    window = VideoViewWindow(videoSource=videoSource, parent=parent, onVideoStarted=onVideoStarted, onVideoStopped=onVideoStopped, onVideoClosed=onVideoClosed, isAutoClose=isAutoClose, soundControl=PausedSoundManager(), canEscape=canEscape, isUIVisible=isUIVisible, uiShowDelay=uiShowDelay, viewId=R.views.lobby.video.VideoViewWebm())
    window.load()
    return window


def lockNyNotifications(source, lock):
    from gui.shared.lock_overlays import lockNotificationManager
    lockNotificationManager(lock=lock, postponeActive=lock, releasePostponed=not lock, source=source)


@replace_none_kwargs(itemsCache=IItemsCache, goodiesCache=IGoodiesCache)
def isRaidComponentEnabled(bonus, reservedResources=None, itemsCache=None, goodiesCache=None):
    reservedResources = reservedResources or {}
    if 'gold' in bonus:
        return itemsCache.items.stats.gold - reservedResources.get('gold', 0) >= bonus['gold']
    else:
        if 'credits' in bonus:
            return itemsCache.items.stats.credits - reservedResources.get('credits', 0) >= bonus['credits']
        if 'crystal' in bonus:
            return itemsCache.items.stats.crystal - reservedResources.get('crystal', 0) >= bonus['crystal']
        if 'freeXP' in bonus:
            return itemsCache.items.stats.freeXP - reservedResources.get('freeXP', 0) >= bonus['freeXP']
        if 'equipCoin' in bonus:
            return itemsCache.items.stats.equipCoin - reservedResources.get('equipCoin', 0) >= bonus['equipCoin']
        if 'items' in bonus:
            itemIntCD, count = next(bonus['items'].iteritems())
            item = itemsCache.items.getItemByCD(itemIntCD)
            return item is not None and item.inventoryCount is not None and item.inventoryCount - reservedResources.get(('items', itemIntCD), 0) >= count
        if 'goodies' in bonus:
            goodieID, info = next(bonus['goodies'].iteritems())
            goodie = goodiesCache.getGoodie(goodieID)
            count = info.get('count', 1)
            availableCount = getattr(goodie, 'inventoryCount', getattr(goodie, 'count', 0)) if goodie is not None else 0
            availableCount = availableCount or 0
            if availableCount > 0 and goodie.state == GOODIE_STATE.ACTIVE:
                availableCount -= 1
            return availableCount - reservedResources.get(('goodies', goodieID), 0) >= count
        if 'tokens' in bonus:
            tokenID, info = next(bonus['tokens'].iteritems())
            return itemsCache.items.tokens.getTokenCount(tokenID=tokenID) - reservedResources.get(('tokens', tokenID), 0) >= info.get('count', 1)
        return False


def _getRaidReservedResourceData(bonus):
    if 'gold' in bonus:
        return ('gold', bonus['gold'])
    else:
        if 'credits' in bonus:
            return ('credits', bonus['credits'])
        if 'crystal' in bonus:
            return ('crystal', bonus['crystal'])
        if 'freeXP' in bonus:
            return ('freeXP', bonus['freeXP'])
        if 'equipCoin' in bonus:
            return ('equipCoin', bonus['equipCoin'])
        if 'items' in bonus:
            itemIntCD, count = next(bonus['items'].iteritems())
            return (
             (
              'items', itemIntCD), count)
        if 'goodies' in bonus:
            goodieID, info = next(bonus['goodies'].iteritems())
            return (
             (
              'goodies', goodieID), info.get('count', 1))
        if 'tokens' in bonus:
            tokenID, info = next(bonus['tokens'].iteritems())
            return (
             (
              'tokens', tokenID), info.get('count', 1))
        return (None, 0)


def _changeRaidReservedResources(reserved, bonus, delta):
    key, count = _getRaidReservedResourceData(bonus)
    if key is None:
        return reserved
    else:
        reserved[key] = max(0, reserved.get(key, 0) + count * delta)
        return reserved


def addRaidReservedResources(reserved, bonus):
    return _changeRaidReservedResources(reserved, bonus, 1)


def subtractRaidReservedResources(reserved, bonus):
    return _changeRaidReservedResources(reserved, bonus, -1)


def collectRaidReservedResources(components, selectedIDs):
    reserved = {}
    for componentId in selectedIDs:
        componentData = components.get(componentId)
        if componentData is not None:
            addRaidReservedResources(reserved, componentData.get('bonus', componentData))

    return reserved


def showEmbeddedAudioVideoView(videoSource, parent=None, onVideoStarted=None, onVideoClosed=None, isControlsVisible=False, isSubtitlesVisible=False, subtitlesPath=None, soundSpace=None, releaseNotificationsLockOnClose=True, canEscape=True, handleWorldDraw=True):
    from events_core_client.gui.impl.video_with_controls.video_view import VideoPrerequisites
    from gui.impl.gen_utils import INVALID_RES_ID
    prerequisites = VideoPrerequisites(videoPath=videoSource, subtitlesPath=subtitlesPath if subtitlesPath is not None else INVALID_RES_ID, isControlsVisible=isControlsVisible, isSubtitlesVisible=isSubtitlesVisible, soundSpace=soundSpace, canEscape=canEscape, handleWorldDraw=handleWorldDraw)
    window = _EmbeddedAudioVideoWindow(prerequisites, parent=parent, onClosed=onVideoClosed, onStarted=onVideoStarted, releaseNotificationsLockOnClose=releaseNotificationsLockOnClose)
    window.load()
    return window