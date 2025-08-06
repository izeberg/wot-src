import logging, typing
from constants import GF_RES_PROTOCOL
from gui.shared.utils.functions import getAbsoluteUrl
if typing.TYPE_CHECKING:
    from typing import Optional
_logger = logging.getLogger(__name__)

def _normalizeGfPath(resourcePath, protocol):
    if not isinstance(resourcePath, (str, unicode)) or not resourcePath:
        _logger.warning('Wrong resource path: %s.', resourcePath)
        return None
    else:
        newPath = getAbsoluteUrl(str(resourcePath))
        newPath = newPath.replace('\\', '/')
        if not newPath.startswith(protocol):
            newPath = ('').join((protocol, newPath))
        return newPath


def normalizeGfImagePath(imgPath):
    return _normalizeGfPath(imgPath, GF_RES_PROTOCOL.IMG)


def normalizeGfVideoPath(videoPath):
    return _normalizeGfPath(videoPath, GF_RES_PROTOCOL.VIDEO)