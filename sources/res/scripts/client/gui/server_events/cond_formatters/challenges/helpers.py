from __future__ import absolute_import
import logging
from gui.impl import backport
from gui.server_events.cond_formatters import FORMATTER_IDS, FormattableField
from gui.server_events.cond_formatters.challenges.constants import DEFAULT_CONDITION_TITLE_TEXT_RES, DEFAULT_CONDITION_TEXT_RES
_logger = logging.getLogger(__name__)

def _createText(textRes, defaultRes, **kwargs):
    if not textRes.exists():
        return backport.text(defaultRes())
    return backport.text(textRes(), **kwargs)


def packDescriptionField(textRes, **kwargs):
    return FormattableField(FORMATTER_IDS.DESCRIPTION, (
     _createText(textRes, DEFAULT_CONDITION_TEXT_RES, **kwargs),))


def packTitleField(textRes, **kwargs):
    return FormattableField(FORMATTER_IDS.SIMPLE_TITLE, (
     _createText(textRes, DEFAULT_CONDITION_TITLE_TEXT_RES, **kwargs),))


def getRelationValue(condition):
    if condition.relationValue is not None:
        return backport.getNiceNumberFormat(condition.relationValue)
    else:
        _logger.error('Undefined relation value for condition: %s', condition.getData())
        return -1