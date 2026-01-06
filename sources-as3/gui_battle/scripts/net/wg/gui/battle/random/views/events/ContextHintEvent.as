package net.wg.gui.battle.random.views.events
{
   import flash.events.Event;
   
   public class ContextHintEvent extends Event
   {
      
      public static const VISIBILITY_CHANGE:String = "visibilityChange";
       
      
      private var _hintType:int = 0;
      
      private var _isVisible:Boolean = false;
      
      public function ContextHintEvent(param1:String, param2:int, param3:Boolean, param4:Boolean = false, param5:Boolean = false)
      {
         super(param1,param4,param5);
         this._hintType = param2;
         this._isVisible = param3;
      }
      
      override public function clone() : Event
      {
         return new ContextHintEvent(type,this._hintType,this._isVisible,bubbles,cancelable);
      }
      
      public function get hintType() : uint
      {
         return this._hintType;
      }
      
      public function get isVisible() : Boolean
      {
         return this._isVisible;
      }
   }
}
