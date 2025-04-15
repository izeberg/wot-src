package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.postmortemPanel.PostmortemPanel;
   
   public class PvePostmortemPanelMeta extends PostmortemPanel
   {
       
      
      public var updateTime:Function;
      
      public function PvePostmortemPanelMeta()
      {
         super();
      }
      
      public function updateTimeS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.updateTime,"updateTime" + Errors.CANT_NULL);
         this.updateTime(param1);
      }
   }
}
