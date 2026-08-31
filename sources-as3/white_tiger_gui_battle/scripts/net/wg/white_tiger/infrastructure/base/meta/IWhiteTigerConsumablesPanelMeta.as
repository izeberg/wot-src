package net.wg.white_tiger.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IWhiteTigerConsumablesPanelMeta extends IEventDispatcher
   {
       
      
      function as_setChargeProgress(param1:int, param2:Number, param3:Boolean) : void;
      
      function as_setSelected(param1:int, param2:Boolean) : void;
      
      function as_setDebuffView(param1:int, param2:Boolean) : void;
      
      function as_setInspired(param1:Boolean) : void;
      
      function as_addWhiteTigerEquipmentSlot(param1:int, param2:Number, param3:Number, param4:int, param5:Number, param6:Number, param7:String, param8:String, param9:int, param10:String, param11:int) : void;
      
      function as_setStage(param1:int, param2:int) : void;
   }
}
