package net.wg.historical_battles.gui.battle.views.respawn.components.card
{
   import flash.events.Event;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.historical_battles.gui.battle.constants.HB_STAGE_SIZE;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_VEHICLE_CARD_PROPS;
   
   public class HBVehicleImage extends BattleUIComponent
   {
      
      public static const HEIGHT:Object = {};
      
      private static const X_OFFSET:int = -30;
      
      {
         HEIGHT[HB_STAGE_SIZE.EXTRA_SMALL] = HB_VEHICLE_CARD_PROPS.getWidthWide(HB_STAGE_SIZE.EXTRA_SMALL);
         HEIGHT[HB_STAGE_SIZE.SMALL] = HB_VEHICLE_CARD_PROPS.getWidthWide(HB_STAGE_SIZE.SMALL);
         HEIGHT[HB_STAGE_SIZE.MEDIUM] = HB_VEHICLE_CARD_PROPS.getWidthWide(HB_STAGE_SIZE.MEDIUM);
         HEIGHT[HB_STAGE_SIZE.LARGE] = HB_VEHICLE_CARD_PROPS.getWidthWide(HB_STAGE_SIZE.LARGE);
         HEIGHT[HB_STAGE_SIZE.EXTRA_LARGE] = HB_VEHICLE_CARD_PROPS.getWidthWide(HB_STAGE_SIZE.EXTRA_LARGE);
      }
      
      public var image:UILoaderAlt = null;
      
      private var _source:String = null;
      
      private var _originalHeight:uint = 0;
      
      private var _size:uint = 0;
      
      public function HBVehicleImage()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.image.addEventListener(UILoaderEvent.COMPLETE,this.onImageCompleteHandler);
      }
      
      override protected function draw() : void
      {
         var _loc1_:Number = NaN;
         super.draw();
         if(this._source && this._originalHeight > 0 && isInvalid(InvalidationType.SIZE))
         {
            _loc1_ = HEIGHT[this._size] / this._originalHeight;
            this.image.scaleX = this.image.scaleY = _loc1_;
            this.image.x = (HB_VEHICLE_CARD_PROPS.getWidthWide(this._size) - this.image.width >> 1) + (X_OFFSET * _loc1_ | 0);
            this.image.visible = true;
         }
      }
      
      override protected function onDispose() : void
      {
         this.image.removeEventListener(UILoaderEvent.COMPLETE,this.onImageCompleteHandler);
         this.image.dispose();
         this.image = null;
         super.onDispose();
      }
      
      public function updateSize(param1:uint) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            invalidateSize();
         }
      }
      
      public function get source() : String
      {
         return this._source;
      }
      
      public function set source(param1:String) : void
      {
         if(this._source != param1)
         {
            this._source = param1;
            this.image.visible = false;
            this.image.source = this._source;
         }
      }
      
      private function onImageCompleteHandler(param1:Event) : void
      {
         this._originalHeight = this.image.height;
         invalidateSize();
      }
   }
}
