package net.wg.gui.battle.views.widgetsPanel.vo
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class StateVO extends DAAPIDataClass
   {
       
      
      public var state:String;
      
      public var isInstantly:Boolean = false;
      
      public function StateVO(param1:Object)
      {
         super();
      }
   }
}
