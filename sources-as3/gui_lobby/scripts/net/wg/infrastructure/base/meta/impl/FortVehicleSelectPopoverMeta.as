package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.components.popovers.VehicleSelectPopoverBase;
   
   public class FortVehicleSelectPopoverMeta extends VehicleSelectPopoverBase
   {
       
      
      public var onFilterChange:Function;
      
      public var onFrozenChange:Function;
      
      public function FortVehicleSelectPopoverMeta()
      {
         super();
      }
      
      public function onFilterChangeS(param1:int, param2:Boolean) : void
      {
         App.utils.asserter.assertNotNull(this.onFilterChange,"onFilterChange" + Errors.CANT_NULL);
         this.onFilterChange(param1,param2);
      }
      
      public function onFrozenChangeS(param1:Boolean) : void
      {
         App.utils.asserter.assertNotNull(this.onFrozenChange,"onFrozenChange" + Errors.CANT_NULL);
         this.onFrozenChange(param1);
      }
   }
}
