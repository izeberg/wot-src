package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class Bullets extends MovieClip implements IDisposable
   {
      
      private static const STEP:int = 6;
      
      private static const BULLET_POS_Y:int = 107;
      
      private static const RADIAN_TO_ANGLE:Number = 180 / Math.PI;
      
      private static const RELOADING_TWEEN_DURATION:int = 700;
      
      private static const FIRST_ANIM_RUN_DELAY:int = 50;
      
      private static const HIDE_ALPHA:int = 0.1;
       
      
      private var _disposed:Boolean = false;
      
      private var _items:Vector.<BulletItem> = null;
      
      private var _reloadingTween:Tween = null;
      
      private var _isInReloading:Boolean = false;
      
      private var _isBurstReloading:Boolean = false;
      
      private var _shellsQuantityLeft:int = 0;
      
      public function Bullets()
      {
         super();
         this._items = new Vector.<BulletItem>();
      }
      
      public final function dispose() : void
      {
         this.removeReloadingAnimation();
         this.remove(this._items.length);
         this._items = null;
         this._disposed = true;
      }
      
      public function isAllEmpty() : Boolean
      {
         var _loc1_:BulletItem = null;
         for each(_loc1_ in this._items)
         {
            if(!_loc1_.isEmpty)
            {
               return false;
            }
         }
         return true;
      }
      
      public function isAllMadeShot() : Boolean
      {
         var _loc1_:BulletItem = null;
         for each(_loc1_ in this._items)
         {
            if(!_loc1_.isShot)
            {
               return false;
            }
         }
         return true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function maxVisualAngle() : Number
      {
         if(!this._items.length)
         {
            return Values.ZERO;
         }
         var _loc1_:Number = Math.abs(this._items[0].posX) + (STEP >> 1);
         return Math.asin(_loc1_ / BULLET_POS_Y) * RADIAN_TO_ANGLE;
      }
      
      public function setShellsQuantityLeft(param1:Number, param2:Boolean) : void
      {
         this._shellsQuantityLeft = param1;
         if(param2 && !this.isShooting())
         {
            this.updateMode(param2,false);
         }
      }
      
      public function setup(param1:int) : void
      {
         this._isBurstReloading = false;
         this._isInReloading = false;
         this._shellsQuantityLeft = Values.ZERO;
         this.remove(this._items.length - param1);
         this.add(param1 - this._items.length);
         this.layout();
      }
      
      public function update(param1:Number, param2:Boolean, param3:Boolean) : void
      {
         var _loc4_:BulletItem = null;
         var _loc5_:int = Math.min(this._items.length - 1,this._shellsQuantityLeft - 1);
         var _loc6_:int = _loc5_;
         while(_loc6_ >= 0)
         {
            _loc4_ = this._items[_loc6_];
            _loc4_.shot(_loc5_ - _loc6_ < param1,param2,param3);
            _loc6_--;
         }
         this.tryRunReloadBurstAnimation(param2);
      }
      
      public function updateBurstReloading(param1:Boolean, param2:Boolean) : void
      {
         if(this._isInReloading == param1)
         {
            return;
         }
         this._isInReloading = param1;
         this.tryRunReloadBurstAnimation(param2);
      }
      
      public function updateMode(param1:Boolean, param2:Boolean) : void
      {
         var _loc3_:BulletItem = null;
         var _loc4_:Boolean = false;
         var _loc5_:int = this._items.length - 1;
         var _loc6_:int = this._shellsQuantityLeft - 1;
         var _loc7_:int = _loc5_;
         while(_loc7_ >= 0)
         {
            _loc3_ = this._items[_loc7_];
            _loc4_ = param1 && _loc7_ <= _loc6_;
            _loc3_.anim(param1,_loc4_,param2);
            _loc7_--;
         }
         this.tryRunReloadBurstAnimation(param1);
      }
      
      private function isShooting() : Boolean
      {
         var _loc1_:BulletItem = null;
         for each(_loc1_ in this._items)
         {
            if(_loc1_.isShot && !_loc1_.isEmpty)
            {
               return true;
            }
         }
         return false;
      }
      
      private function tryRunReloadBurstAnimation(param1:Boolean) : void
      {
         var _loc2_:Boolean = this._isInReloading && param1 && !this.isBurstShotMade;
         if(this._isBurstReloading == _loc2_)
         {
            return;
         }
         this._isBurstReloading = _loc2_;
         if(this._isBurstReloading)
         {
            this.runReloadingTween(Values.DEFAULT_ALPHA,FIRST_ANIM_RUN_DELAY);
         }
         else
         {
            this.removeReloadingAnimation();
            this.alpha = Values.DEFAULT_ALPHA;
            dispatchEvent(new BulletsEvent(BulletsEvent.RELOADING_ANIM_CHANGE,false));
         }
      }
      
      private function runReloadingTween(param1:Number, param2:Number = 0) : void
      {
         var _loc3_:Number = NaN;
         if(this._reloadingTween == null)
         {
            _loc3_ = param1 == HIDE_ALPHA ? Number(Values.DEFAULT_ALPHA) : Number(HIDE_ALPHA);
            this._reloadingTween = new Tween(RELOADING_TWEEN_DURATION,this,{"alpha":param1},{
               "delay":param2,
               "ease":Cubic.easeOut,
               "onComplete":this.onReloadingTweenComplete,
               "data":{"toAlpha":_loc3_}
            });
         }
      }
      
      private function onReloadingTweenComplete(param1:Tween) : void
      {
         var _loc2_:Number = param1.data["toAlpha"];
         this.removeReloadingAnimation();
         this.runReloadingTween(_loc2_);
         dispatchEvent(new BulletsEvent(BulletsEvent.RELOADING_ANIM_CHANGE,true));
      }
      
      private function removeReloadingAnimation() : void
      {
         if(this._reloadingTween)
         {
            this._reloadingTween.paused = true;
            this._reloadingTween.onComplete = null;
            this._reloadingTween.data = null;
            this._reloadingTween.dispose();
            this._reloadingTween = null;
         }
      }
      
      private function remove(param1:int) : void
      {
         var _loc2_:BulletItem = null;
         while(param1 > 0)
         {
            _loc2_ = this._items.pop();
            this.removeChild(_loc2_);
            _loc2_.removeEventListener(BulletsEvent.BURST_SHOT_ANIM_COMPLETED,this.onItemShotComplete);
            _loc2_.dispose();
            param1--;
         }
         _loc2_ = null;
      }
      
      private function add(param1:int) : void
      {
         var _loc2_:BulletItem = null;
         while(param1 > 0)
         {
            _loc2_ = App.utils.classFactory.getComponent(Linkages.CHARGEABLE_BURST_BULLET,BulletItem);
            this.addChild(_loc2_);
            this._items.push(_loc2_);
            param1--;
         }
      }
      
      private function layout() : void
      {
         var _loc1_:BulletItem = null;
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         var _loc2_:int = this._items.length - 1;
         _loc3_ = -(STEP * _loc2_ >> 1);
         _loc4_ = _loc2_;
         while(_loc4_ >= 0)
         {
            _loc1_ = this._items[_loc4_];
            _loc1_.x = _loc3_;
            _loc1_.y = BULLET_POS_Y;
            _loc1_.init(_loc4_,_loc3_);
            _loc1_.addEventListener(BulletsEvent.BURST_SHOT_ANIM_COMPLETED,this.onItemShotComplete);
            _loc3_ += STEP;
            _loc4_--;
         }
      }
      
      private function get isBurstShotMade() : Boolean
      {
         var _loc1_:int = Math.min(this._items.length - 1,this._shellsQuantityLeft - 1);
         return _loc1_ >= Values.ZERO ? Boolean(this._items[_loc1_].isShot) : Boolean(true);
      }
      
      private function onItemShotComplete(param1:BulletsEvent) : void
      {
         dispatchEvent(new BulletsEvent(BulletsEvent.BURST_SHOT_ANIM_COMPLETED));
      }
   }
}
