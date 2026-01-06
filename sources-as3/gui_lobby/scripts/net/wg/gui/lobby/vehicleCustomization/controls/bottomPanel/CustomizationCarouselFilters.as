package net.wg.gui.lobby.vehicleCustomization.controls.bottomPanel
{
   import net.wg.data.VO.TankCarouselFilterSelectedVO;
   import net.wg.gui.components.carousels.filters.TankCarouselFilters;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationCarouselFilterSelectedVO;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterProps;
   
   public class CustomizationCarouselFilters extends TankCarouselFilters
   {
      
      private static const HIDDEN_COUNTER_INVALID:String = "hidden_Count_invalid";
      
      private static const COUNTER_PROPS:ICounterProps = new CounterProps(2,-2);
       
      
      private var _c11SelectedVO:CustomizationCarouselFilterSelectedVO = null;
      
      public function CustomizationCarouselFilters()
      {
         super();
      }
      
      override public function setSelectedData(param1:TankCarouselFilterSelectedVO) : void
      {
         super.setSelectedData(param1);
         if(param1 != null)
         {
            this._c11SelectedVO = CustomizationCarouselFilterSelectedVO(param1);
            invalidate(HIDDEN_COUNTER_INVALID);
         }
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._c11SelectedVO != null && isInvalid(HIDDEN_COUNTER_INVALID))
         {
            if(this._c11SelectedVO.newHiddenElementsCount > 0)
            {
               App.utils.counterManager.setCounter(paramsFilter,String(this._c11SelectedVO.newHiddenElementsCount),null,COUNTER_PROPS);
            }
            else
            {
               App.utils.counterManager.removeCounter(paramsFilter);
            }
         }
      }
      
      override protected function onDispose() : void
      {
         App.utils.counterManager.removeCounter(paramsFilter);
         this._c11SelectedVO = null;
         super.onDispose();
      }
   }
}
