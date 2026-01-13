from gui.Scaleform.daapi.view.lobby.server_events.token_converter_helper import getBonusDataFromOneOfBonuses, convertTokensInBonusData
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData

def packBonusesWithActualTokensConvertion(pCur, model, event, questTokensConvertion, questTokensCount, tooltipData, bonusPacker):
    bonusData = getBonusDataFromOneOfBonuses(event, pCur)
    bonusData = convertTokensInBonusData(event=event, bonusData=bonusData, questTokensConvertion=questTokensConvertion, questTokensCount=questTokensCount)
    questBonuses = event.getBonuses(bonusData=bonusData)
    bonuses = model.getBonuses()
    bonuses.clear()
    packQuestBonusModelAndTooltipData(bonusPacker, bonuses, event, questBonuses=questBonuses, tooltipData=tooltipData)