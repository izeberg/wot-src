package net.wg.gui.lobby.hangar.ammunitionPanel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class AmmunitionPanelBtnVO extends DAAPIDataClass
   {
       
      
      public var visible:Boolean = false;
      
      public var enabled:Boolean = false;
      
      public var tooltip:String = "";
      
      public var isNew:Boolean = false;
      
      public function AmmunitionPanelBtnVO(param1:Object)
      {
         super(param1);
      }
   }
}
