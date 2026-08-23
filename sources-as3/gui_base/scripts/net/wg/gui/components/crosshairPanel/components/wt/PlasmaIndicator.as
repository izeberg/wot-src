package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.display.MovieClip;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class PlasmaIndicator extends SimpleDisposable
   {
      
      private static const VALUE_LABEL:String = "value";
      
      private static const VALUE_LABEL_END:String = "end";
       
      
      public var reticle:MovieClip = null;
      
      public var reticleSaved:MovieClip = null;
      
      private var _plasmaSaved:Number = -1;
      
      public function PlasmaIndicator()
      {
         super();
         this.reticleSaved.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.reticle = null;
         this.reticleSaved = null;
      }
      
      public function setPlasmaSaved(param1:Number) : void
      {
         this._plasmaSaved = param1;
         this.reticleSaved.visible = this._plasmaSaved > Values.DEFAULT_INT;
      }
      
      public function showPlasma(param1:Number, param2:Number) : void
      {
         var _loc3_:Number = Math.min(param1,this._plasmaSaved);
         var _loc4_:Boolean = this.reticleSaved.visible && param1 <= this._plasmaSaved;
         if(param1 == param2)
         {
            this.reticle.gotoAndStop(VALUE_LABEL + param1 + VALUE_LABEL_END);
            if(_loc4_)
            {
               this.reticleSaved.gotoAndStop(VALUE_LABEL + _loc3_ + VALUE_LABEL_END);
            }
            return;
         }
         this.reticle.gotoAndPlay(VALUE_LABEL + param1);
         if(_loc4_)
         {
            this.reticleSaved.gotoAndPlay(VALUE_LABEL + _loc3_);
         }
      }
   }
}
