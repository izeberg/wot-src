package net.wg.white_tiger.gui.components.crosshairPanel
{
   import flash.display.MovieClip;
   
   public class BasePlasmaIndicator extends MovieClip
   {
      
      private static const VALUE_LABEL:String = "value";
      
      private static const VALUE_LABEL_END:String = "end";
      
      private static const PLASMA_DAMAGE_INDICATOR_X_OFFSET:Number = 75;
       
      
      public var wtReticle:MovieClip = null;
      
      public var plasmaDamageIndicator:PlasmaDamageTF = null;
      
      private var _plasmaDamageIndicatorYPos:Array = null;
      
      private var _plasmaDamageIndicatorScale:Array = null;
      
      private var _netType:Number = 0;
      
      public function BasePlasmaIndicator()
      {
         super();
         this.visible = false;
         this.plasmaDamageIndicator.visible = false;
         this._plasmaDamageIndicatorYPos = this.getPlasmaDamageIndicatorYPos();
         this._plasmaDamageIndicatorScale = this.getPlasmaDamageIndicatorScale();
         this.updatePlasmaIndicatorSize(this._netType);
      }
      
      public function set netType(param1:Number) : void
      {
         this._netType = param1;
      }
      
      public function showPlasma(param1:Number, param2:Boolean, param3:String) : void
      {
         this.visible = true;
         var _loc4_:Boolean = param1 != 0;
         if(this.plasmaDamageIndicator)
         {
            this.plasmaDamageIndicator.label = param3;
            this.plasmaDamageIndicator.visible = _loc4_;
         }
         if(!param2)
         {
            this.wtReticle.gotoAndStop(VALUE_LABEL + param1 + VALUE_LABEL_END);
            return;
         }
         this.wtReticle.gotoAndPlay(VALUE_LABEL + param1);
      }
      
      public function setPlasmaDamageIndicatorPosition(param1:Number, param2:Number) : void
      {
         this.plasmaDamageIndicator.x = param1;
         this.plasmaDamageIndicator.y = param2;
      }
      
      public function setPlasmaDamageIndicatorScale(param1:Number) : void
      {
         this.plasmaDamageIndicator.scaleX = this.plasmaDamageIndicator.scaleY = param1;
      }
      
      public function updatePlasmaIndicatorSize(param1:Number) : void
      {
         var _loc2_:Number = this._plasmaDamageIndicatorScale[param1];
         this.setPlasmaDamageIndicatorScale(_loc2_);
         var _loc3_:Number = (this.plasmaDamageIndicator.textField.textWidth >> 1) * -1 + PLASMA_DAMAGE_INDICATOR_X_OFFSET;
         var _loc4_:Number = this._plasmaDamageIndicatorYPos[param1];
         this.setPlasmaDamageIndicatorPosition(_loc3_,_loc4_);
      }
      
      protected function getPlasmaDamageIndicatorYPos() : Array
      {
         return [];
      }
      
      protected function getPlasmaDamageIndicatorScale() : Array
      {
         return [];
      }
   }
}
