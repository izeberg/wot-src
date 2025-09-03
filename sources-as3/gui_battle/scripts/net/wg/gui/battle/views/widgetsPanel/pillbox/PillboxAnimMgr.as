package net.wg.gui.battle.views.widgetsPanel.pillbox
{
   import fl.motion.easing.Cubic;
   import fl.transitions.easing.Elastic;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.PILLBOX_SIEGE_WIDGET_CONST;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.motion.Tween;
   
   public class PillboxAnimMgr implements IDisposable
   {
      
      private static const START_SHAKE_DURATION:int = 60;
      
      private static const CONTINUE_SHAKE_DURATION:int = 600;
      
      private static const SHAKE_MAX_SHIFT_X:int = -4;
       
      
      private var _isDisposed:Boolean = false;
      
      private var _progress:Number = 0;
      
      private var _currentAnimID:String = "";
      
      private var _anim:PillboxAnim = null;
      
      private var _storage:Dictionary = null;
      
      private var _condition:String = "";
      
      private var _isUpdatable:Boolean = true;
      
      private var _state:String = "";
      
      private var _isInstantly:Boolean = false;
      
      private var _shakeTween:Tween = null;
      
      private var _lastUncriticalAnimID:String = "normal";
      
      public function PillboxAnimMgr(param1:PillboxAnim, param2:PillboxAnim, param3:PillboxAnim)
      {
         super();
         this._storage = new Dictionary();
         param1.visible = false;
         param2.visible = false;
         param3.visible = false;
         this._storage[PILLBOX_SIEGE_WIDGET_CONST.CONDITION_NORMAL] = param1;
         this._storage[PILLBOX_SIEGE_WIDGET_CONST.CONDITION_WARNING] = param2;
         this._storage[PILLBOX_SIEGE_WIDGET_CONST.CONDITION_CRITICAL] = param3;
         this.applyAnimID(PILLBOX_SIEGE_WIDGET_CONST.CONDITION_NORMAL,true);
      }
      
      public final function dispose() : void
      {
         this.removeShake();
         this._isDisposed = true;
         App.utils.data.cleanupDynamicObject(this._storage);
         this._storage = null;
         this._anim = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setUpdatable(param1:Boolean) : void
      {
         if(this._isUpdatable == param1)
         {
            return;
         }
         this._anim.isUpdatable = param1;
         this.applyAnimID(this._condition,param1);
         this.invalidateShake(param1);
         this._isUpdatable = param1;
      }
      
      public function setCondition(param1:String) : void
      {
         if(this._condition == param1)
         {
            return;
         }
         this.applyAnimID(param1,this._isUpdatable);
         this._condition = param1;
      }
      
      public function setProgress(param1:Number, param2:Number) : void
      {
         if(this._progress == param1)
         {
            return;
         }
         this._progress = param1;
         if(this._anim)
         {
            this._anim.applyProgress(this._progress,param2);
         }
      }
      
      public function setState(param1:String, param2:Boolean) : void
      {
         if(this._state == param1)
         {
            return;
         }
         this._state = param1;
         this._isInstantly = param2;
         this.applyState();
         this._isInstantly = false;
      }
      
      private function removeShake() : void
      {
         if(this._shakeTween)
         {
            this._shakeTween.paused = true;
            this._shakeTween.onComplete = null;
            this._shakeTween.dispose();
            this._shakeTween = null;
         }
      }
      
      private function applyAnimID(param1:String, param2:Boolean) : void
      {
         if(param1 == PILLBOX_SIEGE_WIDGET_CONST.CONDITION_CRITICAL && param2)
         {
            if(!(this._isUpdatable != param2 && this._anim.isInProgress))
            {
               return;
            }
            param1 = this._lastUncriticalAnimID;
         }
         if(this._currentAnimID == param1)
         {
            return;
         }
         if(!this._storage.hasOwnProperty(param1))
         {
            return;
         }
         var _loc3_:AnimSnapshot = null;
         if(this._anim)
         {
            _loc3_ = this._anim.getSnapshot();
            this._anim.clear();
            this._anim.visible = false;
         }
         if(this._currentAnimID != PILLBOX_SIEGE_WIDGET_CONST.CONDITION_CRITICAL)
         {
            this._lastUncriticalAnimID = this._currentAnimID;
         }
         this._currentAnimID = param1;
         this._anim = this._storage[param1];
         this._anim.visible = true;
         this._anim.x = Values.ZERO;
         if(_loc3_)
         {
            this._anim.setSnapshot(_loc3_);
         }
         if(this._shakeTween)
         {
            this.removeShake();
            this.addShake();
         }
      }
      
      private function applyState() : void
      {
         if(this._anim)
         {
            this._anim.applyState(this._state,this._isInstantly);
         }
      }
      
      private function invalidateShake(param1:Boolean) : void
      {
         this.removeShake();
         if(!param1)
         {
            this.addShake();
         }
      }
      
      private function addShake() : void
      {
         if(this._anim == null)
         {
            return;
         }
         this._shakeTween = new Tween(START_SHAKE_DURATION,this._anim,{"x":SHAKE_MAX_SHIFT_X},{
            "ease":Cubic.easeOut,
            "onComplete":this.onStartShakeComplete
         });
      }
      
      private function onStartShakeComplete() : void
      {
         this.removeShake();
         this._shakeTween = new Tween(CONTINUE_SHAKE_DURATION,this._anim,{"x":Values.ZERO},{
            "ease":Elastic.easeOut,
            "onComplete":this.onShakeComplete
         });
      }
      
      private function onShakeComplete() : void
      {
         this.removeShake();
      }
   }
}
