package net.wg.gui.notification.custom.vo
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class PM3QuestVehicleVO extends DAAPIDataClass
   {
       
      
      public var userName:String = "";
      
      public var isPrem:Boolean = false;
      
      public var type:String = "";
      
      public var levelRoman:String = "";
      
      public var level:int = 0;
      
      public function PM3QuestVehicleVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
