package net.wg.gui.lobby.hangar.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class EconomyWidgetVO extends DAAPIDataClass
   {
       
      
      public var isVisible:Boolean;
      
      public var bonusValue:String = "";
      
      public function EconomyWidgetVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
