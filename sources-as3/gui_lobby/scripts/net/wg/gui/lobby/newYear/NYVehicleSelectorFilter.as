package net.wg.gui.lobby.newYear
{
   import net.wg.gui.lobby.components.VehicleSelectorFilter;
   
   public class NYVehicleSelectorFilter extends VehicleSelectorFilter
   {
       
      
      public function NYVehicleSelectorFilter()
      {
         super();
      }
      
      override protected function updateVisibility() : void
      {
         super.updateVisibility();
         compatibleOnlyCheckBox.visible = false;
         mainCheckBox.visible = false;
      }
   }
}
