import typing, logging
from constants import IS_DEVELOPMENT
from frameworks import wulf
_logger = logging.getLogger(__name__)
INVALID_RESID = ''

def isVaildResId(resId):
    if resId > 0:
        return True
    _logger.warning('Invalid resId')
    if IS_DEVELOPMENT:
        import traceback
        traceback.print_stack(limit=2)
    return False


def text(resId, *args, **kwargs):
    if not isVaildResId(resId):
        return INVALID_RESID
    if args:
        try:
            return wulf.getTranslatedTextByResId(resId, args)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, args)
            return ''

    elif kwargs:
        try:
            return wulf.getTranslatedTextByResId(resId, kwargs)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, kwargs)
            return ''

    return wulf.getTranslatedTextByResId(resId)


def ntext(resId, n, *args, **kwargs):
    if not isVaildResId(resId):
        return INVALID_RESID
    if args:
        try:
            return wulf.getTranslatedPluralTextByResId(resId, n, args)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, args)
            return ''

    elif kwargs:
        try:
            return wulf.getTranslatedPluralTextByResId(resId, n, kwargs)
        except (TypeError, ValueError):
            _logger.warning("Arguments do not match string with resId '%r': %r", resId, kwargs)
            return ''

    return wulf.getTranslatedPluralTextByResId(resId, n)


def msgid(resId):
    return wulf.getTranslatedKey(resId)


def image(resId):
    if not isVaildResId(resId):
        return INVALID_RESID
    return wulf.getImagePath(resId)


def sound(resId):
    return wulf.getSoundEffectId(resId)


def layout(resId):
    return wulf.getLayoutPath(resId)