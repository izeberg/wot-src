from __future__ import absolute_import
import logging
LOGGER_NAME = 'NewbieBattleHints'

def getLogger(*names):
    return logging.getLogger(('{}').format((':').join((LOGGER_NAME,) + names)))