package net.wg.gui.battle.views.widgetsPanel.settings
{
   public class WidgetProperties
   {
       
      
      public var linkage:String = null;
      
      public var cls:Class = null;
      
      public var alias:String = null;
      
      public function WidgetProperties(param1:String, param2:Class, param3:String)
      {
         super();
         this.linkage = param1;
         this.cls = param2;
         this.alias = param3;
      }
   }
}
