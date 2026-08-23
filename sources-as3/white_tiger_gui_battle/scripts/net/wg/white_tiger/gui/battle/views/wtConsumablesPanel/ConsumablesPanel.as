package net.wg.white_tiger.gui.battle.views.wtConsumablesPanel
{
   import flash.display.DisplayObject;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLE_CONSUMABLES_PANEL_TAGS;
   import net.wg.gui.battle.views.consumablesPanel.VO.ConsumablesVO;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IBattleShellButton;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IConsumablesButton;
   import net.wg.white_tiger.data.constants.WT_LINKAGES;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_BATTLE_CONSUMABLES_PANEL_TAGS;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces.IWTBaseConsumablesButton;
   import net.wg.white_tiger.gui.battle.views.wtConsumablesPanel.interfaces.IWTConsumablesButton;
   import net.wg.white_tiger.infrastructure.base.meta.IWTConsumablesPanelMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WTConsumablesPanelMeta;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class ConsumablesPanel extends WTConsumablesPanelMeta implements IWTConsumablesPanelMeta
   {
      
      private static const ITEMS_PADDING:int = 49;
      
      private static const DIVIDER_OFFSET:int = 12;
      
      private static const CAT_SKILL:int = 0;
      
      private static const CAT_CONSUMABLE:int = 1;
      
      private static const CAT_PASSIVE:int = 2;
      
      private static const CAT_AMMO:int = 3;
       
      
      public function ConsumablesPanel()
      {
         super();
      }
      
      override protected function createShellButton() : IBattleShellButton
      {
         return App.utils.classFactory.getComponent(WT_LINKAGES.WT_SHELL_BUTTON_BATTLE,IBattleShellButton);
      }
      
      override protected function createEquipmentButton() : IConsumablesButton
      {
         return App.utils.classFactory.getComponent(WT_LINKAGES.WT_EQUIPMENT_BUTTON,IConsumablesButton);
      }
      
      override protected function drawLayout() : void
      {
         var _loc3_:IConsumablesButton = null;
         var _loc1_:int = renderers.length;
         var _loc2_:int = 0;
         var _loc4_:Boolean = false;
         var _loc5_:int = Values.DEFAULT_INT;
         var _loc6_:int = Values.DEFAULT_INT;
         var _loc7_:uint = 0;
         while(_loc7_ < _loc1_)
         {
            _loc3_ = getRendererBySlotIdx(_loc7_);
            if(_loc3_ != null)
            {
               _loc6_ = this.getSlotCat(_loc3_.consumablesVO.tag);
               if(_loc3_ && _loc3_.visible)
               {
                  if(_loc5_ != _loc6_)
                  {
                     if(!_loc4_)
                     {
                        _loc4_ = true;
                     }
                     else
                     {
                        _loc2_ += DIVIDER_OFFSET;
                     }
                  }
                  _loc3_.x = _loc2_;
                  _loc2_ += ITEMS_PADDING;
               }
               _loc5_ = _loc6_;
            }
            _loc7_++;
         }
         basePanelWidth = _loc2_;
      }
      
      public function as_wtAddPassiveAbilitySlot(param1:int, param2:String, param3:String) : void
      {
         var _loc4_:IConsumablesButton = null;
         if(renderers[param1] == null)
         {
            _loc4_ = this.createPassiveAbilityButton();
            renderers[param1] = _loc4_;
            addChild(DisplayObject(_loc4_));
         }
         else
         {
            _loc4_ = getRendererBySlotIdx(param1);
         }
         var _loc5_:ConsumablesVO = _loc4_.consumablesVO;
         _loc5_.idx = param1;
         _loc5_.tag = WHITE_TIGER_BATTLE_CONSUMABLES_PANEL_TAGS.WT_PASSIVE_ABILITY_ITEM;
         _loc4_.icon = param2;
         _loc4_.tooltipStr = param3;
         invalidate(INVALIDATE_DRAW_LAYOUT);
      }
      
      public function as_wtSetChargeProgress(param1:int, param2:int) : void
      {
         var _loc3_:IWTConsumablesButton = getRendererBySlotIdx(param1) as IWTConsumablesButton;
         if(_loc3_)
         {
            _loc3_.wtSetCharge(param2);
         }
      }
      
      public function as_wtSetDisabled(param1:int, param2:Boolean) : void
      {
         var _loc3_:IWTBaseConsumablesButton = getRendererBySlotIdx(param1) as IWTBaseConsumablesButton;
         if(_loc3_)
         {
            _loc3_.wtSetDisabled(param2);
         }
      }
      
      public function as_wtSetLocked(param1:int, param2:Boolean) : void
      {
         var _loc3_:IWTConsumablesButton = getRendererBySlotIdx(param1) as IWTConsumablesButton;
         if(_loc3_)
         {
            _loc3_.wtSetLocked(param2);
         }
      }
      
      public function as_wtShowActive(param1:int, param2:int) : void
      {
         var _loc3_:IWTBaseConsumablesButton = getRendererBySlotIdx(param1) as IWTBaseConsumablesButton;
         if(_loc3_)
         {
            _loc3_.wtShowActive(param2);
         }
      }
      
      public function as_wtShowCooldown(param1:int, param2:int) : void
      {
         var _loc3_:IWTConsumablesButton = getRendererBySlotIdx(param1) as IWTConsumablesButton;
         if(_loc3_)
         {
            _loc3_.wtShowCooldown(param2);
         }
      }
      
      public function as_wtShowDeploying(param1:int) : void
      {
         var _loc2_:IWTConsumablesButton = getRendererBySlotIdx(param1) as IWTConsumablesButton;
         if(_loc2_)
         {
            _loc2_.wtShowDeploying();
         }
      }
      
      public function as_wtShowPreparing(param1:int) : void
      {
         var _loc2_:IWTConsumablesButton = getRendererBySlotIdx(param1) as IWTConsumablesButton;
         if(_loc2_)
         {
            _loc2_.wtShowPreparing();
         }
      }
      
      public function as_wtShowReady(param1:int) : void
      {
         var _loc2_:IWTConsumablesButton = getRendererBySlotIdx(param1) as IWTConsumablesButton;
         if(_loc2_)
         {
            _loc2_.wtShowReady();
         }
      }
      
      private function createPassiveAbilityButton() : IWTBaseConsumablesButton
      {
         return App.utils.classFactory.getComponent(WT_LINKAGES.WT_PASSIVE_ABILITY_BUTTON,IWTBaseConsumablesButton);
      }
      
      private function getSlotCat(param1:String) : int
      {
         if(param1 == BATTLE_CONSUMABLES_PANEL_TAGS.MED_KIT || param1 == BATTLE_CONSUMABLES_PANEL_TAGS.REPAIR_KIT)
         {
            return CAT_CONSUMABLE;
         }
         if(param1 == WHITE_TIGER_BATTLE_CONSUMABLES_PANEL_TAGS.WT_PASSIVE_ABILITY_ITEM)
         {
            return CAT_PASSIVE;
         }
         if(StringUtils.isEmpty(param1))
         {
            return CAT_AMMO;
         }
         return CAT_SKILL;
      }
   }
}
