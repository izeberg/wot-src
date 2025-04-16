package net.wg.frontline.gui.battle.views.frontlineMissionsPanel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class FrontlineMissionVO extends DAAPIDataClass
   {
       
      
      public var objectiveType:int = -1;
      
      public var objectiveID:int = -1;
      
      public var missionText:String = "";
      
      public var subText:String = "";
      
      public function FrontlineMissionVO(param1:Object)
      {
         super(param1);
      }
   }
}
