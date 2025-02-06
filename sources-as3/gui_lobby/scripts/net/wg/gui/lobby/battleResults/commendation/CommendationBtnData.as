package net.wg.gui.lobby.battleResults.commendation
{
   public class CommendationBtnData
   {
       
      
      public var iconPath:String;
      
      public var iconGlowPath:String;
      
      public var selectedIconPath:String;
      
      public var btnID:int;
      
      public function CommendationBtnData(param1:String, param2:String, param3:String, param4:int)
      {
         super();
         this.iconPath = param1;
         this.selectedIconPath = param3;
         this.iconGlowPath = param2;
         this.btnID = param4;
      }
   }
}
