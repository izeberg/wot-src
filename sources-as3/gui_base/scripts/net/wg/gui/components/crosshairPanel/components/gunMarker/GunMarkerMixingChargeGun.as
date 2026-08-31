package net.wg.gui.components.crosshairPanel.components.gunMarker
{
   import flash.display.BitmapData;
   import flash.display.CapsStyle;
   import flash.display.LineScaleMode;
   import flash.events.Event;
   import flash.geom.Matrix;
   import flash.utils.getDefinitionByName;
   import net.wg.gui.utils.GraphicsUtilities;
   import net.wg.infrastructure.base.SimpleContainer;
   
   public class GunMarkerMixingChargeGun extends SimpleContainer
   {
      
      private static const ROTATION_OFFSET:int = 90;
      
      private static const GAP_RATIO:Number = 0.03;
      
      private static const SEGMENT_NOTCH_RATIO:Number = 0.15;
      
      private static const NO_NOTCH:int = -1;
      
      private static const LINE_ALPHA:Number = 1;
      
      private static const RENDER_AREA_ALPHA:Number = 0;
      
      private static const GLOW_RADIUS:uint = 350;
      
      private static const GLOW_ARCADE_LINKAGE:String = "ChargeGunGlowArcadeUI";
      
      private static const GLOW_SNIPER_LINKAGE:String = "ChargeGunGlowSniperUI";
      
      private static const RADIUS:uint = 256;
      
      private static const OVERHEAT_RADIUS:uint = 240;
      
      private static const NOTCH_LENGTH:uint = 8;
      
      private static const GLOW_NOTCH_LENGTH:uint = 14;
      
      private static const MAIN_COLOR:uint = 16751872;
      
      private static const MAIN_COLOR_SMALL:uint = 264600064;
      
      private static const RELOAD_COLOR:uint = 16751872;
      
      private static const RELOAD_COLOR_SMALL:uint = 264600064;
      
      private static const RELOAD_PROGRESS_COLOR:uint = 16751872;
      
      private static const RELOAD_PROGRESS_COLOR_SMALL:uint = 16758854;
      
      private static const READY_COLOR:uint = 15919035;
      
      private static const OVERHEAT_COLOR:uint = 16730685;
      
      private static const ARC_THICKNESS_SMALL:uint = 2;
      
      private static const ARC_THICKNESS_LARGE:uint = 2;
      
      private static const PROGRESS_THICKNESS_SMALL:uint = 2;
      
      private static const PROGRESS_THICKNESS_MEDIUM:uint = 4;
      
      private static const PROGRESS_THICKNESS_LARGE:uint = 6;
      
      private static const OVERHEAT_THICKNESS_SMALL:uint = 2;
      
      private static const OVERHEAT_THICKNESS_MEDIUM:uint = 4;
      
      private static const OVERHEAT_THICKNESS_LARGE:uint = 6;
      
      private static const ARC_PROGRESS_EXTRA_RADIUS_SMALL:uint = 4;
      
      private static const ARC_PROGRESS_EXTRA_RADIUS_LARGE:uint = 2;
      
      private static const NOTCH_THICKNESS:uint = 2;
      
      private static const NOTCH_THICKNESS_LARGE:uint = 4;
      
      private static const ZOOM_FACTOR_BREAKPOINT_SMALL:Number = 2;
      
      private static const ZOOM_FACTOR_BREAKPOINT_MEDIUM:Number = 8;
      
      private static const ZOOM_FACTOR_BREAKPOINT_LARGE:Number = 16;
      
      private static const ZOOM_FACTOR_BREAKPOINT_HUGE:Number = 25;
      
      private static const SECTION_GAP:Number = Math.PI * GAP_RATIO;
      
      private static const HALF_PI:Number = Math.PI / 2;
      
      private static const SEGMENT_LEAD:Number = HALF_PI * SEGMENT_NOTCH_RATIO;
      
      private static const SEGMENTS:Array = [{
         "start":Math.PI + HALF_PI,
         "length":SEGMENT_LEAD,
         "notch":HALF_PI - SEGMENT_LEAD
      },{
         "start":Math.PI + HALF_PI + SEGMENT_LEAD + SECTION_GAP,
         "length":HALF_PI - SEGMENT_LEAD - SECTION_GAP * 2,
         "notch":SECTION_GAP
      },{
         "start":0,
         "length":HALF_PI,
         "notch":NO_NOTCH
      }];
      
      private static const RENDER_AREA_SIZE:uint = 700;
      
      private static const MARKER_DRAW_INVALID:String = "invalidMarker";
      
      private static const MAX_STACKS:uint = 3;
      
      private static const SMOOTHING_FACTOR:Number = 0.2;
      
      private static const PROGRESS_TOLERANCE:Number = 0.001;
      
      private static const DIRECT_THRESHOLD:Number = 0.25;
      
      private static const SPEED_MULTIPLIER:Number = 1.25;
      
      private static const SPEED_SMOOTHING:Number = SMOOTHING_FACTOR * SPEED_MULTIPLIER;
       
      
      private var _zoomFactor:Number = 1.0;
      
      private var _chargeProgress:Number = 0;
      
      private var _stacks:uint = 0;
      
      private var _currentProgress:Number = 0;
      
      private var _targetProgress:Number = 0;
      
      private var _needUpdate:Boolean = false;
      
      private var _glowMatrix:Matrix;
      
      private var _glowTextureArcade:BitmapData;
      
      private var _glowTextureSniper:BitmapData;
      
      public function GunMarkerMixingChargeGun()
      {
         super();
         rotation -= ROTATION_OFFSET;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         var _loc1_:Class = getDefinitionByName(GLOW_ARCADE_LINKAGE) as Class;
         this._glowTextureArcade = new _loc1_();
         _loc1_ = getDefinitionByName(GLOW_SNIPER_LINKAGE) as Class;
         this._glowTextureSniper = new _loc1_();
         this._glowMatrix = new Matrix();
         this._glowMatrix.translate(-GLOW_RADIUS,-GLOW_RADIUS);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(MARKER_DRAW_INVALID))
         {
            graphics.clear();
            this.drawMarker();
         }
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
         if(this._glowTextureArcade)
         {
            this._glowTextureArcade.dispose();
            this._glowTextureArcade = null;
         }
         if(this._glowTextureSniper)
         {
            this._glowTextureSniper.dispose();
            this._glowTextureSniper = null;
         }
         this._glowMatrix = null;
         super.onDispose();
      }
      
      public function setChargeGunState(param1:Number, param2:uint) : void
      {
         this._stacks = param2;
         if(Math.abs(param1 - this._currentProgress) >= DIRECT_THRESHOLD)
         {
            this._currentProgress = param1;
            this._chargeProgress = this._currentProgress;
            this._needUpdate = false;
            invalidate(MARKER_DRAW_INVALID);
         }
         else
         {
            this._targetProgress = param1;
            if(!this._needUpdate)
            {
               this._needUpdate = true;
               addEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler,false,0,true);
            }
         }
      }
      
      public function set zoomFactor(param1:Number) : void
      {
         if(param1 == this._zoomFactor)
         {
            return;
         }
         this._zoomFactor = param1;
         invalidate(MARKER_DRAW_INVALID);
      }
      
      private function onEnterFrameHandler(param1:Event) : void
      {
         var _loc2_:Number = this._targetProgress - this._currentProgress;
         if(Math.abs(_loc2_) >= DIRECT_THRESHOLD)
         {
            this._currentProgress = this._targetProgress;
            this._needUpdate = false;
         }
         else if(Math.abs(_loc2_) <= PROGRESS_TOLERANCE)
         {
            this._currentProgress = this._targetProgress;
            this._needUpdate = false;
         }
         else
         {
            this._currentProgress += _loc2_ * SPEED_SMOOTHING;
         }
         if(this._currentProgress > 1)
         {
            this._currentProgress = 1;
         }
         this._chargeProgress = this._currentProgress;
         invalidate(MARKER_DRAW_INVALID);
         if(!this._needUpdate)
         {
            removeEventListener(Event.ENTER_FRAME,this.onEnterFrameHandler);
         }
      }
      
      private function drawMarker() : void
      {
         var _loc1_:Object = null;
         var _loc2_:uint = 0;
         var _loc3_:int = 0;
         var _loc4_:Object = null;
         this.drawRenderArea();
         this.updateLineStyle(this.arcThickness,this.mainColor);
         for each(_loc1_ in SEGMENTS)
         {
            this.drawArcBoth(_loc1_.start,_loc1_.length);
         }
         _loc2_ = SEGMENTS.length;
         _loc3_ = 0;
         while(_loc3_ < _loc2_)
         {
            _loc4_ = SEGMENTS[_loc3_];
            if(this._stacks > _loc3_)
            {
               this.updateLineStyle(this.arcThickness,READY_COLOR);
               this.drawArcBoth(_loc4_.start,_loc4_.length);
               if(_loc4_.notch != NO_NOTCH)
               {
                  this.updateLineStyle(this.notchThickness,READY_COLOR);
                  this.drawNotchBoth(_loc4_.notch,GLOW_NOTCH_LENGTH);
               }
               this.drawGlowBoth(_loc4_.start,_loc4_.length);
               this.updateLineStyle(this.progressThickness,READY_COLOR);
               this.drawArcBoth(_loc4_.start,_loc4_.length,this.arcProgressRadius);
            }
            else if(this._stacks == _loc3_)
            {
               this.updateLineStyle(this.arcThickness,this.progressColor);
               this.drawArcBoth(_loc4_.start,_loc4_.length);
               if(_loc4_.notch != NO_NOTCH)
               {
                  this.drawNotchBoth(_loc4_.notch);
               }
               this.updateLineStyle(this.progressThickness,this.progressProcessColor);
               this.drawArcBoth(_loc4_.start,_loc4_.length * this._chargeProgress,this.arcProgressRadius);
            }
            _loc3_++;
         }
         if(this._stacks === MAX_STACKS)
         {
            this.updateLineStyle(this.overheatThickness,OVERHEAT_COLOR);
            this.drawArcBoth(Math.PI + HALF_PI,Math.PI - Math.PI * this._chargeProgress,OVERHEAT_RADIUS);
         }
      }
      
      private function updateLineStyle(param1:Number, param2:uint) : void
      {
         graphics.lineStyle(param1,param2,LINE_ALPHA,false,LineScaleMode.NONE,CapsStyle.NONE);
      }
      
      private function drawArc(param1:Number, param2:Number, param3:uint = 256) : void
      {
         GraphicsUtilities.drawArc(graphics,0,0,param1,param2,param3);
      }
      
      private function drawGlow(param1:Number, param2:Number) : void
      {
         graphics.lineStyle();
         graphics.beginBitmapFill(this.getGlowTexture(),this._glowMatrix,false,true);
         var _loc3_:Number = param1;
         var _loc4_:Number = GLOW_RADIUS * Math.cos(_loc3_);
         var _loc5_:Number = GLOW_RADIUS * Math.sin(-_loc3_);
         graphics.moveTo(_loc4_,_loc5_);
         GraphicsUtilities.drawArc(graphics,0,0,_loc3_,param2,GLOW_RADIUS);
         graphics.lineTo(0,0);
         graphics.endFill();
      }
      
      private function getGlowTexture() : BitmapData
      {
         return this._zoomFactor < ZOOM_FACTOR_BREAKPOINT_MEDIUM ? this._glowTextureArcade : this._glowTextureSniper;
      }
      
      private function drawArcBoth(param1:Number, param2:Number, param3:uint = 256) : void
      {
         this.drawArc(param1,param2,param3);
         this.drawArc(Math.PI - param1 - param2,param2,param3);
      }
      
      private function drawGlowBoth(param1:Number, param2:Number) : void
      {
         this.drawGlow(param1,param2);
         this.drawGlow(Math.PI - param1 - param2,param2);
      }
      
      private function drawNotchBoth(param1:Number, param2:Number = 8) : void
      {
         this.drawNotchAt(param1,param2);
         this.drawNotchAt(Math.PI - param1,param2);
      }
      
      private function drawNotchAt(param1:Number, param2:Number = 8) : void
      {
         var _loc3_:Number = RADIUS * Math.cos(param1);
         var _loc4_:Number = RADIUS * Math.sin(param1);
         var _loc5_:Number = (RADIUS + param2) * Math.cos(param1);
         var _loc6_:Number = (RADIUS + param2) * Math.sin(param1);
         graphics.moveTo(_loc3_,_loc4_);
         graphics.lineTo(_loc5_,_loc6_);
      }
      
      private function drawRenderArea() : void
      {
         graphics.lineStyle();
         graphics.beginFill(RENDER_AREA_ALPHA,RENDER_AREA_ALPHA);
         graphics.drawRect(-RENDER_AREA_SIZE >> 1,-RENDER_AREA_SIZE >> 1,RENDER_AREA_SIZE,RENDER_AREA_SIZE);
         graphics.endFill();
      }
      
      private function get arcThickness() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
               return ARC_THICKNESS_SMALL;
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return ARC_THICKNESS_LARGE;
            default:
               return ARC_THICKNESS_SMALL;
         }
      }
      
      private function get notchThickness() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
               return NOTCH_THICKNESS;
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return NOTCH_THICKNESS_LARGE;
            default:
               return NOTCH_THICKNESS;
         }
      }
      
      private function get arcProgressRadius() : uint
      {
         var _loc1_:uint = ARC_PROGRESS_EXTRA_RADIUS_SMALL;
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               _loc1_ = ARC_PROGRESS_EXTRA_RADIUS_LARGE;
         }
         return RADIUS + _loc1_ - this.arcThickness / 2;
      }
      
      private function get progressThickness() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
               return PROGRESS_THICKNESS_SMALL;
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
               return PROGRESS_THICKNESS_MEDIUM;
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return PROGRESS_THICKNESS_LARGE;
            default:
               return PROGRESS_THICKNESS_SMALL;
         }
      }
      
      private function get progressColor() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
               return RELOAD_COLOR_SMALL;
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return RELOAD_COLOR;
            default:
               return RELOAD_COLOR_SMALL;
         }
      }
      
      private function get mainColor() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
               return MAIN_COLOR_SMALL;
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return MAIN_COLOR;
            default:
               return MAIN_COLOR_SMALL;
         }
      }
      
      private function get progressProcessColor() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
               return RELOAD_PROGRESS_COLOR_SMALL;
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return RELOAD_PROGRESS_COLOR;
            default:
               return RELOAD_PROGRESS_COLOR_SMALL;
         }
      }
      
      private function get overheatThickness() : uint
      {
         switch(this._zoomFactor)
         {
            case ZOOM_FACTOR_BREAKPOINT_SMALL:
               return OVERHEAT_THICKNESS_SMALL;
            case ZOOM_FACTOR_BREAKPOINT_MEDIUM:
               return OVERHEAT_THICKNESS_MEDIUM;
            case ZOOM_FACTOR_BREAKPOINT_LARGE:
            case ZOOM_FACTOR_BREAKPOINT_HUGE:
               return OVERHEAT_THICKNESS_LARGE;
            default:
               return OVERHEAT_THICKNESS_SMALL;
         }
      }
   }
}
