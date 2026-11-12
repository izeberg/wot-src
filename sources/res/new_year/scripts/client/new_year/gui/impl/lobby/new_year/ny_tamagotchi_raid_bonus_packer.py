from new_year.gui.impl.gen.view_models.views.lobby.new_year.raid_item_model import RaidItemModel
from new_year.gui.impl.new_year.new_year_bonus_packer import getNewYearBonusPacker
_COPY_FIELDS = (
 ('getName', 'setName'),
 ('getValue', 'setValue'),
 ('getIsCompensation', 'setIsCompensation'),
 ('getTooltipId', 'setTooltipId'),
 ('getTooltipContentId', 'setTooltipContentId'),
 ('getLabel', 'setLabel'),
 ('getItem', 'setItem'),
 ('getUserName', 'setUserName'),
 ('getIcon', 'setIcon'),
 ('getType', 'setType'),
 ('getBigIcon', 'setBigIcon'),
 ('getIconName', 'setIconName'),
 ('getOverlayType', 'setOverlayType'))

def packRaidBonusModelAndTooltipData(bonuses, bonusModelsList, componentId=None, isEnabled=False, tooltipsData=None):
    packer = getNewYearBonusPacker()
    for bonus in bonuses:
        if not bonus.isShowInGUI():
            continue
        bonusList = packer.pack(bonus)
        bonusTooltipList = packer.getToolTip(bonus)
        bonusContentIdList = packer.getContentId(bonus)
        for bonusModel, tooltipData, contentId in zip(bonusList, bonusTooltipList, bonusContentIdList):
            raidModel = _createRaidModel(bonusModel, componentId, isEnabled)
            _fillTooltipData(raidModel, tooltipsData, tooltipData, contentId)
            bonusModelsList.addViewModel(raidModel)


def _createRaidModel(bonusModel, componentId, isEnabled):
    raidModel = RaidItemModel()
    _fillRaidModel(raidModel, bonusModel)
    raidModel.setIsEnabled(isEnabled)
    if componentId is not None:
        raidModel.setComponentID(componentId)
    return raidModel


def _fillTooltipData(raidModel, tooltipsData, tooltipData, contentId):
    if tooltipsData is None:
        return
    else:
        tooltipIdx = str(len(tooltipsData))
        raidModel.setTooltipId(tooltipIdx)
        if tooltipData is not None:
            tooltipsData[tooltipIdx] = tooltipData
        raidModel.setTooltipContentId(str(contentId))
        return


def _fillRaidModel(raidModel, bonusModel):
    for getterName, setterName in _COPY_FIELDS:
        if hasattr(bonusModel, getterName):
            getattr(raidModel, setterName)(getattr(bonusModel, getterName)())