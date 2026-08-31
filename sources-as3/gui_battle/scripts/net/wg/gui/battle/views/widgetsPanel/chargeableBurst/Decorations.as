package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import fl.motion.easing.Cubic;
   import fl.motion.easing.Exponential;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.widgetsPanel.ChargeableBurstWidget;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class Decorations extends MovieClip implements IDisposable
   {
      
      private static const STATE_IDLE:String = "idle";
      
      private static const STATE_BURST_RELOADED:String = "burstModeReloaded";
      
      private static const SIDE_DECOR_STATE_NORMAL:String = "normal";
      
      private static const SIDE_DECOR_STATE_CHARGED:String = "charged";
      
      private static const ADDITIONAL_CLOSE_ANGLE_GAP:int = 2;
       
      
      public var leftSide:MovieClip = null;
      
      public var rightSide:MovieClip = null;
      
      public var glow:Sprite = null;
      
      private var _openAngle:Number = 0;
      
      private var _closeAngle:Number = 0;
      
      private var _disposed:Boolean = false;
      
      private var _tweenLeft:Tween = null;
      
      private var _tweenRight:Tween = null;
      
      private var _isBurstReloading:Boolean = false;
      
      public function Decorations()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.removeTweens();
         this.leftSide.stop();
         this.rightSide.stop();
         this.leftSide = null;
         this.rightSide = null;
         this.glow = null;
         this._disposed = true;
      }
      
      public function setBurstBullets(param1:Boolean) : void
      {
         if(param1)
         {
            this.leftSide.gotoAndPlay(SIDE_DECOR_STATE_CHARGED);
            this.rightSide.gotoAndPlay(SIDE_DECOR_STATE_CHARGED);
         }
         else
         {
            this.leftSide.gotoAndStop(SIDE_DECOR_STATE_NORMAL);
            this.rightSide.gotoAndStop(SIDE_DECOR_STATE_NORMAL);
         }
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setup(param1:Number, param2:Number) : void
      {
         this._openAngle = param1;
         this._closeAngle = param2 + ADDITIONAL_CLOSE_ANGLE_GAP;
         this._isBurstReloading = false;
         this.anim(false,true);
      }
      
      public function updateBurstReloadingState(param1:Boolean) : void
      {
         if(this._isBurstReloading == param1)
         {
            return;
         }
         if(this._isBurstReloading && !param1)
         {
            gotoAndPlay(STATE_BURST_RELOADED);
         }
         else
         {
            gotoAndStop(STATE_IDLE);
         }
         this._isBurstReloading = param1;
      }
      
      public function updateMode(param1:Boolean, param2:Boolean) : void
      {
         this.anim(param1,param2);
      }
      
      private function anim(param1:Boolean, param2:Boolean) : void
      {
         this.removeTweens();
         var _loc3_:Number = !!param1 ? Number(this._closeAngle) : Number(this._openAngle);
         var _loc4_:Number = !!param1 ? Number(Values.DEFAULT_ALPHA) : Number(Values.ZERO);
         var _loc5_:Function = !!param1 ? Cubic.easeOut : Exponential.easeOut;
         if(param2)
         {
            this.leftSide.rotation = _loc3_;
            this.rightSide.rotation = -_loc3_;
            this.leftSide.alpha = _loc4_;
            this.rightSide.alpha = _loc4_;
         }
         else
         {
            this._tweenLeft = new Tween(ChargeableBurstWidget.TWEEN_DURATION,this.leftSide,{
               "alpha":_loc4_,
               "rotation":_loc3_
            },{
               "delay":Values.ZERO,
               "ease":_loc5_
            });
            this._tweenRight = new Tween(ChargeableBurstWidget.TWEEN_DURATION,this.rightSide,{
               "alpha":_loc4_,
               "rotation":-_loc3_
            },{
               "delay":Values.ZERO,
               "ease":_loc5_
            });
         }
      }
      
      private function removeTweens() : void
      {
         if(this._tweenLeft)
         {
            this._tweenLeft.paused = true;
            this._tweenLeft.dispose();
            this._tweenLeft = null;
         }
         if(this._tweenRight)
         {
            this._tweenRight.paused = true;
            this._tweenRight.dispose();
            this._tweenRight = null;
         }
      }
   }
}
