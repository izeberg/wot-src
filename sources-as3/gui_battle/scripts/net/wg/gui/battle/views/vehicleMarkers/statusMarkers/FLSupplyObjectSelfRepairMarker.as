package net.wg.gui.battle.views.vehicleMarkers.statusMarkers
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   
   public class FLSupplyObjectSelfRepairMarker extends VehicleAnimatedStatusBaseMarker
   {
      
      private static const TEXTFIELD_PADDING:int = 5;
      
      private static const OFFSET_X:int = 2;
      
      private static const SECONDS_IN_MIN:int = 60;
      
      private static const ZERO:String = "0";
      
      private static const TIMER_DEL:String = ":";
       
      
      public var iconMc:MovieClip = null;
      
      private var _animMc:MovieClip = null;
      
      private var _labelTF:TextField = null;
      
      private var _shadowMc:MovieClip = null;
      
      public function FLSupplyObjectSelfRepairMarker()
      {
         super();
         this._animMc = this.iconMc.animMc;
         this._labelTF = this.iconMc.labelTf;
         this._shadowMc = this.iconMc.shadowMc;
      }
      
      override public function updateEffectTimer(param1:int, param2:Boolean, param3:Boolean = false) : void
      {
         super.updateEffectTimer(param1,param2,param3);
         this.setLabelText(this.getTimeLeftStr(param1));
      }
      
      private function getTimeLeftStr(param1:int) : String
      {
         var _loc2_:int = param1 / SECONDS_IN_MIN;
         var _loc3_:int = param1 % SECONDS_IN_MIN;
         return this.getTimeStrDecimal(_loc2_) + TIMER_DEL + this.getTimeStrDecimal(_loc3_);
      }
      
      private function getTimeStrDecimal(param1:int) : String
      {
         return param1 < 10 ? ZERO + param1 : String(param1);
      }
      
      override protected function onHiddenStateShowed() : void
      {
         super.onHiddenStateShowed();
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.iconMc = null;
         this._animMc = null;
         this._labelTF = null;
         this._shadowMc = null;
         super.onDispose();
      }
      
      private function setLabelText(param1:String) : void
      {
         this._labelTF.text = param1;
         this._labelTF.width = this._labelTF.textWidth + TEXTFIELD_PADDING | 0;
         this.centerMarker();
      }
      
      private function centerMarker() : void
      {
         var _loc1_:int = this._animMc.width + this._labelTF.width + OFFSET_X >> 1;
         var _loc2_:int = this._animMc.width >> 1;
         this._animMc.x = -_loc1_ + _loc2_ + OFFSET_X | 0;
         this._labelTF.x = this._animMc.x + _loc2_ - OFFSET_X | 0;
         this._shadowMc.x = this._labelTF.x + (this._labelTF.width >> 1) | 0;
      }
   }
}
