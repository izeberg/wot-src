package net.wg.historical_battles.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.consumablesPanel.ConsumablesPanel;
   import net.wg.historical_battles.gui.battle.data.HBAbilitySlotVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class HBConsumablesPanelMeta extends ConsumablesPanel
   {
       
      
      private var _hBAbilitySlotVO:HBAbilitySlotVO;
      
      private var _array:Array;
      
      private var _hBAbilitySlotVO1:HBAbilitySlotVO;
      
      public function HBConsumablesPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._hBAbilitySlotVO)
         {
            this._hBAbilitySlotVO.dispose();
            this._hBAbilitySlotVO = null;
         }
         if(this._array)
         {
            this._array.splice(0,this._array.length);
            this._array = null;
         }
         if(this._hBAbilitySlotVO1)
         {
            this._hBAbilitySlotVO1.dispose();
            this._hBAbilitySlotVO1 = null;
         }
         super.onDispose();
      }
      
      public final function as_addAbilitySlot(param1:int, param2:Object) : void
      {
         var _loc3_:HBAbilitySlotVO = this._hBAbilitySlotVO;
         this._hBAbilitySlotVO = new HBAbilitySlotVO(param2);
         this.addAbilitySlot(param1,this._hBAbilitySlotVO);
         if(_loc3_)
         {
            _loc3_.dispose();
         }
      }
      
      public final function as_resetPassiveAbilities(param1:Array) : void
      {
         var _loc2_:Array = this._array;
         this._array = param1;
         this.resetPassiveAbilities(this._array);
         if(_loc2_)
         {
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      public final function as_addRoleAbilitySlot(param1:int, param2:Object) : void
      {
         var _loc3_:HBAbilitySlotVO = this._hBAbilitySlotVO1;
         this._hBAbilitySlotVO1 = new HBAbilitySlotVO(param2);
         this.addRoleAbilitySlot(param1,this._hBAbilitySlotVO1);
         if(_loc3_)
         {
            _loc3_.dispose();
         }
      }
      
      protected function addAbilitySlot(param1:int, param2:HBAbilitySlotVO) : void
      {
         var _loc3_:String = "as_addAbilitySlot" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc3_);
         throw new AbstractException(_loc3_);
      }
      
      protected function resetPassiveAbilities(param1:Array) : void
      {
         var _loc2_:String = "as_resetPassiveAbilities" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function addRoleAbilitySlot(param1:int, param2:HBAbilitySlotVO) : void
      {
         var _loc3_:String = "as_addRoleAbilitySlot" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc3_);
         throw new AbstractException(_loc3_);
      }
   }
}
