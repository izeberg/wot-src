package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.white_tiger.gui.battle.views.shared.WhiteTigerDeploymentMapView;
   
   public class WhiteTigerBossTeleportViewMeta extends WhiteTigerDeploymentMapView
   {
       
      
      public var onTeleportPointClick:Function;
      
      public var onCancel:Function;
      
      public function WhiteTigerBossTeleportViewMeta()
      {
         super();
      }
      
      public function onTeleportPointClickS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onTeleportPointClick,"onTeleportPointClick" + Errors.CANT_NULL);
         this.onTeleportPointClick(param1);
      }
      
      public function onCancelS() : void
      {
         App.utils.asserter.assertNotNull(this.onCancel,"onCancel" + Errors.CANT_NULL);
         this.onCancel();
      }
   }
}
