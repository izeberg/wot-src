package net.wg.infrastructure.managers.utils.impl
{
   import net.wg.data.TweenConstraintsVO;
   import net.wg.data.constants.TweenTypes;
   import net.wg.infrastructure.managers.ITweenManagerHelper;
   
   public class TweenManagerHelper implements ITweenManagerHelper
   {
       
      
      private var _data:TweenConstraintsVO;
      
      private var _durationByType:Vector.<Object>;
      
      private var _disposed:Boolean = false;
      
      public function TweenManagerHelper(param1:TweenConstraintsVO)
      {
         super();
         this._data = param1;
         this._durationByType = new <Object>[{
            "types":TweenTypes.FADE_TYPES,
            "duration":param1.fadeDuration
         },{
            "types":TweenTypes.BLINKING_TYPES,
            "duration":param1.blinkingDuration
         },{
            "types":TweenTypes.MOVE_TYPES,
            "duration":param1.moveDuration
         },{
            "types":TweenTypes.GLOW_TYPES,
            "duration":param1.glowDuration
         },{
            "types":TweenTypes.SHADOW_TYPES,
            "duration":param1.shadowDuration
         },{
            "types":TweenTypes.TURN_TYPES,
            "duration":param1.halfTurnDuration
         }];
      }
      
      public function getFadeDuration() : int
      {
         return this._data.fadeDuration;
      }
      
      public function getFadeDurationSlow() : int
      {
         return this._data.fadeDuration << 1;
      }
      
      public function getFadeDurationFast() : int
      {
         return this._data.fadeDuration >> 1;
      }
      
      public function getMoveDuration() : int
      {
         return this._data.moveDuration;
      }
      
      public function getMoveDurationSlow() : int
      {
         return this._data.moveDuration << 1;
      }
      
      public function getMoveDurationFast() : int
      {
         return this._data.moveDuration >> 1;
      }
      
      public function getGlowDuration() : int
      {
         return this._data.glowDuration;
      }
      
      public function getGlowDurationSlow() : int
      {
         return this._data.glowDuration << 1;
      }
      
      public function getGlowDurationFast() : int
      {
         return this._data.glowDuration >> 1;
      }
      
      public function getShadowDuration() : int
      {
         return this._data.shadowDuration;
      }
      
      public function getShadowDurationFast() : int
      {
         return this._data.shadowDuration << 1;
      }
      
      public function getShadowDurationSlow() : int
      {
         return this._data.shadowDuration >> 1;
      }
      
      public function getBlinkingDuration() : int
      {
         return this._data.blinkingDuration;
      }
      
      public function getTranslationLength() : int
      {
         return this._data.translationLength;
      }
      
      public function getFadeAlphaMax() : int
      {
         return this._data.fadeAlphaMax;
      }
      
      public function getFadeAlphaMin() : int
      {
         return this._data.fadeAlphaMin;
      }
      
      public function getHalfTurnDuration() : int
      {
         return this._data.halfTurnDuration;
      }
      
      public function getHalfTurnDelay() : int
      {
         return this._data.halfTurnDelay;
      }
      
      public function getSimilarTypes(param1:String) : Vector.<String>
      {
         var _loc4_:Vector.<String> = null;
         var _loc2_:uint = this._durationByType.length;
         var _loc3_:int = 0;
         while(_loc3_ < _loc2_)
         {
            _loc4_ = this._durationByType[_loc3_].types;
            if(_loc4_.indexOf(param1) >= 0)
            {
               return _loc4_;
            }
            _loc3_++;
         }
         return new Vector.<String>(0);
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this._data = null;
         this._durationByType.splice(0,this._durationByType.length);
         this._durationByType = null;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
   }
}
