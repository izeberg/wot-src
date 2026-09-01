package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import fl.motion.easing.Cubic;
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.widgetsPanel.ChargeableBurstWidget;
   import net.wg.gui.utils.FrameHelper;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class BulletItem extends MovieClip implements IDisposable
   {
      
      private static const FRAME_LABEL_FIRST:String = "first";
      
      private static const FRAME_LABEL_OTHER:String = "other";
      
      private static const STATE_CHARGED:String = "charged";
      
      private static const STATE_SHOT:String = "shot";
      
      private static const STATE_EMPTY:String = "empty";
      
      private static const HIDE_SCALE:Number = 0.4;
      
      private static const SHOW_SCALE:Number = 1;
       
      
      public var bulletImg:MovieClip = null;
      
      public var bulletBg:MovieClip = null;
      
      private var _disposed:Boolean = false;
      
      private var _isShot:Boolean = false;
      
      private var _isEmpty:Boolean = false;
      
      private var _tween:Tween = null;
      
      private var _frameHelper:FrameHelper = null;
      
      private var _frames:Dictionary = null;
      
      private var _posX:int = 0;
      
      public function BulletItem()
      {
         var _loc3_:FrameLabel = null;
         super();
         this._frameHelper = new FrameHelper(this);
         this._frames = new Dictionary();
         var _loc1_:Array = this.currentLabels;
         var _loc2_:int = _loc1_.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc2_)
         {
            _loc3_ = _loc1_[_loc4_];
            if(_loc3_.name == STATE_EMPTY)
            {
               this._frames[_loc3_.name] = _loc3_.frame;
               addFrameScript(_loc3_.frame - 1,this.onItemShotComplete);
            }
            _loc4_++;
         }
      }
      
      public function anim(param1:Boolean, param2:Boolean, param3:Boolean) : void
      {
         var _loc5_:Number = NaN;
         this.removeTween();
         if(param1)
         {
            this.resetShot(param2);
         }
         var _loc4_:Number = !!param1 ? Number(Values.DEFAULT_ALPHA) : Number(Values.ZERO);
         _loc5_ = !!param1 ? Number(SHOW_SCALE) : Number(HIDE_SCALE);
         var _loc6_:Number = !!param1 ? Number(this._posX) : Number(Values.ZERO);
         if(param3)
         {
            this.x = _loc6_;
            this.alpha = _loc4_;
            this.scaleX = this.scaleY = _loc5_;
         }
         else
         {
            this._tween = new Tween(ChargeableBurstWidget.TWEEN_DURATION,this,{
               "alpha":_loc4_,
               "x":_loc6_,
               "scaleX":_loc5_,
               "scaleY":_loc5_
            },{
               "delay":Values.ZERO,
               "ease":Cubic.easeOut
            });
         }
      }
      
      public final function dispose() : void
      {
         var _loc1_:* = null;
         this.removeTween();
         stop();
         for(_loc1_ in this._frames)
         {
            addFrameScript(this._frames[_loc1_] - 1,null);
         }
         App.utils.data.cleanupDynamicObject(this._frames);
         this._frames = null;
         this._frameHelper.dispose();
         this._frameHelper = null;
         this.bulletImg = null;
         this.bulletBg = null;
         this._disposed = true;
      }
      
      public function init(param1:int, param2:int) : void
      {
         var _loc3_:String = param1 == 0 ? FRAME_LABEL_FIRST : FRAME_LABEL_OTHER;
         this.bulletImg.gotoAndStop(_loc3_);
         this.bulletBg.gotoAndStop(_loc3_);
         this._posX = param2;
         this.x = Values.ZERO;
         this.scaleX = this.scaleY = HIDE_SCALE;
         this.alpha = Values.ZERO;
         this.anim(false,true,true);
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function shot(param1:Boolean, param2:Boolean, param3:Boolean) : void
      {
         if(this._isShot == param1)
         {
            return;
         }
         if(param1 && param2)
         {
            if(param3)
            {
               gotoAndStop(STATE_EMPTY);
            }
            else
            {
               gotoAndPlay(STATE_SHOT);
            }
         }
         this._isShot = param1;
      }
      
      private function onItemShotComplete() : void
      {
         this._isEmpty = true;
         dispatchEvent(new BulletsEvent(BulletsEvent.BURST_SHOT_ANIM_COMPLETED));
         stop();
      }
      
      private function removeTween() : void
      {
         if(this._tween)
         {
            this._tween.paused = true;
            this._tween.dispose();
            this._tween = null;
         }
      }
      
      private function resetShot(param1:Boolean) : void
      {
         gotoAndStop(!!param1 ? STATE_CHARGED : STATE_EMPTY);
         this._isShot = !param1;
         this._isEmpty = !param1;
      }
      
      public function get posX() : int
      {
         return this._posX;
      }
      
      public function get isEmpty() : Boolean
      {
         return this._isEmpty;
      }
      
      public function get isShot() : Boolean
      {
         return this._isShot;
      }
   }
}
