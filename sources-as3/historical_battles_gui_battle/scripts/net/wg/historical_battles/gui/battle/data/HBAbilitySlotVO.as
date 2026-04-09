package net.wg.historical_battles.gui.battle.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HBAbilitySlotVO extends DAAPIDataClass
   {
       
      
      public var keyCode:Number = -1;
      
      public var sfKeyCode:Number = -1;
      
      public var quantity:int = -1;
      
      public var timeRemaining:Number = -1;
      
      public var reloadingTime:Number = -1;
      
      public var iconPath:String = "";
      
      public var tooltipText:String = "";
      
      public function HBAbilitySlotVO(param1:Object)
      {
         super(param1);
      }
   }
}
