package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.lobby.vehPostProgression.VehPostProgressionViewBase;
   
   public class VehiclePostProgressionViewMeta extends VehPostProgressionViewBase
   {
       
      
      public var goToVehicleView:Function;
      
      public var compareVehicle:Function;
      
      public function VehiclePostProgressionViewMeta()
      {
         super();
      }
      
      public function goToVehicleViewS() : void
      {
         App.utils.asserter.assertNotNull(this.goToVehicleView,"goToVehicleView" + Errors.CANT_NULL);
         this.goToVehicleView();
      }
      
      public function compareVehicleS() : void
      {
         App.utils.asserter.assertNotNull(this.compareVehicle,"compareVehicle" + Errors.CANT_NULL);
         this.compareVehicle();
      }
   }
}
