package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.minimap.BaseMinimap;
   
   public class FrontlineMinimapMeta extends BaseMinimap
   {
       
      
      public var onZoomModeChanged:Function;
      
      public function FrontlineMinimapMeta()
      {
         super();
      }
      
      public function onZoomModeChangedS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.onZoomModeChanged,"onZoomModeChanged" + Errors.CANT_NULL);
         this.onZoomModeChanged(param1);
      }
   }
}
