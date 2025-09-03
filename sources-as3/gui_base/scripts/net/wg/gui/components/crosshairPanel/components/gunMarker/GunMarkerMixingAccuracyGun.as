package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import flash.display.Graphics;
   import flash.display.LineScaleMode;
   import flash.display.Shape;
   import net.wg.gui.utils.GraphicsUtilities;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class GunMarkerMixingAccuracyGun extends SimpleContainer implements IGunMarkerMixing
   {
      
      private static const RADIUS:uint = 256;
      
      private static const MAX_STACKS:uint = 4;
      
      private static const ACCURACY_FOR_STACK:Number = 0.12;
      
      private static const FULL_CIRCLE:Number = Math.PI * 2;
      
      private static const QUADRANT:Number = Math.PI / 2;
      
      private static const GAP_ANGLE:Number = Math.PI * 0.05;
      
      private static const GAP_ARC_ANGLE:Number = Math.PI * 0.01;
      
      private static const GAP_ARC_STEP:Number = Math.PI * 0.004;
      
      private static const GAP_ARC_STEP_BOUGHT_SIDES:Number = GAP_ARC_STEP * 2;
      
      private static const STACK_RADIUS_STEP:Number = RADIUS * ACCURACY_FOR_STACK;
      
      private static const GAP_WITH_ARK_OFFSET:Number = GAP_ANGLE - GAP_ARC_ANGLE * 2;
      
      private static const THICKNESS_THIN:uint = 1;
      
      private static const THICKNESS_BOLD:uint = 2;
      
      private static const THIN_ZOOM:uint = 4;
      
      private static const ARCS_COLOR:Number = 16774606;
      
      private static const RELOAD_COLOR:Number = 16711680;
      
      private static const EMPTY_COLOR:Number = 9305906;
       
      
      private var _curPercents:Number = 0;
      
      private var _circleShape:Shape;
      
      private var _accuracyStacks:uint = 0;
      
      private var _thickness:uint = 2;
      
      public function GunMarkerMixingAccuracyGun()
      {
         this._circleShape = new Shape();
         super();
         addChild(this._circleShape);
         this.setReloadingAsPercent(1);
         rotation -= 90;
      }
      
      private static function drawArc(param1:Graphics, param2:Number, param3:Number, param4:Number, param5:uint, param6:Number, param7:Number, param8:Number = 16711680) : void
      {
         param2 = (param2 + FULL_CIRCLE) % FULL_CIRCLE;
         var _loc9_:Number = (param2 + param3) % FULL_CIRCLE;
         param1.lineStyle(param5,EMPTY_COLOR,param6,false,LineScaleMode.NONE);
         GraphicsUtilities.drawArc(param1,0,0,param2,param3,param4);
         var _loc10_:Number = 0;
         if(param2 < _loc9_)
         {
            if(param7 >= _loc9_)
            {
               _loc10_ = param3;
            }
            else if(param7 > param2)
            {
               _loc10_ = param7 - param2;
            }
         }
         else if(param7 >= param2 || param7 > 0 && param7 <= _loc9_)
         {
            _loc10_ = param7 >= param2 ? Number(param7 - param2) : Number(FULL_CIRCLE - param2 + param7);
         }
         if(_loc10_ > 0)
         {
            param1.lineStyle(param5,param8,param6,false,LineScaleMode.NONE);
            GraphicsUtilities.drawArc(param1,0,0,param2,_loc10_,param4);
         }
      }
      
      private static function drawSolidArc(param1:Graphics, param2:Number, param3:Number, param4:Number, param5:uint, param6:Number, param7:Number) : void
      {
         param1.lineStyle(param5,param7,param6,false,LineScaleMode.NONE);
         GraphicsUtilities.drawArc(param1,0,0,param2,param3,param4);
      }
      
      override protected function onDispose() : void
      {
         removeChild(this._circleShape);
         this._circleShape = null;
         super.onDispose();
      }
      
      public function setStacks(param1:uint) : void
      {
         if(param1 != this._accuracyStacks)
         {
            this._accuracyStacks = param1;
            this.drawCircle();
         }
      }
      
      private function drawMainArcs(param1:Graphics, param2:Number, param3:Number, param4:Number) : void
      {
         var _loc5_:Number = this._accuracyStacks > 0 ? Number(GAP_ANGLE) : Number(0);
         var _loc6_:Number = Math.PI + QUADRANT + _loc5_;
         var _loc7_:Number = QUADRANT - _loc5_;
         var _loc8_:Number = 0;
         var _loc9_:Number = QUADRANT + _loc5_;
         var _loc10_:Number = Math.PI - _loc5_ * 2;
         drawArc(param1,_loc6_,_loc7_,param2,this._thickness,param3,param4);
         drawArc(param1,_loc8_,_loc7_,param2,this._thickness,param3,param4);
         drawArc(param1,_loc9_,_loc10_,param2,this._thickness,param3,param4);
      }
      
      private function drawStacks(param1:Graphics, param2:Number) : void
      {
         var _loc7_:Boolean = false;
         var _loc8_:Number = NaN;
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc3_:Number = RADIUS - STACK_RADIUS_STEP * (MAX_STACKS - this._accuracyStacks);
         var _loc4_:Number = 1;
         var _loc5_:Number = 0.6;
         var _loc6_:uint = 0;
         while(_loc6_ < MAX_STACKS)
         {
            _loc7_ = this._accuracyStacks > 0 && _loc6_ == MAX_STACKS - this._accuracyStacks;
            _loc8_ = _loc3_ + _loc6_ * STACK_RADIUS_STEP;
            _loc9_ = -(QUADRANT + GAP_ARC_STEP * _loc6_) - GAP_ARC_ANGLE;
            _loc10_ = GAP_WITH_ARK_OFFSET + GAP_ARC_STEP_BOUGHT_SIDES * (_loc6_ - 1);
            if(_loc7_)
            {
               drawArc(param1,_loc9_,_loc10_,_loc8_,this._thickness,_loc4_,param2,RELOAD_COLOR);
               drawArc(param1,_loc9_ + Math.PI,_loc10_,_loc8_,this._thickness,_loc4_,param2,RELOAD_COLOR);
            }
            else
            {
               drawSolidArc(param1,_loc9_,_loc10_,_loc8_,this._thickness,_loc5_,ARCS_COLOR);
               drawSolidArc(param1,_loc9_ + Math.PI,_loc10_,_loc8_,this._thickness,_loc5_,ARCS_COLOR);
            }
            _loc6_++;
         }
      }
      
      private function drawCircle() : void
      {
         var _loc1_:Graphics = this._circleShape.graphics;
         _loc1_.clear();
         var _loc2_:Number = FULL_CIRCLE * (1 - this._curPercents);
         if(_loc2_ >= FULL_CIRCLE)
         {
            _loc2_ -= FULL_CIRCLE;
         }
         this.drawMainArcs(_loc1_,RADIUS,1,_loc2_);
         this.drawStacks(_loc1_,_loc2_);
      }
      
      public function setReloadingAsPercent(param1:Number, param2:Boolean = false) : void
      {
         if(this._curPercents != param1 || param2)
         {
            this._curPercents = param1;
            this.drawCircle();
         }
      }
      
      public function setZoomFactor(param1:Number) : void
      {
         this._thickness = param1 > THIN_ZOOM ? uint(THICKNESS_BOLD) : uint(THICKNESS_THIN);
         this.drawCircle();
      }
      
      public function setReloadingState(param1:String) : void
      {
      }
      
      public function setThickness(param1:String) : void
      {
      }
   }
}
