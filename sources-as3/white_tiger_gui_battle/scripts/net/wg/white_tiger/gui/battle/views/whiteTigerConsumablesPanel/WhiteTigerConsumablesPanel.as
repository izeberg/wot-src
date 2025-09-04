package net.wg.white_tiger.gui.battle.views.whiteTigerConsumablesPanel
{
   import flash.display.DisplayObject;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.consumablesPanel.VO.ConsumablesVO;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IBattleShellButton;
   import net.wg.gui.battle.views.consumablesPanel.interfaces.IConsumablesButton;
   import net.wg.white_tiger.data.constants.generated.WHITE_TIGER_CONSUMABLES_PANEL_TAGS;
   import net.wg.white_tiger.infrastructure.base.meta.IWhiteTigerConsumablesPanelMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WhiteTigerConsumablesPanelMeta;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class WhiteTigerConsumablesPanel extends WhiteTigerConsumablesPanelMeta implements IWhiteTigerConsumablesPanelMeta
   {
      
      private static const ITEMS_PADDING:int = 53;
      
      private static const DIVIDER_OFFSET:int = 12;
      
      private static const CAT_AMMO:int = 0;
      
      private static const CAT_CONSUMABLE:int = 1;
      
      private static const CAT_SKILL:int = 2;
       
      
      private var shellButton:IWhiteTigerBattleShellButton = null;
      
      public function WhiteTigerConsumablesPanel()
      {
         super();
      }
      
      public function as_setStage(param1:int, param2:int) : void
      {
         var _loc3_:IWhiteTigerConsumablesButton = getRendererBySlotIdx(param1) as IWhiteTigerConsumablesButton;
         if(_loc3_)
         {
            _loc3_.setStage(param2);
         }
      }
      
      public function as_addWhiteTigerEquipmentSlot(param1:int, param2:Number, param3:Number, param4:int, param5:Number, param6:Number, param7:String, param8:String, param9:int, param10:String, param11:int) : void
      {
         equipmentButtonLinkage = settings[_settingsId].equipmentButtonLinkage;
         this.addEquipmentSlot(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11);
         invalidate(INVALIDATE_DRAW_LAYOUT);
      }
      
      private function addEquipmentSlot(param1:int, param2:Number, param3:Number, param4:int, param5:Number, param6:Number, param7:String, param8:String, param9:int, param10:String, param11:int) : void
      {
         var _loc12_:IWhiteTigerConsumablesButton = null;
         if(renderers[param1] == null)
         {
            _loc12_ = this.createEquipmentButton() as IWhiteTigerConsumablesButton;
            renderers[param1] = _loc12_;
            addChild(DisplayObject(_loc12_));
         }
         else
         {
            _loc12_ = getRendererBySlotIdx(param1) as IWhiteTigerConsumablesButton;
         }
         var _loc13_:ConsumablesVO = _loc12_.consumablesVO;
         _loc13_.keyCode = param2;
         _loc13_.idx = param1;
         _loc13_.tag = param10;
         _loc12_.isReplay = isReplay;
         _loc12_.icon = param7;
         _loc12_.tooltipStr = param8;
         _loc12_.key = param3;
         _loc12_.addClickCallBack(this);
         _loc12_.setCoolDownTime(param5,param6,param6 - param5,param9);
         _loc12_.quantity = param4;
         _loc12_.setStage(param11);
      }
      
      public function as_setChargeProgress(param1:int, param2:Number, param3:Boolean) : void
      {
         var _loc4_:IWhiteTigerConsumablesButton = getRendererBySlotIdx(param1) as IWhiteTigerConsumablesButton;
         if(_loc4_)
         {
            _loc4_.setCharge(param1,param2,param3);
         }
      }
      
      public function as_setSelected(param1:int, param2:Boolean) : void
      {
         var _loc3_:IWhiteTigerConsumablesButton = getRendererBySlotIdx(param1) as IWhiteTigerConsumablesButton;
         if(_loc3_)
         {
            _loc3_.setSelected(param2);
         }
      }
      
      public function as_setDebuffView(param1:int, param2:Boolean) : void
      {
         var _loc3_:IWhiteTigerConsumablesButton = getRendererBySlotIdx(param1) as IWhiteTigerConsumablesButton;
         if(_loc3_)
         {
            _loc3_.setDebuffView(param2);
         }
      }
      
      public function as_setInspired(param1:Boolean) : void
      {
         if(this.shellButton)
         {
            this.shellButton.setInspired(param1);
         }
      }
      
      override protected function createShellButton() : IBattleShellButton
      {
         this.shellButton = App.utils.classFactory.getComponent(Linkages.EVENT_SHELL_BUTTON_BATTLE,IWhiteTigerBattleShellButton);
         return this.shellButton;
      }
      
      override protected function createEquipmentButton() : IConsumablesButton
      {
         return App.utils.classFactory.getComponent(Linkages.EVENT_EQUIPMENT_BUTTON,IConsumablesButton);
      }
      
      override protected function get itemsPadding() : int
      {
         return ITEMS_PADDING;
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
                  _loc2_ += this.itemsPadding;
               }
               _loc5_ = _loc6_;
            }
            _loc7_++;
         }
         basePanelWidth = _loc2_;
      }
      
      private function getSlotCat(param1:String) : int
      {
         if(param1 == WHITE_TIGER_CONSUMABLES_PANEL_TAGS.TRIGGER_ITEM)
         {
            return CAT_SKILL;
         }
         if(StringUtils.isEmpty(param1))
         {
            return CAT_AMMO;
         }
         return CAT_CONSUMABLE;
      }
   }
}
