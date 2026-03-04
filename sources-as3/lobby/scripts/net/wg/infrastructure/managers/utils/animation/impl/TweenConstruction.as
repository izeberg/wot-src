package net.wg.infrastructure.managers.utils.animation.impl
{
   import flash.display.DisplayObject;
   import net.wg.data.TweenDataByType;
   import net.wg.data.constants.DelayTypes;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.TweenTypes;
   import net.wg.infrastructure.interfaces.ISimpleTweenPropertiesVO;
   import net.wg.infrastructure.interfaces.ITween;
   import net.wg.infrastructure.interfaces.ITweenConstructionHandler;
   import net.wg.infrastructure.interfaces.ITweenTypesDuration;
   import net.wg.infrastructure.managers.ITweenManagerHelper;
   import net.wg.utils.IAssertable;
   import net.wg.utils.ICommons;
   import net.wg.utils.IDataUtils;
   import net.wg.utils.ITweenAnimator;
   import net.wg.utils.animation.ITweenConstruction;
   import org.idmedia.as3commons.util.Iterator;
   import org.idmedia.as3commons.util.Map;
   
   public class TweenConstruction implements ITweenConstruction
   {
      
      private static var identicalTypes:Vector.<TweenDataByType>;
      
      private static const GLOBAL_DELAY_IDX:int = 0;
      
      private static const LOCAL_DELAY_IDX:int = 1;
       
      
      private var _tweenTypesMap:Map = null;
      
      private var _pythonTweenCreators:Map = null;
      
      private var _target:DisplayObject = null;
      
      private var _tweensData:Vector.<TweenLinkedObjects>;
      
      private var _tweenConstructionHandler:ITweenConstructionHandler = null;
      
      private var _firstPlayingElement:TweenLinkedObjects = null;
      
      private var _lastPlayingElement:TweenLinkedObjects = null;
      
      private var _tweenWrapper:TweenWrapper = null;
      
      private var _startStateTarget:Object;
      
      private var _stateTargetAfterAnim:Object;
      
      private var _disposed:Boolean = false;
      
      public function TweenConstruction(param1:DisplayObject, param2:ITweenConstructionHandler)
      {
         this._tweensData = new Vector.<TweenLinkedObjects>(0);
         this._startStateTarget = {};
         this._stateTargetAfterAnim = {};
         super();
         var _loc3_:IDataUtils = App.utils.data;
         identicalTypes = new <TweenDataByType>[new TweenDataByType(TweenTypes.MOVE_TYPES,this.tweenMgrHelper.getMoveDuration()),new TweenDataByType(TweenTypes.FADE_TYPES,this.tweenMgrHelper.getFadeDuration()),new TweenDataByType(TweenTypes.GLOW_TYPES,this.tweenMgrHelper.getGlowDuration()),new TweenDataByType(TweenTypes.SHADOW_TYPES,this.tweenMgrHelper.getShadowDuration()),new TweenDataByType(TweenTypes.TURN_TYPES,this.tweenMgrHelper.getHalfTurnDuration())];
         this._tweenTypesMap = _loc3_.createMap([Linkages.GLOW_IN_ANIM,TweenTypes.GLOW_IN,Linkages.GLOW_OUT_ANIM,TweenTypes.GLOW_OUT,Linkages.SHADOW_IN_ANIM,TweenTypes.SHADOW_IN,Linkages.SHADOW_OUT_ANIM,TweenTypes.SHADOW_OUT]);
         var _loc4_:ITweenAnimator = this.getAnimator();
         this._pythonTweenCreators = _loc3_.createMap([TweenTypes.FADE_IN,_loc4_.addFadeInAnimEx,TweenTypes.FADE_OUT,_loc4_.addFadeOutAnimEx,TweenTypes.MOVE_DOWN,_loc4_.addMoveDownAnimEx,TweenTypes.MOVE_UP,_loc4_.addMoveUpAnimEx,TweenTypes.TURN_HALF,_loc4_.addHalfTurnAnimEx]);
         this._target = param1;
         this.createStartParams();
         this._tweenWrapper = new TweenWrapper(param1.parent,param1);
         this._tweenConstructionHandler = param2;
      }
      
      private static function getTweenSettingByType(param1:String) : ITweenTypesDuration
      {
         var _loc2_:int = 0;
         while(_loc2_ < identicalTypes.length)
         {
            if(identicalTypes[_loc2_].types.indexOf(param1))
            {
               return identicalTypes[_loc2_];
            }
            _loc2_++;
         }
         return null;
      }
      
      public function addFadeIn(param1:int, param2:String = "global") : ITweenConstruction
      {
         this.createPythonTween(TweenTypes.FADE_IN,param1,param2);
         return this;
      }
      
      public function addFadeOut(param1:int, param2:String = "global") : ITweenConstruction
      {
         this.createPythonTween(TweenTypes.FADE_OUT,param1,param2);
         return this;
      }
      
      public function addMoveUp(param1:int, param2:String = "global") : ITweenConstruction
      {
         this.createPythonTween(TweenTypes.MOVE_UP,param1,param2);
         return this;
      }
      
      public function addMoveDown(param1:int, param2:String = "global") : ITweenConstruction
      {
         this.createPythonTween(TweenTypes.MOVE_DOWN,param1,param2);
         return this;
      }
      
      public function addHalfTurn(param1:int, param2:String = "global") : ITweenConstruction
      {
         this.createPythonTween(TweenTypes.TURN_HALF,param1,param2);
         return this;
      }
      
      public function addTween(param1:ITween, param2:int, param3:String = "global") : ITweenConstruction
      {
         if(param1.memberData == null)
         {
            param1.memberData = {"type":TweenTypes.USER_TWEEN};
         }
         else
         {
            param1.memberData.type = TweenTypes.USER_TWEEN;
         }
         this.addInStack(new TweenLinkedObjects(param1,param2,param3));
         return this;
      }
      
      public function start() : void
      {
         var _loc1_:TweenLinkedObjects = null;
         var _loc2_:ITween = null;
         this._tweenWrapper.changeVisibilityFromTarget();
         for each(_loc1_ in this._tweensData)
         {
            _loc2_ = _loc1_.tween;
            _loc2_.resetAnimS();
            _loc2_.setPausedS(false);
         }
      }
      
      public function onComplete(param1:ITween) : void
      {
         var _loc3_:TweenLinkedObjects = null;
         var _loc2_:ISimpleTweenPropertiesVO = ISimpleTweenPropertiesVO(param1.props);
         if(this._tweenConstructionHandler != null)
         {
            this._tweenConstructionHandler.onComplete(_loc2_);
         }
         for each(_loc3_ in this._tweensData)
         {
            if(_loc3_ == this._lastPlayingElement && _loc3_.tween == param1)
            {
               if(this._tweenConstructionHandler != null)
               {
                  this._tweenConstructionHandler.constructionOnComplete(_loc2_);
               }
            }
         }
      }
      
      public function onStart(param1:ITween) : void
      {
         var _loc3_:TweenLinkedObjects = null;
         var _loc2_:ISimpleTweenPropertiesVO = ISimpleTweenPropertiesVO(param1.props);
         for each(_loc3_ in this._tweensData)
         {
            if(_loc3_ == this._firstPlayingElement && _loc3_.tween == param1)
            {
               if(this._tweenConstructionHandler != null)
               {
                  this._tweenConstructionHandler.constructionOnStart(_loc2_);
               }
               break;
            }
         }
         if(this._tweenConstructionHandler != null)
         {
            this._tweenConstructionHandler.onStart(_loc2_);
         }
      }
      
      public final function dispose() : void
      {
         var _loc1_:TweenLinkedObjects = null;
         this._disposed = true;
         while(this._tweensData.length > 0)
         {
            _loc1_ = this._tweensData.pop();
            App.tweenMgr.disposeTweenS(_loc1_.tween);
            _loc1_.dispose();
         }
         this._tweensData = null;
         this._firstPlayingElement = null;
         this._lastPlayingElement = null;
         this._tweenWrapper.dispose();
         this._tweenWrapper = null;
         this._target = null;
         this._tweenConstructionHandler = null;
         this._tweenTypesMap.clear();
         this._tweenTypesMap = null;
         this._pythonTweenCreators.clear();
         this._pythonTweenCreators = null;
         this._startStateTarget = null;
         this._stateTargetAfterAnim = null;
      }
      
      public function removeTween(param1:int) : void
      {
         var _loc8_:String = null;
         var _loc9_:Iterator = null;
         var _loc10_:Object = null;
         var _loc2_:String = "Not element with such index";
         var _loc3_:String = "Not element with such className";
         var _loc4_:TweenLinkedObjects = this._tweensData[param1];
         var _loc5_:IAssertable = this.getAsserter();
         var _loc6_:Boolean = param1 < this._tweensData.length && param1 >= 0;
         _loc5_.assert(_loc6_,_loc2_);
         var _loc7_:String = _loc4_.tween.memberData.type;
         if(this.findTweenDataByType(_loc7_).length == 1)
         {
            _loc8_ = null;
            _loc9_ = this._tweenTypesMap.entrySet().iterator();
            while(_loc9_.hasNext())
            {
               _loc10_ = _loc9_.next();
               if(_loc10_.getValue() == _loc7_)
               {
                  _loc8_ = _loc10_.getKey();
                  break;
               }
            }
            _loc5_.assertNotNull(_loc8_,_loc3_);
            this._tweenWrapper.removeAnimationByClassName(_loc8_);
         }
         App.tweenMgr.disposeTweenS(_loc4_.tween);
         this._tweensData[param1].dispose();
         this._tweensData.splice(param1,1);
         this._firstPlayingElement = this.findFirstPlayingElement();
         this._lastPlayingElement = this.findLastPlayingElement();
      }
      
      public function countTweens() : int
      {
         return this._tweensData.length;
      }
      
      public function getAllTweens() : Vector.<ISimpleTweenPropertiesVO>
      {
         var _loc1_:Vector.<ISimpleTweenPropertiesVO> = new Vector.<ISimpleTweenPropertiesVO>(0);
         var _loc2_:int = 0;
         while(_loc2_ < this._tweensData.length)
         {
            _loc1_.push(this._tweensData[_loc2_].tween.props);
            _loc2_++;
         }
         return _loc1_;
      }
      
      public function getTweenByIdx(param1:int) : ISimpleTweenPropertiesVO
      {
         var _loc2_:String = "Not element with such index!";
         this.getAsserter().assert(param1 < this._tweensData.length,_loc2_);
         return this._tweensData[param1].tween.props;
      }
      
      private function createStartParams() : void
      {
         var _loc2_:String = null;
         var _loc1_:Vector.<String> = new <String>["x","y","alpha","rotation","scaleX","scaleY"];
         for each(_loc2_ in _loc1_)
         {
            if(_loc2_ in this._target)
            {
               this._stateTargetAfterAnim[_loc2_] = this._startStateTarget[_loc2_] = this._target[_loc2_];
            }
         }
      }
      
      private function getAsserter() : IAssertable
      {
         return App.utils.asserter;
      }
      
      private function getAnimator() : ITweenAnimator
      {
         return App.utils.tweenAnimator;
      }
      
      private function getCommon() : ICommons
      {
         return App.utils.commons;
      }
      
      private function findTweenDataByType(param1:String) : Vector.<int>
      {
         var _loc2_:Vector.<int> = new Vector.<int>(0);
         var _loc3_:int = 0;
         while(_loc3_ < this._tweensData.length)
         {
            if(this._tweensData[_loc3_].tween.memberData.type == param1)
            {
               _loc2_.push(_loc3_);
            }
            _loc3_++;
         }
         return _loc2_;
      }
      
      private function createPythonTween(param1:String, param2:int, param3:String) : void
      {
         var _loc4_:ITween = null;
         this.setParamsToTarget(this._stateTargetAfterAnim);
         if(TweenTypes.MOVE_TYPES.indexOf(param1) >= 0)
         {
            _loc4_ = this._pythonTweenCreators.get(param1)(this._tweenWrapper,this._tweenWrapper.y);
         }
         else
         {
            _loc4_ = this._pythonTweenCreators.get(param1)(this._tweenWrapper);
         }
         var _loc5_:Object = TweenDataByType.getPropertyChanges(param1);
         if(_loc5_.propertyName in this._stateTargetAfterAnim)
         {
            if(_loc5_.type == TweenDataByType.TYPE_ADD)
            {
               this._stateTargetAfterAnim[_loc5_.propertyName] += _loc5_.value;
            }
            else if(_loc5_.type == TweenDataByType.TYPE_SET)
            {
               this._stateTargetAfterAnim[_loc5_.propertyName] = _loc5_.value;
            }
         }
         this.addInStack(new TweenLinkedObjects(_loc4_,param2,param3));
         this.setParamsToTarget(this._startStateTarget);
      }
      
      private function setParamsToTarget(param1:Object) : void
      {
         var _loc2_:* = null;
         for(_loc2_ in param1)
         {
            this._tweenWrapper[_loc2_] = param1[_loc2_];
         }
      }
      
      private function getDelays(param1:int, param2:String = "global") : Array
      {
         var _loc5_:TweenLinkedObjects = null;
         var _loc3_:int = 0;
         var _loc4_:int = 0;
         if(param2 == DelayTypes.GLOBAL)
         {
            _loc3_ = param1;
            _loc4_ = param1;
         }
         else if(param2 == DelayTypes.LOCAL)
         {
            _loc5_ = this._tweensData[this._tweensData.length - 1];
            _loc3_ = _loc5_.delay + _loc5_.tween.props.getDuration() + param1;
            _loc4_ = param1;
         }
         return [_loc3_,_loc4_];
      }
      
      private function addInStack(param1:TweenLinkedObjects) : void
      {
         var _loc2_:String = "Tweens with identical type will not be executed in at one time!";
         this.getAsserter().assert(this.tweensAreNotCrossedInTime(param1),_loc2_);
         var _loc3_:ITween = param1.tween;
         _loc3_.setHandler(this);
         var _loc4_:Array = this.getDelays(param1.delay,param1.type);
         _loc3_.setDelayS(_loc4_[GLOBAL_DELAY_IDX]);
         _loc3_.props.setGlobalDelay(_loc4_[GLOBAL_DELAY_IDX]);
         _loc3_.props.setLocalDelay(_loc4_[LOCAL_DELAY_IDX]);
         this._tweensData.push(param1);
         this._firstPlayingElement = this.findFirstPlayingElement();
         this._lastPlayingElement = this.findLastPlayingElement();
      }
      
      private function findFirstPlayingElement() : TweenLinkedObjects
      {
         var _loc3_:TweenLinkedObjects = null;
         var _loc1_:TweenLinkedObjects = null;
         if(this._tweensData.length > 0)
         {
            _loc1_ = this._tweensData[0];
         }
         var _loc2_:int = 1;
         while(_loc2_ < this._tweensData.length)
         {
            _loc3_ = this._tweensData[_loc2_];
            if(_loc3_.type == null && _loc1_.tween.props.getGlobalDelay() > _loc3_.tween.props.getGlobalDelay())
            {
               _loc1_ = _loc3_;
            }
            _loc2_++;
         }
         return _loc1_;
      }
      
      private function findLastPlayingElement() : TweenLinkedObjects
      {
         var _loc3_:TweenLinkedObjects = null;
         var _loc4_:int = 0;
         var _loc5_:int = 0;
         var _loc6_:TweenLinkedObjects = null;
         var _loc7_:int = 0;
         var _loc1_:TweenLinkedObjects = null;
         if(this._tweensData.length > 0)
         {
            _loc1_ = this._tweensData[0];
         }
         var _loc2_:int = 1;
         while(_loc2_ < this._tweensData.length)
         {
            _loc3_ = this._tweensData[_loc2_];
            if(_loc3_.type == null)
            {
               _loc4_ = _loc3_.tween.props.getGlobalDelay() + _loc3_.tween.props.getDuration();
               _loc5_ = _loc1_.tween.props.getGlobalDelay() + _loc1_.tween.props.getDuration();
               if(_loc5_ <= _loc4_)
               {
                  _loc1_ = _loc3_;
               }
            }
            else
            {
               _loc6_ = this._tweensData[_loc2_ - 1];
               _loc7_ = _loc6_.tween.props.getGlobalDelay() + _loc6_.tween.props.getDuration();
               if(_loc1_.tween.props.getGlobalDelay() <= _loc7_)
               {
                  _loc1_ = _loc3_;
               }
            }
            _loc2_++;
         }
         return _loc1_;
      }
      
      private function tweensAreNotCrossedInTime(param1:TweenLinkedObjects) : Boolean
      {
         var _loc6_:Object = null;
         var _loc7_:int = 0;
         var _loc8_:TweenLinkedObjects = null;
         var _loc9_:Boolean = false;
         var _loc2_:Vector.<String> = null;
         var _loc3_:uint = identicalTypes.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc3_)
         {
            _loc6_ = identicalTypes[_loc4_];
            if(_loc6_.types.indexOf(param1.tween.memberData.type) >= 0)
            {
               _loc2_ = _loc6_.types;
               _loc7_ = _loc6_.duration;
            }
            _loc4_++;
         }
         var _loc5_:uint = this._tweensData.length;
         _loc4_ = 0;
         while(_loc4_ < _loc5_)
         {
            _loc8_ = this._tweensData[_loc4_];
            if(!(_loc8_.type != null || param1.type != null && _loc8_.tween.getTargetDisplayObject() != param1.tween.getTargetDisplayObject()))
            {
               if(_loc2_.indexOf(_loc8_.tween.memberData.type) >= 0)
               {
                  _loc9_ = Math.abs(_loc8_.delay - param1.delay) >= _loc7_;
                  if(!_loc9_)
                  {
                     return false;
                  }
               }
            }
            _loc4_++;
         }
         return true;
      }
      
      private function get tweenMgrHelper() : ITweenManagerHelper
      {
         return App.tweenMgr.getTweenManagerHelper();
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
