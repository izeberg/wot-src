package net.wg.gui.components.crosshairPanel
{
   import flash.text.TextField;
   
   public class CrosshairSniper extends CrosshairWithCassette
   {
      
      private static const GUN_COOLING_INDICATOR_OFFSET:int = -175;
       
      
      public var zoomTF:TextField = null;
      
      private var _zoomIndicatorAlphaValue:Number = 1;
      
      private var _zoomStr:String = "";
      
      private var _reloadTimeBlinkYPositions:Array;
      
      private var _abilityModifierXPositions:Array;
      
      public function CrosshairSniper()
      {
         this._reloadTimeBlinkYPositions = [7,39,11,39,25];
         this._abilityModifierXPositions = [155,211,145,155,155];
         super();
      }
      
      override public function setComponentsAlpha(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : void
      {
         this._zoomIndicatorAlphaValue = param7;
         super.setComponentsAlpha(param1,param2,param3,param4,param5,param6,param7);
         this.zoomTF.alpha = this._zoomIndicatorAlphaValue;
      }
      
      override public function setNetType(param1:Number) : void
      {
         super.setNetType(param1);
         this.zoomTF.text = this._zoomStr;
         this.zoomTF.alpha = this._zoomIndicatorAlphaValue;
      }
      
      override public function setZoom(param1:String) : void
      {
         if(this._zoomStr == param1)
         {
            return;
         }
         this._zoomStr = param1;
         this.zoomTF.text = this._zoomStr;
      }
      
      override protected function onDispose() : void
      {
         this._reloadTimeBlinkYPositions.splice(0,this._reloadTimeBlinkYPositions.length);
         this._reloadTimeBlinkYPositions = null;
         this._abilityModifierXPositions.splice(0,this._abilityModifierXPositions.length);
         this._abilityModifierXPositions = null;
         this.zoomTF = null;
         super.onDispose();
      }
      
      override protected function getReloadTimeBlinkYPos() : Array
      {
         return this._reloadTimeBlinkYPositions;
      }
      
      override protected function getAbilityModifierXPos() : Array
      {
         return this._abilityModifierXPositions;
      }
      
      override protected function getGunCoolingIndicatorYOffset() : int
      {
         return GUN_COOLING_INDICATOR_OFFSET;
      }
   }
}
