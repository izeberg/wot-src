package net.wg.white_tiger.gui.battle.views.wtMissileWidget
{
   import flash.display.MovieClip;
   import flash.filters.GlowFilter;
   import net.wg.gui.components.controls.TextFieldContainer;
   import net.wg.white_tiger.infrastructure.base.meta.IWTMissileWidgetMeta;
   import net.wg.white_tiger.infrastructure.base.meta.impl.WTMissileWidgetMeta;
   
   public class WTMissileWidget extends WTMissileWidgetMeta implements IWTMissileWidgetMeta
   {
      
      private static const MISSILE_WIDGET_OFFSET_X:uint = 9;
      
      private static const MISSILE_WIDGET_OFFSET_Y:uint = 14;
       
      
      public var rangeTf:TextFieldContainer = null;
      
      public var aim:MovieClip = null;
      
      public var altitudeIndicator:AltitudeIndicator = null;
      
      public var rangeIndicator:MovieClip = null;
      
      private var _range:Number = 0;
      
      private var _rangeMeasureSymbol:String;
      
      public function WTMissileWidget()
      {
         super();
         mouseEnabled = mouseChildren = false;
         this.rangeTf.textFilters = [new GlowFilter(0,0.68,4,4,1.2,2)];
         this.rangeTf.textField.text = INGAME_GUI.MARKER_METERS;
         this._rangeMeasureSymbol = this.rangeTf.textField.text;
         this.updateRangeTf();
         this.as_hide(false);
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.rangeTf.dispose();
         this.rangeTf = null;
         this.aim = null;
         this.altitudeIndicator.dispose();
         this.altitudeIndicator = null;
         this.rangeIndicator = null;
         super.onDispose();
      }
      
      public function as_hide(param1:Boolean) : void
      {
         visible = false;
         gotoAndStop(1);
         this.altitudeIndicator.resetAltitude();
      }
      
      public function as_setAltitude(param1:Number) : void
      {
         this.altitudeIndicator.setAltitude(param1);
      }
      
      public function as_setMaxAltitude(param1:Number) : void
      {
         this.altitudeIndicator.setMaxAltitude(param1);
      }
      
      public function as_setRange(param1:Number) : void
      {
         if(this._range == param1)
         {
            return;
         }
         this._range = param1;
         this.updateRangeTf();
      }
      
      public function as_show(param1:Boolean) : void
      {
         visible = true;
         if(param1)
         {
            gotoAndPlay(1);
         }
         else
         {
            gotoAndStop(totalFrames);
         }
      }
      
      public function updatePosition(param1:Number, param2:Number) : void
      {
         x = (param1 - this.width >> 1) - MISSILE_WIDGET_OFFSET_X;
         y = (param2 - this.width >> 1) + MISSILE_WIDGET_OFFSET_Y;
      }
      
      private function updateRangeTf() : void
      {
         this.rangeTf.label = this._range + this._rangeMeasureSymbol;
      }
      
      override public function get width() : Number
      {
         return this.rangeIndicator.width;
      }
      
      override public function get height() : Number
      {
         return this.rangeIndicator.height;
      }
   }
}
