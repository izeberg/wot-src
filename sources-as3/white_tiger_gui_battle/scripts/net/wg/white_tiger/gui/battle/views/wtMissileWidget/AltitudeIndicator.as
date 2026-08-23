package net.wg.white_tiger.gui.battle.views.wtMissileWidget
{
   import fl.motion.easing.Quartic;
   import flash.display.MovieClip;
   import flash.filters.GlowFilter;
   import net.wg.gui.components.controls.TextFieldContainer;
   import net.wg.infrastructure.base.SimpleDisposable;
   import scaleform.clik.motion.Tween;
   
   public class AltitudeIndicator extends SimpleDisposable
   {
      
      private static const TWEEN_DURATION:uint = 190;
       
      
      public var valueTf:TextFieldContainer = null;
      
      public var bar:MovieClip = null;
      
      public var arrow:MovieClip = null;
      
      private var _maxAltitude:int = 0;
      
      private var _altitude:int = 0;
      
      private var _altitudePct:Number = 0;
      
      private var _appearanceTween:Tween = null;
      
      private var _valueTween:Tween = null;
      
      private var _rangeMeasureSymbol:String;
      
      private var _isUnset:Boolean = true;
      
      public function AltitudeIndicator()
      {
         super();
         this.valueTf.textFilters = [new GlowFilter(0,0.68,4,4,1.2,2)];
         this.valueTf.textField.text = INGAME_GUI.MARKER_METERS;
         this._rangeMeasureSymbol = this.valueTf.textField.text;
         this.updateAltitude();
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.clearAppearanceTween();
         this.clearValueTween();
         this._appearanceTween = null;
         this._valueTween = null;
         this.valueTf.dispose();
         this.valueTf = null;
         this.bar = null;
         this.arrow = null;
         super.onDispose();
      }
      
      public function resetAltitude() : void
      {
         gotoAndStop(1);
         alpha = 0;
         this._isUnset = true;
         this._altitude = 0;
         this.updateAltitude();
         this.clearAppearanceTween();
      }
      
      public function setAltitude(param1:Number) : void
      {
         if(this._altitude == param1)
         {
            return;
         }
         this.clearValueTween();
         this._valueTween = new Tween(TWEEN_DURATION,this,{"altitudeValue":param1},{"ease":Quartic.easeOut});
         if(this._isUnset)
         {
            this._isUnset = false;
            this.clearAppearanceTween();
            this._appearanceTween = new Tween(TWEEN_DURATION,this,{"alpha":1},{"ease":Quartic.easeOut});
         }
      }
      
      public function setMaxAltitude(param1:Number) : void
      {
         if(this._maxAltitude == param1)
         {
            return;
         }
         this._maxAltitude = param1;
         this._altitudePct = this._maxAltitude * 0.01;
      }
      
      private function clearAppearanceTween() : void
      {
         if(this._appearanceTween)
         {
            this._appearanceTween.dispose();
            this._appearanceTween = null;
         }
      }
      
      private function clearValueTween() : void
      {
         if(this._valueTween)
         {
            this._valueTween.dispose();
            this._valueTween = null;
         }
      }
      
      private function updateAltitude() : void
      {
         this.valueTf.label = this._altitude + this._rangeMeasureSymbol;
         var _loc1_:int = this._altitude / this._altitudePct;
         gotoAndStop(_loc1_);
      }
      
      public function get altitudeValue() : int
      {
         return this._altitude;
      }
      
      public function set altitudeValue(param1:int) : void
      {
         this._altitude = param1;
         this.updateAltitude();
      }
   }
}
