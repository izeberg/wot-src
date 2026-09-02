package net.wg.gui.components.crosshairPanel.wt
{
   import flash.display.DisplayObject;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.crosshairPanel.CrosshairArcade;
   import net.wg.gui.components.crosshairPanel.components.wt.BarrierHint;
   
   public class WTCrosshairArcade extends CrosshairArcade
   {
      
      private static const PLASMA_DAMAGE_Y_HORIZONTAL:Number = 240;
      
      private static const PLASMA_DAMAGE_Y_DIAGONAL:Number = 152;
      
      private static const PLASMA_DAMAGE_Y_RADIAL:Number = 152;
      
      private static const PLASMA_DAMAGE_Y_DASHED:Number = 152;
      
      private static const PLASMA_DAMAGE_Y_SIEGE:Number = 152;
       
      
      public var wtBarrierHint:BarrierHint = null;
      
      private var _isBarrierShown:Boolean = false;
      
      private var _netTypeDirty:Number = -1;
      
      public function WTCrosshairArcade()
      {
         super();
         this.setComponentVisibility(this.wtBarrierHint,false);
      }
      
      override public function setNetType(param1:Number) : void
      {
         if(this._isBarrierShown)
         {
            this._netTypeDirty = param1;
            return;
         }
         super.setNetType(param1);
      }
      
      override protected function onDispose() : void
      {
         this.wtBarrierHint.dispose();
         this.wtBarrierHint = null;
         super.onDispose();
      }
      
      override protected function setComponentVisibility(param1:DisplayObject, param2:Boolean) : void
      {
         if(this._isBarrierShown)
         {
            visibilityMap[param1.name] = param2;
         }
         else
         {
            super.setComponentVisibility(param1,param2);
         }
      }
      
      override protected function getPlasmaExtraDamageYPos() : Array
      {
         return [PLASMA_DAMAGE_Y_DIAGONAL,PLASMA_DAMAGE_Y_HORIZONTAL,PLASMA_DAMAGE_Y_RADIAL,PLASMA_DAMAGE_Y_DASHED,PLASMA_DAMAGE_Y_SIEGE];
      }
      
      public function showBarrier(param1:Boolean, param2:String) : void
      {
         var _loc3_:DisplayObject = null;
         if(this._isBarrierShown == param1)
         {
            return;
         }
         this._isBarrierShown = param1;
         if(this._isBarrierShown)
         {
            cleanVisibilityMap();
         }
         var _loc4_:int = 0;
         while(_loc4_ < numChildren)
         {
            _loc3_ = getChildAt(_loc4_);
            if(this._isBarrierShown)
            {
               visibilityMap[_loc3_.name] = _loc3_.visible;
               _loc3_.visible = false;
            }
            else
            {
               _loc3_.visible = visibilityMap[_loc3_.name];
            }
            _loc4_++;
         }
         this.wtBarrierHint.visible = this._isBarrierShown;
         this.wtBarrierHint.setBindKey(param2);
         if(this._netTypeDirty != Values.DEFAULT_INT)
         {
            this.setNetType(this._netTypeDirty);
            this._netTypeDirty = Values.DEFAULT_INT;
         }
      }
   }
}
