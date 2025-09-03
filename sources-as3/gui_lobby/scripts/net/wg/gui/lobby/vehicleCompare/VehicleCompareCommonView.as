package net.wg.gui.lobby.vehicleCompare
{
   import flash.display.InteractiveObject;
   import net.wg.infrastructure.base.meta.IVehicleCompareCommonViewMeta;
   import net.wg.infrastructure.base.meta.impl.VehicleCompareCommonViewMeta;
   
   public class VehicleCompareCommonView extends VehicleCompareCommonViewMeta implements IVehicleCompareCommonViewMeta
   {
      
      protected static const TOP_PANEL_HEIGHT:int = 162;
       
      
      public function VehicleCompareCommonView()
      {
         super();
      }
      
      override protected function onInitModalFocus(param1:InteractiveObject) : void
      {
         super.onInitModalFocus(param1);
         var _loc2_:Vector.<InteractiveObject> = this.getFocusChain();
         if(_loc2_)
         {
            App.utils.commons.initTabIndex(_loc2_);
            setFocus(_loc2_[0]);
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      override protected function onEscapeKeyDown() : void
      {
         closeViewS();
      }
      
      protected function getFocusChain() : Vector.<InteractiveObject>
      {
         return null;
      }
   }
}
