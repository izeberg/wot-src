from typing import TYPE_CHECKING
from CurrentVehicle import g_currentVehicle
from gui.customization.constants import CustomizationModes
from gui.customization.shared import SEASONS_ORDER, SEASON_TYPE_TO_NAME
from gui.impl.gen.view_models.views.lobby.customization.customization_seasons_item_model import CustomizationSeasonsItemModel
from gui.impl.lobby.customization.shared import CustomizationTabs, checkSlotsFilling, getItemTypesAvailableForVehicle
from gui.shared.gui_items import GUI_ITEM_TYPE
if TYPE_CHECKING:
    from typing import Dict, List
    from gui.impl.gen.view_models.views.lobby.customization.customization_seasons_model import CustomizationSeasonsModel
    from gui.impl.lobby.customization.context.context import CustomizationContext

def fillSeasonsModel(seasonsModel, ctx):
    seasonsData = getSeasonData(ctx)
    itemsList = seasonsModel.getSeasonsList()
    itemsList.clear()
    for season in seasonsData:
        itemData = CustomizationSeasonsItemModel()
        itemData.setSeason(season['season'])
        itemData.setIsFull(season['isFull'])
        itemData.setIsSelected(season['isSelected'])
        itemData.setItemNotificationCount(season['notificationCount'])
        itemsList.addViewModel(itemData)

    itemsList.invalidate()


def getSeasonData(ctx):
    seasonsList = []
    seasonNotificationCounters = getNotificationCounters(ctx)
    for season in SEASONS_ORDER:
        isFull = False
        if ctx.modeId == CustomizationModes.CUSTOM:
            outfit = ctx.mode.getModifiedOutfit(season)
            slotTypes = (CustomizationTabs.SLOT_TYPES[tabId] for tabId in CustomizationTabs.CUSTOM_ALL)
            isFull = all(filled_slots >= total_slots for total_slots, filled_slots in (checkSlotsFilling(outfit, slot_type) for slot_type in slotTypes))
        elif ctx.modeId in CustomizationModes.ALL_STYLES:
            isFull = ctx.mode.currentOutfit.style is not None
        seasonsList.append({'season': SEASON_TYPE_TO_NAME.get(season), 
           'isFull': isFull, 
           'isSelected': season == ctx.season, 
           'notificationCount': seasonNotificationCounters[season]})

    return seasonsList


def getNotificationCounters(ctx):
    seasonCounters = {}
    itemTypes = (GUI_ITEM_TYPE.STYLE,) if ctx.modeId in CustomizationModes.STYLED else getItemTypesAvailableForVehicle() - {GUI_ITEM_TYPE.STYLE}
    itemsFilter = --- This code section failed: ---

 L.  77         0  LOAD_DEREF            0  'ctx'
                3  LOAD_ATTR             0  'modeId'
                6  LOAD_GLOBAL           1  'CustomizationModes'
                9  LOAD_ATTR             2  'EDITABLE_STYLE'
               12  COMPARE_OP            2  ==
               15  POP_JUMP_IF_FALSE    50  'to 50'
               18  LOAD_DEREF            0  'ctx'
               21  LOAD_ATTR             3  'mode'
               24  LOAD_ATTR             4  'style'
               27  LOAD_ATTR             5  'isItemInstallable'
               30  LOAD_FAST             0  'item'
               33  CALL_FUNCTION_1       1  None
               36  JUMP_IF_FALSE_OR_POP    56  'to 56'
               39  LOAD_FAST             0  'item'
               42  LOAD_ATTR             6  'isAllSeason'
               45  CALL_FUNCTION_0       0  None
               48  UNARY_NOT        
               49  RETURN_END_IF_LAMBDA
             50_0  COME_FROM            36  '36'
             50_1  COME_FROM            15  '15'

 L.  78        50  LOAD_LAMBDA              '<code_object <lambda>>'
               53  MAKE_FUNCTION_0       0  None
               56  RETURN_VALUE_LAMBDA
               -1  LAMBDA_MARKER    

Parse error at or near `None' instruction at offset -1
    for season in SEASONS_ORDER:
        seasonCounters[season] = g_currentVehicle.item.getC11nItemsNoveltyCounter(g_currentVehicle.itemsCache.items, itemTypes, season, itemsFilter) if ctx.season != season else 0

    return seasonCounters# Decompile failed :(