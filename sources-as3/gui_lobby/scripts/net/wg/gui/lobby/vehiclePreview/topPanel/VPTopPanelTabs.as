package net.wg.gui.lobby.vehiclePreview.topPanel
{
   import net.wg.infrastructure.base.meta.IVehiclePreviewTopPanelTabsMeta;
   import net.wg.infrastructure.base.meta.impl.VehiclePreviewTopPanelTabsMeta;
   
   public class VPTopPanelTabs extends VehiclePreviewTopPanelTabsMeta implements IVehiclePreviewTopPanelTabsMeta, IVPTopPanel
   {
      
      private static const WIDTH:uint = 416;
      
      private static const HEIGHT:uint = 120;
       
      
      public function VPTopPanelTabs()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
      }
   }
}
