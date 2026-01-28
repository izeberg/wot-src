package net.wg.gui.lobby.epicBattles.components
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import net.wg.data.constants.Values;
   import net.wg.gui.lobby.epicBattles.data.EpicBattlesWidgetEvent;
   import net.wg.gui.lobby.epicBattles.data.EpicBattlesWidgetVO;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class EpicBattlesWidgetButton extends EpicBattlesWidgetBaseButton
   {
      
      private static const COUNTER_CONTAINER_ID:String = "epicBattlesWidget";
      
      private static const OFFSET_COUNTER_X:int = -10;
      
      private static const OFFSET_COUNTER_Y:int = 50;
      
      private static const HIT_AREA_SIZE_SMALL:uint = 130;
      
      private static const HIT_AREA_SIZE_BIG:uint = 150;
      
      private static const OFFSET_POINTS_X_SMALL:uint = 6;
      
      private static const OFFSET_POINTS_X_BIG:uint = 8;
      
      private static const OFFSET_POINTS_Y_SMALL:uint = 98;
      
      private static const OFFSET_POINTS_Y_BIG:uint = 60;
      
      private static const MARGIN_RIGHT_DEFAULT:int = 25;
      
      private static const MARGIN_RIGHT_SMALL:int = -5;
      
      private static const MARGIN_RIGHT_BIG:int = 80;
       
      
      public var widget:EpicBattlesWidgetComponent = null;
      
      public var reservesPoints:EpicReservesPointsPanel = null;
      
      public var hitMc:MovieClip = null;
      
      private var _counterManager:ICounterManager;
      
      private var _counterValue:int = 0;
      
      public function EpicBattlesWidgetButton()
      {
         this._counterManager = App.utils.counterManager;
         super();
      }
      
      override protected function init() : void
      {
         this.widget.hitArea = this.hitMc;
         this.widget.buttonMode = true;
         this.widget.addEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.widget.addEventListener(MouseEvent.ROLL_OVER,onRollOverHandler);
         this.widget.addEventListener(MouseEvent.ROLL_OUT,onRollOutHandler);
         addEventListener(EpicBattlesWidgetEvent.LAYOUT_CHANGE,this.onLayoutChange);
      }
      
      override protected function onDispose() : void
      {
         this.widget.removeEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.widget.removeEventListener(MouseEvent.ROLL_OVER,onRollOverHandler);
         this.widget.removeEventListener(MouseEvent.ROLL_OUT,onRollOutHandler);
         removeEventListener(EpicBattlesWidgetEvent.LAYOUT_CHANGE,this.onLayoutChange);
         this.hitMc = null;
         this.widget.dispose();
         this.widget = null;
         this.reservesPoints.dispose();
         this.reservesPoints = null;
         this._counterManager.disposeCountersForContainer(COUNTER_CONTAINER_ID);
         this._counterManager = null;
         super.onDispose();
      }
      
      private function onClickHandler(param1:MouseEvent) : void
      {
         if(param1.target == this.widget && App.utils.commons.isLeftButton(param1))
         {
            dispatchClickEvent();
         }
      }
      
      private function setCounter() : void
      {
         var _loc1_:CounterProps = null;
         this._counterManager.removeCounter(this.widget,COUNTER_CONTAINER_ID);
         if(this._counterValue > Values.ZERO)
         {
            _loc1_ = new CounterProps(OFFSET_COUNTER_X,OFFSET_COUNTER_Y);
            this._counterManager.setCounter(this.widget,this._counterValue.toString(),COUNTER_CONTAINER_ID,_loc1_);
         }
      }
      
      private function onLayoutChange(param1:EpicBattlesWidgetEvent) : void
      {
         this.updateSize();
      }
      
      public function setData(param1:EpicBattlesWidgetVO) : void
      {
         this.widget.setData(param1);
         this.reservesPoints.visible = StringUtils.isNotEmpty(param1.points);
         this.reservesPoints.setData(param1.points);
         this._counterValue = !!param1.isSupplyHint ? int(Values.ZERO) : int(param1.counterValue);
      }
      
      override public function updateSize() : void
      {
         this.hitMc.width = this.hitMc.height = !!isSmallHeight ? Number(HIT_AREA_SIZE_SMALL) : Number(HIT_AREA_SIZE_BIG);
         this.widget.invalidateSize();
         this.reservesPoints.x = (this.widget.ribbonWidth >> 1) - (!!isSmallWidth ? OFFSET_POINTS_X_SMALL : OFFSET_POINTS_X_BIG);
         this.reservesPoints.y = !!isSmallWidth ? Number(OFFSET_POINTS_Y_SMALL) : Number(OFFSET_POINTS_Y_BIG);
         this.reservesPoints.updateSize(isSmallWidth);
         this.setCounter();
      }
      
      public function get marginRight() : int
      {
         if(this.reservesPoints.visible)
         {
            return !!isSmallWidth ? int(MARGIN_RIGHT_SMALL) : int(MARGIN_RIGHT_BIG);
         }
         return MARGIN_RIGHT_DEFAULT;
      }
      
      public function get marginLeft() : int
      {
         return MARGIN_RIGHT_DEFAULT;
      }
   }
}
