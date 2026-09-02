package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.white_tiger.gui.battle.views.shared.WhiteTigerDeploymentMapView;
   
   public class WhiteTigerHunterRespawnViewMeta extends WhiteTigerDeploymentMapView
   {
       
      
      public var onRespawnPointClick:Function;
      
      public function WhiteTigerHunterRespawnViewMeta()
      {
         super();
      }
      
      public function onRespawnPointClickS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onRespawnPointClick,"onRespawnPointClick" + Errors.CANT_NULL);
         this.onRespawnPointClick(param1);
      }
   }
}
