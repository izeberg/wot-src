package net.wg.frontline.gui.battle.views.modificationPanel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class FrontlineModificationPanelVO extends DAAPIDataClass
   {
       
      
      public var modificationIconPath:String = "";
      
      public var modificationTitle:String = "";
      
      public var modificationDescription:String = "";
      
      public function FrontlineModificationPanelVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
