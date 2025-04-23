package net.wg.frontline.gui.battle.views.modificationPanel.components
{
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.components.controls.UILoaderAlt;
   
   public class FrontlineModificationIcon extends BattleUIComponent
   {
       
      
      public var loader:UILoaderAlt = null;
      
      public function FrontlineModificationIcon()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.loader.dispose();
         this.loader = null;
         super.onDispose();
      }
      
      public function setIcon(param1:String) : void
      {
         this.loader.source = param1;
      }
   }
}
