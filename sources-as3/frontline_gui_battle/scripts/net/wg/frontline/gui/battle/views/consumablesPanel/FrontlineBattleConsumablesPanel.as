package net.wg.frontline.gui.battle.views.consumablesPanel
{
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.generated.CONSUMABLES_PANEL_SETTINGS;
   import net.wg.frontline.data.constants.FrontlineLinkages;
   import net.wg.frontline.gui.battle.views.consumablesPanel.interfaces.IFrontlineBattleConsumableButton;
   import net.wg.frontline.infrastructure.base.meta.IFrontlineBattleConsumablesPanelMeta;
   import net.wg.frontline.infrastructure.base.meta.impl.FrontlineBattleConsumablesPanelMeta;
   import net.wg.gui.battle.views.consumablesPanel.ConsumablesPanelSettings;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IConsumablesButton;
   
   public class FrontlineBattleConsumablesPanel extends FrontlineBattleConsumablesPanelMeta implements IFrontlineBattleConsumablesPanelMeta
   {
      
      private static const FL_BATTLE_GROUP_GAP:int = 10;
      
      private static const FL_BATTLE_GROUP_INDEXES:Vector.<uint> = new <uint>[6,9];
       
      
      public function FrontlineBattleConsumablesPanel()
      {
         super();
      }
      
      override protected function preInitialize() : void
      {
         super.preInitialize();
         settings[CONSUMABLES_PANEL_SETTINGS.EPIC_BATTLE_SETTINGS_ID] = new ConsumablesPanelSettings(CONSUMABLES_PANEL_Y_OFFSET,getItemWidthPadding(App.appWidth),FrontlineLinkages.FRONTLINE_BATTLE_CONSUMABLE_BUTTON,Linkages.SHELL_BUTTON_BATTLE,FL_BATTLE_GROUP_GAP,FL_BATTLE_GROUP_INDEXES);
      }
      
      public function as_addEpicBattleEquipmentSlot(param1:int, param2:Number, param3:Number, param4:int, param5:Number, param6:Number, param7:String, param8:Boolean, param9:String, param10:int) : void
      {
         super.as_addEquipmentSlot(param1,param2,param3,param4,param5,param6,param7,param9,param10);
         var _loc11_:IFrontlineBattleConsumableButton = this.getEBRendererBySlotIdx(param1);
         _loc11_.isTooltipSpecial = param8;
      }
      
      public function as_updateLevelInformation(param1:int, param2:int) : void
      {
         var _loc3_:IFrontlineBattleConsumableButton = this.getEBRendererBySlotIdx(param1);
         if(_loc3_)
         {
            _loc3_.updateLevelInformation(param2);
         }
      }
      
      public function as_updateLockedInformation(param1:int, param2:int, param3:String, param4:Boolean) : void
      {
         var _loc5_:IFrontlineBattleConsumableButton = this.getEBRendererBySlotIdx(param1);
         if(_loc5_)
         {
            _loc5_.updateLockedInformation(param2,param3,param4);
         }
      }
      
      public function as_updateStacks(param1:int, param2:int) : void
      {
         var _loc3_:IFrontlineBattleConsumableButton = this.getEBRendererBySlotIdx(param1);
         if(_loc3_)
         {
            _loc3_.updateStacks(param2);
         }
      }
      
      public function as_showPossibleStacks(param1:int, param2:int) : void
      {
         var _loc3_:IFrontlineBattleConsumableButton = this.getEBRendererBySlotIdx(param1);
         if(_loc3_)
         {
            _loc3_.showPossibleStacks(param2);
         }
      }
      
      override protected function createEquipmentButton() : IConsumablesButton
      {
         return App.utils.classFactory.getComponent(FrontlineLinkages.FRONTLINE_BATTLE_CONSUMABLE_BUTTON,FrontlineBattleConsumableButton);
      }
      
      private function getEBRendererBySlotIdx(param1:int) : IFrontlineBattleConsumableButton
      {
         return getRendererBySlotIdx(param1) as IFrontlineBattleConsumableButton;
      }
   }
}
