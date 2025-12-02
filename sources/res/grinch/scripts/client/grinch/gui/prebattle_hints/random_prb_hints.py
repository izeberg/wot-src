import random
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R

def _createHtmlTextWithDescr(title, descrTxt):
    return makeHtmlString('html_templates:battle/loadingScreenSimple', 'mainTip', ctx={'title': backport.text(title), 
       'description': backport.text(descrTxt)})


def _makeImgPath(index):
    return ('grinch/gui/maps/icons/map/screen/prebattle_hints/{}.dds').format(index)


class GrinchPrbRandomHintManager(object):

    def __init__(self):
        super(GrinchPrbRandomHintManager, self).__init__()
        self._imgs = []
        self._texts = []
        self._currentImgIndex = 0
        self._currentHintTextIndex = 0
        self._fillPrbHintTexts()
        self._fillPrbImgs()

    def _fillPrbHintTexts(self):
        prbHintsTexts = R.strings.grinch.battle.loadingScreen
        for txtItem in prbHintsTexts.values():
            self._texts.append(_createHtmlTextWithDescr(txtItem.title(), txtItem.description()))

        random.shuffle(self._imgs)

    def _fillPrbImgs(self):
        prbHintsImgs = R.images.grinch.gui.maps.icons.map.screen.prebattle_hints
        for imgName in prbHintsImgs.keys():
            self._imgs.append(_makeImgPath(imgName))

        random.shuffle(self._texts)

    def incrementIndexes(self):
        self._currentHintTextIndex = (self._currentHintTextIndex + 1) % len(self._texts)
        self._currentImgIndex = (self._currentImgIndex + 1) % len(self._imgs)

    def getHintText(self):
        return self._texts[self._currentHintTextIndex]

    def getHintImagePath(self):
        return self._imgs[self._currentImgIndex]