package net.wg.gui.battle.views.widgetsPanel.vo
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class HotKeyVo extends DAAPIDataClass
   {
       
      
      public var command:String = "";
      
      public var keyCode:uint = 777;
      
      public var isLong:Boolean = false;
      
      public function HotKeyVo(param1:Object = null)
      {
         super(param1);
      }
   }
}
