package net.wg.gui.battle.views.widgetsPanel.pillbox
{
   public class AnimSnapshot
   {
       
      
      private var _state:String = "";
      
      private var _isInTransition:Boolean = false;
      
      private var _inStartTransition:Boolean = false;
      
      private var _allowProgress:Boolean = false;
      
      private var _isUpdatable:Boolean = false;
      
      private var _progress:Number = 0;
      
      private var _timeLeft:Number = 0;
      
      private var _skippedProgress:Number = 0;
      
      private var _animProgressFromFrame:int = 0;
      
      private var _animProgressToFrame:int = 0;
      
      private var _currentFrame:int = 0;
      
      private var _isInPlay:Boolean = false;
      
      public function AnimSnapshot(param1:String, param2:Boolean, param3:Boolean, param4:Boolean, param5:Boolean, param6:Number, param7:Number, param8:Number, param9:int, param10:int, param11:int, param12:Boolean)
      {
         super();
         this._state = param1;
         this._isInTransition = param2;
         this._inStartTransition = param3;
         this._allowProgress = param4;
         this._isUpdatable = param5;
         this._progress = param6;
         this._timeLeft = param7;
         this._skippedProgress = param8;
         this._animProgressFromFrame = param9;
         this._animProgressToFrame = param10;
         this._currentFrame = param11;
         this._isInPlay = param12;
      }
      
      public function get state() : String
      {
         return this._state;
      }
      
      public function get isInTransition() : Boolean
      {
         return this._isInTransition;
      }
      
      public function get inStartTransition() : Boolean
      {
         return this._inStartTransition;
      }
      
      public function get allowProgress() : Boolean
      {
         return this._allowProgress;
      }
      
      public function get isUpdatable() : Boolean
      {
         return this._isUpdatable;
      }
      
      public function get progress() : Number
      {
         return this._progress;
      }
      
      public function get timeLeft() : Number
      {
         return this._timeLeft;
      }
      
      public function get skippedProgress() : Number
      {
         return this._skippedProgress;
      }
      
      public function get animProgressFromFrame() : int
      {
         return this._animProgressFromFrame;
      }
      
      public function get animProgressToFrame() : int
      {
         return this._animProgressToFrame;
      }
      
      public function get currentFrame() : int
      {
         return this._currentFrame;
      }
      
      public function get isInPlay() : Boolean
      {
         return this._isInPlay;
      }
   }
}
