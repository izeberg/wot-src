from __future__ import absolute_import
from gui.shared.gui_items.dossier.achievements import validators

class Deprecated(object):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)