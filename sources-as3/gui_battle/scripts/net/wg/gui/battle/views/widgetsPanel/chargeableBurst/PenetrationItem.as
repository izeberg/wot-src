package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import fl.motion.easing.Cubic;
   import flash.display.FrameLabel;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.widgetsPanel.ChargeableBurstWidget;
   import net.wg.gui.utils.FrameHelper;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class PenetrationItem extends MovieClip implements IDisposable
   {
      
      private static const STATE_IDLE:String = "idle";
      
      private static const STATE_ACTIVATE:String = "activate";
      
      private static const STATE_ACTIVATED:String = "activated";
       
      
      private var _disposed:Boolean = false;
      
      private var _angle:Number = 0;
      
      private var _isLast:Boolean = false;
      
      private var _isActive:Boolean = false;
      
      private var _isActivated:Boolean = false;
      
      private var _tween:Tween = null;
      
      private var _frameHelper:FrameHelper = null;
      
      private var _frames:Dictionary;
      
      public function PenetrationItem()
      {
         var _loc2_:FrameLabel = null;
         this._frames = new Dictionary();
         super();
         this._frameHelper = new FrameHelper(this);
         var _loc1_:int = currentLabels.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc1_)
         {
            _loc2_ = currentLabels[_loc3_];
            if(_loc2_.name == STATE_ACTIVATED)
            {
               this._frames[_loc2_.name] = _loc2_.frame;
               addFrameScript(_loc2_.frame - 1,this.onItemActivateComplete);
            }
            _loc3_++;
         }
      }
      
      public function activate(param1:Boolean, param2:Boolean, param3:Boolean) : void
      {
         if(this._isActive == param1)
         {
            return;
         }
         if(param1 && !param2)
         {
            if(param3)
            {
               gotoAndStop(STATE_ACTIVATED);
            }
            else
            {
               gotoAndPlay(STATE_ACTIVATE);
            }
         }
         this._isActive = param1;
      }
      
      public function anim(param1:Boolean, param2:Boolean) : void
      {
         var _loc4_:Number = NaN;
         this.removeTween();
         if(!param1)
         {
            this.resetCharge();
         }
         var _loc3_:Number = !!param1 ? Number(Values.ZERO) : Number(Values.DEFAULT_ALPHA);
         _loc4_ = !!param1 ? Number(Values.ZERO) : Number(this._angle);
         if(param2)
         {
            this.alpha = _loc3_;
            this.rotation = _loc4_;
         }
         else
         {
            this._tween = new Tween(ChargeableBurstWidget.TWEEN_DURATION,this,{
               "alpha":_loc3_,
               "rotation":_loc4_
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
         this._disposed = true;
      }
      
      public function init(param1:Number, param2:Boolean) : void
      {
         this._angle = param1;
         this._isLast = param2;
         rotation = param1;
         this.anim(false,true);
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      private function onItemActivateComplete() : void
      {
         this._isActivated = true;
         stop();
         if(this._isLast)
         {
            dispatchEvent(new Event(Event.COMPLETE));
         }
      }
      
      private function resetCharge() : void
      {
         gotoAndStop(STATE_IDLE);
         this._isActive = false;
         this._isActivated = false;
         this.alpha = Values.DEFAULT_ALPHA;
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
      
      public function get isActivated() : Boolean
      {
         return this._isActivated;
      }
      
      public function get isActive() : Boolean
      {
         return this._isActive;
      }
   }
}
