package net.wg.gui.lobby.vehPostProgression
{
   import net.wg.data.constants.generated.HANGAR_ALIASES;
   import net.wg.gui.lobby.techtree.TechTreeEvent;
   import net.wg.infrastructure.base.meta.IVehiclePostProgressionViewMeta;
   import net.wg.infrastructure.base.meta.impl.VehiclePostProgressionViewMeta;
   
   public class VehPostProgressionView extends VehiclePostProgressionViewMeta implements IVehiclePostProgressionViewMeta
   {
      
      private static const COOLDOWN:int = 250;
       
      
      private var _requestInCoolDown:Boolean = false;
      
      public function VehPostProgressionView()
      {
         super();
      }
      
      override protected function onBeforeDispose() : void
      {
         App.utils.scheduler.cancelTask(this.deactivateCoolDown);
         _vehicleBlock.removeEventListener(TechTreeEvent.GO_TO_VEHICLE_VIEW,this.onRendererGoToVehicleViewHandler);
         _vehicleBlock.removeEventListener(TechTreeEvent.CLICK_VEHICLE_COMPARE,this.onRendererClickVehicleCompareHandler);
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.deactivateCoolDown();
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         vehParamsPanel.panel.showBottomShadowLipAlways = true;
         _vehicleBlock.addEventListener(TechTreeEvent.GO_TO_VEHICLE_VIEW,this.onRendererGoToVehicleViewHandler,false,0,true);
         _vehicleBlock.addEventListener(TechTreeEvent.CLICK_VEHICLE_COMPARE,this.onRendererClickVehicleCompareHandler,false,0,true);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerFlashComponentS(injectComponent,HANGAR_ALIASES.POST_PROGRESSION_INJECT);
      }
      
      private function activateCoolDown() : void
      {
         this._requestInCoolDown = true;
         App.utils.scheduler.scheduleTask(this.deactivateCoolDown,COOLDOWN);
      }
      
      private function deactivateCoolDown() : void
      {
         this._requestInCoolDown = false;
      }
      
      private function onRendererGoToVehicleViewHandler(param1:TechTreeEvent) : void
      {
         if(!this._requestInCoolDown && param1.index > -1 && _vo.vehicleButton.goToVehicleViewBtnVisible)
         {
            goToVehicleViewS();
            this.activateCoolDown();
         }
      }
      
      private function onRendererClickVehicleCompareHandler(param1:TechTreeEvent) : void
      {
         if(!this._requestInCoolDown && param1.index > -1)
         {
            compareVehicleS();
            this.activateCoolDown();
         }
      }
   }
}
