import logging
from gui.Scaleform.daapi.view.lobby.vehicle_preview.shared import EXT_PREVIEW_ITEMS
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def addExtPreviewAliasItem(previewAliasItem, personality):
    if previewAliasItem[0] in EXT_PREVIEW_ITEMS:
        raise SoftException(('EXT_PREVIEW_ITEMS already has arenaGuiType:{previewAliasItem}. Personality: {personality}').format(previewAliasItem=previewAliasItem, personality=personality))
    EXT_PREVIEW_ITEMS.update((previewAliasItem,))
    msg = ('previewAliasItem:{previewAliasItem} was added to EXT_PREVIEW_ITEMS. Personality: {p}').format(previewAliasItem=previewAliasItem, p=personality)
    logging.debug(msg)