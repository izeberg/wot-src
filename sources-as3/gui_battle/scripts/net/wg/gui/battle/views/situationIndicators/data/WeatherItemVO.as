package net.wg.gui.battle.views.situationIndicators.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class WeatherItemVO extends DAAPIDataClass
   {
      
      public static const STATE_INACTIVE:int = 0;
      
      public static const STATE_ACTIVE:int = 1;
       
      
      public var weatherName:String = "";
      
      public var state:int = -1;
      
      public var toolTip:String = "";
      
      public function WeatherItemVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
